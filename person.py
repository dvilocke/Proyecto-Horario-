class Person:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight
        self.mustRestOneDay = False
        self.hoursWorked = 0
        self.restDay = 0

    @property
    def getName(self):
        return self.name

    @property
    def getWeight(self):
        return self.weight

    @property
    def getMustRestOneDay(self):
        return self.mustRestOneDay

    @property
    def getHoursWorked(self):
        return self.hoursWorked

    @property
    def getRestDay(self):
        return self.restDay

    @getMustRestOneDay.setter
    def setMustRestOneDay(self, newValue):
        self.mustRestOneDay = newValue

    @getHoursWorked.setter
    def setHoursWorked(self, newValue):
        self.hoursWorked = newValue

    @getRestDay.setter
    def setRestDay(self, newValue):
        self.restDay = newValue

    def resetData(self):
        self.mustRestOneDay = False
        self.hoursWorked = 0
        self.restDay = 0

    def __repr__(self) -> str:
        return f'Name:{self.name}-weight:{self.weight}-mustRestOneDay:{self.mustRestOneDay}-hoursWorked:{self.hoursWorked}-restDay:{self.restDay}'

    def __str__(self) -> str:
        return f'Name:{self.name}-weight:{self.weight}-mustRestOneDay:{self.mustRestOneDay}-hoursWorked:{self.hoursWorked}-restDay:{self.restDay}'