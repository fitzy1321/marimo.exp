FROM python:3.13-slim

# Set UV_VERSION var?
COPY --from=ghcr.io/astral-sh/uv:0.8.2 /uv /uvx /bin/
# ENV UV_SYSTEM_PYTHON=1

ADD . /app
WORKDIR /app

RUN uv sync --locked

EXPOSE 8080

RUN useradd -m app_user
USER app_user

HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8080/health || exit 1
# CMD curl -f http://localhost:3000/health || exit 1


CMD ["marino", "run", "notebook.py", "--host", "0.0.0.0", "-p", "8080"]
