# Goal

This data comes from a repo from indeed (https://github.com/hiring-lab/job_postings_tracker)

Create a minimal sumary of the content in different history points (since Feb 2022)

Create a perspective of current view (9April 2025) of Indeed stats per country

Check job-sctor titles and summarize

# We will use python


### Backend




```sh
cd ./backend

############ one time #############
conda create --prefix ./venv python=3.12
pip install requirements.txt
###################################

#activate conda env

conda activate ./venv

```

run locally the fastapi

```sh
uvicorn api.main:app --reload
```