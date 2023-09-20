import polars as pl


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


spotify
# Making a plot
# def viz():
#     value_counts = spotify.select(pl.col("artist_name")).value_counts()
#     top_10_value_counts = value_counts.head(10)
#     top_10_value_counts = top_10_value_counts.to_pandas()
#     top_10_value_counts.plot(kind="bar", x="artist_name", y="count", figsize=(20, 12))
#     plt.xlabel("Top Artists")
#     plt.ylabel("Number of top tracks")
#     plt.title("Which artists had the most top tracks in the last few years?")
#     plt.show()

# viz()
