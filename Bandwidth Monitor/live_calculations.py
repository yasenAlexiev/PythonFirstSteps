
from datetime import datetime
from database import *





def log_information():
    date = datetime.datetime.today().strftime(DATE_FORMAT)

    commit_data(date, sum_for_hour_download, sum_for_hour_upload)

    read_data()
    get_last_minutes_data(5)

