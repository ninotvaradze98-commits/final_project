
# load CSV from:
# local file (data/)
# OR OWID URL


import pandas as pd
from final_project.covid_src.config import Configuration as config

def load_covid_data() -> pd.DataFrame:
    """
    Load COVID-19 dataset from local CSV file.
    """
    data = pd.read_csv(config.DATA_URL)
    return data

if __name__ == "__main__":
    df = load_covid_data()
    print(df.shape)
