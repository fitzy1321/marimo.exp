# Export as a readonly app
marimo_edit:
    uv run marimo edit notebook.py

marimo_read:
    uv reade marimo read notebook.py

export_readonly:
    marimo export html-wasm notebook.py -o output_dir --mode run

# Export as an editable notebook
export_edit:
    marimo export html-wasm notebook.py -o output_dir --mode edit
