import datetime

class LogEntryBuilder:
    class LogEntry:
        __log_number = 1 #TODO: Sync with database
        def __init__(self):
            self.log_number = LogEntryBuilder.LogEntry.__log_number
            LogEntryBuilder.LogEntry.__log_number += 1

        def __str__(self):
            delimiter = " | "
            append = lambda string, value: string + delimiter + value
            output = str(self.log_number)
            output = append(append(append(append(append(append(
                output, self.username), self.date), self.time), self.description)
                , self.info), self.sus)
            return output

    def __init__(self, datetime: datetime = datetime.datetime.now()):
        self.reset(datetime)

    def reset(self, datetime: datetime = datetime.datetime.now()):
        self.product = LogEntryBuilder.LogEntry()
        self.product.date = datetime.date
        self.product.time = datetime.time

    def SetAttribute(self, name, value):
        """
        username: str
        date: datetime.date
        time: datetime.time
        description: str
        info: str
        sus: bool
        """
        self.product.__setattr__(name, value)

    def GetProduct(self):
        return self.product