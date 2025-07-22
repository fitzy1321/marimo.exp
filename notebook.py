import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path

    import marimo as mo  # noqa: F401
    import polars as pl

    polar_df = pl.read_csv(mo.notebook_dir() or Path("./") / "large_random_data.csv")
    # polar_df
    # return
    import os

    cwd_path = Path(os.getcwd())
    os.chdir("..")
    os.listdir()


if __name__ == "__main__":
    app.run()
