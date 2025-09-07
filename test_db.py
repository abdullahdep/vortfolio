import pymysql
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Connect to the database
try:
    connection = pymysql.connect(
        host='gateway01.ap-northeast-1.prod.aws.tidbcloud.com',
        user='3TJFdzBsW6BQcdA.root',
        password='3xv6bY5a4oHNEUhh',
        database='test',
        port=4000,
        ssl={
            'ca': os.path.join(BASE_DIR, 'certs/isrgrootx1.pem')
        },
        charset='utf8mb4'
    )
    print("Successfully connected to the database!")
    connection.close()
except Exception as e:
    print(f"Error connecting to database: {e}")
