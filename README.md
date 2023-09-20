# Python - Basic descriptive statistics using POLARS library

[![CiCd](https://github.com/nogibjj/fj49_week3_ds_polars/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/fj49_week3_ds_polars/actions/workflows/cicd.yml)

# Spotify Data Analysis

This Python project analyzes data from the Spotify API, which is stored in a CSV file named `spotify.csv`. It provides insights into song lengths and identifies the top 10 artists with the most chart-topping hits between 2010 and 2022.

The csv file when read in polars looks like this:

<img width="672" alt="Screenshot 2023-09-17 at 11 51 47 PM" src="https://github.com/nogibjj/fj49_week3_ds_polars/assets/101464414/20eb5bb4-4c58-487e-b674-f0b1bc232d56">



## Features

Descriptive statistics on song lengths (in milliseconds) to showcase the variation:

- `Mean = 226033`
- `Median = 221653`
- `Mode = 236133`
- `Std = 42063`

Visualization of the top 10 artists with the most chart-topping hits.

Here is the visualization:

<img width="1580" alt="Screenshot 2023-09-10 at 7 11 13 PM" src="https://github.com/nogibjj/fj49_week2_ds/assets/101464414/cfc958df-4041-4c8f-be86-ab6885a69074">




## CI/CD Integration

This repository is integrated with a CI/CD template for automatic deployment of Python projects within a virtual environment. 

You can find the template [here]([https://github.com/farazjawedd/python-template-ids706]). Feel free to use the template for other projects!

