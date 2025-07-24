default:
    just --list

[doc("Export marimo notebook in edit mode")]
export_edit:
    uv run marimo export html-wasm notebook.py -o build --mode edit

[doc("Export to html-wasm app in readonly mode")]
export_readonly:
   uv run marimo export html-wasm notebook.py -o build --mode run

[doc("start marimo notebook in edit mode")]
marimo_edit:
    uv run marimo edit notebook.py

[doc("start marimo notebook in readonly mood")]
marimo_read:
    uv run marimo read notebook.py

[doc("Build a docker image with current 'notebook.py' marimo notebook")]
docker-build:
    docker build -t marimo-exp .

docker-run:
    docker run -d --rm -p 2718:8080 --add-host=host.docker.internal:host-gateway -v marmi-exp:/app/backend/data --name marimo-notebook marimo-exp:latest
    sleep 1
    open http://localhost:2718
