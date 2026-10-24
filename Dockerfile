# syntax=docker/dockerfile:1.4
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-slim AS runner

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY src/ ./src/
COPY tests/ ./tests/

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

USER 65532:65532

ENTRYPOINT ["python", "-m", "src.cli"]
CMD ["--ledger"]
