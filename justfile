# Export as a readonly app
export_readonly:
    marimo export html-wasm notebook.py -o output_dir --mode run

# Export as an editable notebook
export_edit:
    marimo export html-wasm notebook.py -o output_dir --mode edit
