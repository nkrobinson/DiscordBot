import time

class Event(object):
    pass

class TimeEvent(Event):
    def __init__(self, title, author, time, date=""):
        self.title = title
        self.author = author
        self.time = time
        self.date = time.strftime("%d/%m/%Y")

class DateEvent(Event):
    def __init__(self, title, author, date, time="-1.0"):
        self.title = title
        self.author = author
        self.date = date
        self.time = time
