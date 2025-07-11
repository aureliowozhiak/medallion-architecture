import os
import pandas as pd
import psycopg2

class DB:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conn = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)

    def create_table(self, table_name, columns):
        cursor = self.conn.cursor()
        columns_with_types = [f"{col} TEXT" for col in columns]
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns_with_types)})")
        self.conn.commit()
        cursor.close()

    def insert_data(self, table_name, df):
        cursor = self.conn.cursor()
        for index, row in df.iterrows():
            values = [str(v) if v is not None else None for v in row.values]
            placeholders = ', '.join(['%s'] * len(values))
            cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", values)
        self.conn.commit()
        cursor.close()

    def execute_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def select_all_data_from_table(self, table_name, limit=10):
        query = f"SELECT * FROM {table_name} LIMIT {limit}"
        return self.execute_query(query)

    def close(self):
        self.conn.close()