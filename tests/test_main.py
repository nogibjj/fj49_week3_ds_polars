import sys
import polars as pl
import matplotlib.pyplot as plt

# sys.path.append("/fj49_week3_ds_polars")
from sorc.main import mean, median, mode, std, viz, reader

spotify = reader()
mean = mean()
median = median()
mode = mode()
std = std()
viz = viz()


def test_mean():
    assert mean == int(
        spotify.select(pl.col("duration_ms"))
        .mean()
        .take(1)
        .to_pandas()["mean_duration_ms"]
    )


def test_median():
    assert median == int(
        spotify.select(pl.col("duration_ms"))
        .median()
        .take(1)
        .to_pandas()["median_duration_ms"]
    )


def test_mode():
    assert mode == int(
        spotify.select(pl.col("duration_ms"))
        .mode()
        .take(1)
        .to_pandas()["mode_duration_ms"]
    )


def test_std():
    assert std == int(
        spotify.select(pl.col("duration_ms"))
        .std()
        .take(1)
        .to_pandas()["std_duration_ms"]
    )


def test_viz():
    assert viz is not None  # asserts that viz is not empty
