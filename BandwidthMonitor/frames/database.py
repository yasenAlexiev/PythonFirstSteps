import sqlite3

import datetime

DATABASE_NAME = "internet_log.db"
DATE_FORMAT = "%Y-%m-%d-%H-%M-%S"


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS internet_speeds (
        date DATETIME,
        download_speed REAL,
        upload_speed REAL
    )""")

    conn.commit()
    conn.close()


def commit_data(date, download_speed, upload_speed):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO internet_speeds VALUES ('{date}', '{download_speed}', '{upload_speed}')")

    conn.commit()
    conn.close()


def get_last_minutes_data(minutes_delta):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    now = datetime.datetime.today()

    minutes_ago = (now - datetime.timedelta(minutes=minutes_delta)).strftime(DATE_FORMAT)

    cursor.execute("SELECT * FROM internet_speeds WHERE date >= ?", (minutes_ago,))
    rows = cursor.fetchall()

    conn.close()
    return rows


def read_data():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM internet_speeds")

    records = cursor.fetchall()

    for record in records:
        print(record)

    conn.commit()
    conn.close()