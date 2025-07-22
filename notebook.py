import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium", app_title="Fitzy1321 Marimo Notebook")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Welcome to my first Marimo Notebook!

    Hosted on Github Pages. Github [repo link](https://github.com/fitzy1321/marimo_exp)

    **FYI**: You can edit this notebook, but it *shouldn't* save to the server? I think?

    Anyway, not sure what this notebook will be next. Maybe I'll find an actually interesting dataset to anaylze and visualize?

    Maybe some kind of population data? IDK, some kind of large data set.
    """
    )
    return


@app.cell
def _():
    import os

    # Choose local csv or remote, depending on ENVs
    csv_path = (
        "assets/world_population.csv"
        if os.getenv("MISE_SHELL") or os.getenv("UV")
        else "https://raw.githubusercontent.com/fitzy1321/marimo_exp/refs/heads/main/assets/world_population.csv"
    )
    return (csv_path,)


@app.cell
def _(csv_path):
    import polars as pl

    pdf = pl.read_csv(csv_path, truncate_ragged_lines=True, separator=";")
    pdf
    return


if __name__ == "__main__":
    app.run()
