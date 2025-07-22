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
