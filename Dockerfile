FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS base

RUN apt-get update && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

FROM base AS deps
ADD . /app
WORKDIR /app

RUN uv sync --locked

EXPOSE 8080

RUN useradd -m app_user
USER app_user

FROM deps AS editmode

HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8080/health || exit 1
# CMD curl -f http://localhost:3000/health || exit 1


CMD ["uv", "run", "marimo", "edit", "notebook.py", "--host", "0.0.0.0", "-p", "8080", "--no-token"]
