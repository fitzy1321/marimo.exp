import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
def _():
    import os

    import marimo as mo  # noqa: F401
    import polars as pl

    # if not on 'my local'(i.e. has mise installed), get csv from github
    # TODO: need a better way to determine where this is being executed
    # choices: local, published to ghpages, deployed else where?
    csv_path = (
        "https://raw.githubusercontent.com/fitzy1321/marimo_exp/refs/heads/main/assets/large_random_data.csv"
        if "__MISE_ORIG_PATH" not in dict(os.environ)
        else "assets/large_random_data.csv"
    )

    polar_df = pl.read_csv(csv_path)
    polar_df
    return


if __name__ == "__main__":
    app.run()
