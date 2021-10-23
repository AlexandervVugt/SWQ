import sqlite3

class DbSingleton:
    __instance = None

    def __init__(self):
        if DbSingleton.__instance is None:
            raise RuntimeError("Only one instance is allowed!")
        else:
            self.__connection = sqlite3.connect('my_db.db')
            DbSingleton.__instance = self
    
    def GetInstance():
        if DbSingleton.__instance is object:
            return DbSingleton.__instance
        else:
            DbSingleton.__instance = DbSingleton()
            return DbSingleton.__instance
