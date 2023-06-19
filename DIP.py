from abc import ABC, abstractmethod

# Abstraction
class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

# Concrete Implementation
class MySQLConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to MySQL database...")

# High-level module depending on abstraction
class DataManager:
    def __init__(self, connector: DatabaseConnector):
        self.connector = connector

    def fetch_data(self):
        self.connector.connect()
        print("Fetching data from the database...")
        # Additional data processing logic

# Usage
mysql_connector = MySQLConnector()
data_manager = DataManager(mysql_connector)
data_manager.fetch_data()
