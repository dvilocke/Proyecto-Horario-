class Person:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight
        self.mustRestOneDay = False
        self.hoursWorked = 0

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
        return self.getHoursWorked


    @getMustRestOneDay.setter
    def setMustRestOneDay(self, newValue):
        self.mustRestOneDay = newValue

    @getHoursWorked.setter
    def setHoursWorked(self, newValue):
        self.hoursWorked = newValue