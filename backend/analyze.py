#### SCRIPT TO ANALYZE data ####
# import polars 

from datetime import datetime
import pandas as pd
You can get the current date in a numeric string format using Python's datetime module. Here's an example:
from datetime import datetime

# Get current date
current_date = datetime.now()
# Format as a number string (YYYYMMDD)
date_string = current_date.strftime("%Y%m%d")
print(date_string)




dict_folders = [{"country":"AU",
                "infosummary":["aggregate_job_postings_AU.csv",
                "job_postings_by_sector_AU.csv"],
                "date":date_string},
                {"country":"CA",
                "infosummary":[
                    "aggregate_job_postings_CA.csv",
                "job_postings_by_sector_CA.csv",
                "metro_job_postings_CA.csv",
                "provincial_postings_ca.csv" 
                ],
                "date":date_string},
                {"country":"DE",
                "infosummary":[
                    "aggregate_job_postings_DE.csv",
                "job_postings_by_sector_DE.csv"
                ],
                "date":date_string},
                {"country":"FR",
                "infosummary":[
                    "aggregate_job_postings_FR.csv",
                "job_postings_by_sector_FR.csv"
                ],
                "date":date_string},
                {"country":"GB",
                "infosummary":[
                    "aggregate_job_postings_GB.csv",
                "city_postings_gb.csv",
                "job_postings_by_sector_GB.csv",
                "regional_gb.csv" 
                ],
                "date":date_string},
                {"country":"IE",
                "infosummary":[
                    "aggregate_job_postings_IE.csv"
                ],
                "date":date_string},
                {"country":"US",
                "infosummary":[
                    "aggregate_job_postings_US.csv",
                "job_postings_by_sector_US.csv",
                "metro_job_postings_us.csv",
                "state_job_postings_us.csv" 
                ],
                "date":date_string}]



# Current path
# current_folder = os.path.dirname(__file__)  # Replace __file__ with your path if not in a script
current_folder = os.getcwd()

# Parent folder path
parent_folder = os.path.dirname(current_folder)
print(parent_folder)



col_table_name = []
col_file_name =[]
col_count_cols=[]
col_count_rows=[]
col_name_cols=[]
col_daterelease=[]

for dicti in dict_folders:
    country_name = dicti["country"]
    files_country = dicti["infosummary"]
    file_date =dicti["date"]
    for filei in files_country:
        dict_folders_path = os.path.join(parent_folder,country_name,filei)
        print(dict_folders_path)
        # Read the CSV file
        df = pd.read_csv(dict_folders_path)
        # Print the number of rows and columns
        print(f"File: {filei}")
        print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        col_table_name.append(country_name)
        col_file_name.append(filei)
        col_count_cols.append(df.shape[1])
        col_count_rows.append(df.shape[0])
        col_name_cols.append(";".join(df.columns.tolist()))
        col_daterelease.append(file_date)



df_summary = pd.DataFrame(
                {
            "CountryIndeedSymbol":col_table_name,
            "FileIndeedName":col_file_name,
            "n_cols":col_count_cols,
            "n_rows":col_count_rows,
            "colnames":col_name_cols,
            "date_release":col_daterelease
            }
        )


date_forcsv = dict_folders[0]["date"]

df_summary.to_csv(f"./outputs/df_summary{}.csv")
