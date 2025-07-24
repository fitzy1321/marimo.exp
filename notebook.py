import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium", app_title="Fitzy1321 Marimo Notebook")


@app.cell
def _():
    import os

    import marimo as mo
    import polars as pl
    return mo, os, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Welcome to my first Marimo Notebook!

    Hosted on Github Pages. Github [repo link](https://github.com/fitzy1321/marimo_exp)

    **FYI**: You can edit this notebook, but it *shouldn't* save to the server? I think?

    Anyway, not sure what this notebook will be next. Maybe I'll find an actually interesting dataset to anaylze and visualize?

    Maybe some kind of population data? IDK, some kind of large data set.

    ---

    Found this World Population Dataset, from Kaggle. Link provided [here](https://www.kaggle.com/datasets/jinundjanun/population-world-2024).

    I have no idea how the data was sourced, method of collect, etc., but this notebook is only an experiment.

    None of the data here should be taken as fact. This is a tech demo of marimo and various notebook UI elements and techniques.

    Also, learning how to use polars with visulation libraries for real. I'm gonna try to make various interactive graphs, plots, charts, etc.

    I'll try to add some methodiology as I go.
    """
    )
    return


@app.cell
def _(os):
    # Choose local csv or remote, depending on ENVs
    csv_path = (
        "assets/world_population.csv"
        if os.getenv("MISE_SHELL") or os.getenv("UV")
        else "https://raw.githubusercontent.com/fitzy1321/marimo_exp/refs/heads/main/assets/world_population.csv"
    )

    print(f'Using this csv: {csv_path}')
    return (csv_path,)


@app.cell
def _(csv_path, pl):
    pdf = pl.read_csv(csv_path, truncate_ragged_lines=True, separator=";")
    pdf
    return (pdf,)


@app.cell
def _(pdf, pl):
    # What's the top 10 rated countries? What does 'Rank' meak here?
    top_10 = pdf.filter(pl.col("Rank").is_in(range(1, 11))).sort("Rank")
    top_10
    return


@app.cell
def _(pdf, pl):
    # What's the bottom 20 countries?

    # Get the highest number from 'Rank' col
    bottom_num = pdf.select(pl.col("Rank").max()).item()
    bottom_range = range(bottom_num, bottom_num - 20, -1)
    # use predicate to find bottom 10 counties
    bottom_10 = pdf.filter(pl.col("Rank").is_in(bottom_range)).sort("Rank")
    bottom_10
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Pie Chart of World Population, with a slider

    - Pie chart of world pop per year.
    - Slider changes year.
    """
    )
    return


@app.cell
def _(mo):
    # Population_{year} slider
    year_slider = mo.ui.slider(steps=[2000, 2010, 2015, 2020, 2022, 2024])
    year_slider
    return (year_slider,)


@app.cell
def _(pdf, year_slider):
    # Switches 'Population_{year}' Column string, based on the slider
    col = f"Population_{year_slider.value}"
    pdf[col]
    return


@app.cell
def _():
    # pie_chart = alt.Chart(pdf).mark_arc().encode(
    #     theta=col,
    #     color="Country/Territory"
    # )
    # pie_chart
    return


if __name__ == "__main__":
    app.run()
