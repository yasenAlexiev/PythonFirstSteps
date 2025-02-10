import sqlite3

DATABASE_NAME = "internet_log.db"


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE internet_speeds (
        date text,
        download_speed real,
        upload_speed real
    )""")

    conn.commit()
    conn.close()


def commit_data(date, download_speed, upload_speed):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO internet_speeds VALUES ('{date}', '{download_speed}', '{upload_speed}')")

    conn.commit()
    conn.close()
