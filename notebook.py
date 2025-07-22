import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
def _():
    # import polars as pl
    # polar_df = pl.read_csv("large_random_data.csv")
    # polar_df
    import os

    import marimo as mo  # noqa: F401

    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    files
    return


if __name__ == "__main__":
    app.run()
