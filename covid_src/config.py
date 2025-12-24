"""
list of countries
column names
rolling average window (e.g. 7 days)
file paths
"""
from pathlib import Path


class Configuration:

    BASE_FILE = Path(__file__).resolve().parent.parent #final_project
    DATA_PATH = BASE_FILE / "covid_data" / "covid-data.csv"
    DATA_URL = "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/vaccine_data/global_data/time_series_covid19_vaccine_global.csv"

