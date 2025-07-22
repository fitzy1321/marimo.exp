import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
def _():
    import os
    from pathlib import Path
    from pprint import pprint
    import marimo as mo  # noqa: F401
    import polars as pl

    if "__MISE_ORIG_PATH" not in dict(os.environ):
        csv_path = "https://fitzy1321.github.io/marimo_exp/large_random_data.csv"
    else:
        csv_path = Path("assets/large_random_data.csv")
    
    polar_df = pl.read_csv(csv_path)
    polar_df
    return


if __name__ == "__main__":
    app.run()
