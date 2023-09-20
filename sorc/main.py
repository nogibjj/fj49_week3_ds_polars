import polars as pl
import matplotlib.pyplot as plt


# Reading the data
def reader():
    df = pl.read_csv("spotify.csv")
    return df


spotify = reader()
print(spotify)


# Basic stats
def mean():
    mean_duration = int(
        spotify.select(pl.col("duration_ms"))
        .mean()
        .take(1)
        .to_pandas()["mean_duration_ms"]
    )
    return mean_duration


def median():
    median_duration = int(
        spotify.select(pl.col("duration_ms"))
        .median()
        .take(1)
        .to_pandas()["median_duration_ms"]
    )
    return median_duration


def mode():
    mode_duration = int(
        spotify.select(pl.col("duration_ms"))
        .mode()
        .take(1)
        .to_pandas()["mode_duration_ms"]
    )
    return mode_duration


def std():
    std_duration = int(
        spotify.select(pl.col("duration_ms"))
        .std()
        .take(1)
        .to_pandas()["std_duration_ms"]
    )
    return std_duration


# Making a plot
def viz():
    frequency_df = spotify.groupby("artist_name").agg(
        pl.col("artist_name").count().alias("frequency")
    )
    sorted_df = frequency_df.sort("frequency")
    top_10_frequencies = sorted_df.tail(10)
    # top_10_frequencies_pandas = top_10_frequencies.to_pandas()
    plt.figure(figsize=(20, 12))
    plt.bar(top_10_frequencies["artist_name"], top_10_frequencies["frequency"])

    # top_10_frequencies.plot(kind="bar", x="artist_name", y="frequency", figsize=(20, 12))
    plt.xlabel("Top Artists")
    plt.ylabel("Number of top tracks")
    plt.title("Which artists had the most top tracks in the last few years?")
    plt.show()


viz()
