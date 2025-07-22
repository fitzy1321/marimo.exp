import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
def _():
    import os

    import marimo as mo

    # if not on 'my local'(i.e. has mise installed), get csv from github
    # TODO: need a better way to determine where this is being executed
    # choices: local, published to ghpages, deployed else where?
    csv_path = (
        "https://raw.githubusercontent.com/fitzy1321/marimo_exp/refs/heads/main/assets/large_random_data.csv"
        if "__MISE_ORIG_PATH" not in dict(os.environ)
        else "assets/large_random_data.csv"
    )
    return csv_path, mo


@app.cell
def _(csv_path):
    import polars as pl

    pdf = pl.read_csv(csv_path)
    pdf
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Welcome to my first Marimo Notebook!

    Hosted on Github Pages.
    """
    )
    return


if __name__ == "__main__":
    app.run()
