import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path

    import marimo as mo  # noqa: F401
    import polars as pl

    file_path = mo.notebook_dir() or Path("./")
    polar_df = pl.read_csv(file_path / "large_random_data.csv")
    polar_df
    return


if __name__ == "__main__":
    app.run()
