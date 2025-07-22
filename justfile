# Export as a readonly app
marimo_edit:
    uv run marimo edit notebook.py

marimo_read:
    uv run marimo read notebook.py

export_readonly:
   uv run marimo export html-wasm notebook.py -o build --mode run

# Export as an editable notebook
export_edit:
    uv run marimo export html-wasm notebook.py -o build --mode edit
