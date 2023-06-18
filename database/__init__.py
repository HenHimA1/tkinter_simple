import sqlite3


class AppDatabase():
    def __init__(self):
        self.connection = sqlite3.connect('database/database.db')
        self.connection.row_factory = sqlite3.Row

    def create_record(self, table, data_dict):
        self.connection.execute(
            f"INSERT INTO {table} f{tuple(data_dict.keys())} VALUES f{tuple(data_dict.values())}")
        self.connection.commit()
        self.connection.close()

    def select_record(self, table, domain):
        cursor = self.connection.cursor()
        condition = " AND ".join([f"{val_domain[0]} {val_domain[1]} '{val_domain[2]}'" for val_domain in domain])
        cursor.execute(f"SELECT * FROM {table} WHERE {condition}")
        records = cursor.fetchall() 
        self.connection.close()
        return self.unpack(records)
    
    def unpack(self, records):
        datas = []
        for record in records:
            datas.append({key: record[key]  for key in record.keys()})
        return datas
    

    def execute(self, query):
        self.connection.execute(query)
        self.connection.commit()
        self.connection.close()