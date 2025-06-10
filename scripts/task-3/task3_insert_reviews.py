import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

#  Load environment variables
# -------------------------------
load_dotenv()  # Load variables from .env file

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

# Load cleaned dataset
df = pd.read_csv('./data/clean_bank_reviews.csv')


# -------------------------------
#  Connect to PostgreSQL
# -------------------------------
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
    print("✅ Connected to PostgreSQL database.")
except Exception as e:
    print("❌ Failed to connect to the database.")
    print(e)
    exit()

# Insert bank names (once)
banks = df['bank'].unique()
bank_id_map = {}
for bank in banks:
    cursor.execute("INSERT INTO banks (name) VALUES (%s) ON CONFLICT (name) DO NOTHING RETURNING bank_id;", (bank,))
    result = cursor.fetchone()
    if result:
        bank_id_map[bank] = result[0]
    else:
        cursor.execute("SELECT bank_id FROM banks WHERE name=%s", (bank,))
        bank_id_map[bank] = cursor.fetchone()[0]

# Insert reviews
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reviews (review_text, rating, review_date, source, bank_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        row['review'],
        int(row['rating']),
        row['date'],
        row['source'],
        bank_id_map[row['bank']]
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ All data inserted successfully.")
