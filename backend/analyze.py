#### SCRIPT TO ANALYZE data ####
# import polars 

from datetime import datetime
import pandas as pd

dict_folders = [{"country":"AU",
                "infosummary":["aggregate_job_postings_AU.csv",
                "job_postings_by_sector_AU.csv"],
                "date":datetime},
                {"country":"CA",
                "infosummary":[
                    "aggregate_job_postings_CA.csv",
                "job_postings_by_sector_CA.csv",
                "metro_job_postings_CA.csv",
                "provincial_postings_ca.csv" 
                ],
                "date":datetime},
                {"country":"DE",
                "infosummary":[
                    "aggregate_job_postings_DE.csv",
                "job_postings_by_sector_DE.csv"
                ],
                "date":datetime},
                {"country":"FR",
                "infosummary":[
                    "aggregate_job_postings_FR.csv",
                "job_postings_by_sector_FR.csv"
                ],
                "date":datetime},
                {"country":"GB",
                "infosummary":[
                    "aggregate_job_postings_GB.csv",
                "city_postings_gb.csv",
                "job_postings_by_sector_GB.csv",
                "regional_gb.csv" 
                ],
                "date":datetime},
                {"country":"IE",
                "infosummary":[
                    "aggregate_job_postings_IE.csv"
                ],
                "date":datetime},
                {"country":"US",
                "infosummary":[
                    "aggregate_job_postings_US.csv",
                "job_postings_by_sector_US.csv",
                "metro_job_postings_us.csv",
                "state_job_postings_us.csv" 
                ],
                "date":datetime}]


# Current path
# current_folder = os.path.dirname(__file__)  # Replace __file__ with your path if not in a script
current_folder = os.getcwd()

# Parent folder path
parent_folder = os.path.dirname(current_folder)
print(parent_folder)



for dicti in dict_folders:
    country_name = dicti["country"]
    files_country = dicti["infosummary"]
    for filei in files_country:
        dict_folders_path = os.path.join(parent_folder,country_name,filei)
        print(dict_folders_path)
        # Read the CSV file
        df = pd.read_csv(dict_folders_path)
        # Print the number of rows and columns
        print(f"File: {filei}")
        print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")



