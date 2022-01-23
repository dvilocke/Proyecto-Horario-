class Day:
    def __init__(self,day:str, numberDay:int, weight:int, dayIsSunday:bool = False, weightMorning = 10, weightAfternoon = 12, numberPeople:int = 2, weightDaySunday = 2) -> None:
        self.day = day 
        self.numberDay = numberDay
        self.weight = weight
        self.numberPeople = numberPeople
        self.dayIsSunday = dayIsSunday
        self.weightUpdated = 0
        self.weightDaySunday = weightDaySunday

        #Data of the person

        self.pointerToPersonsDay = []
        self.pointerToPersonsAfternoon = []

        self.weightMorning = weightMorning
        self.weightAfternoon = weightAfternoon
        
    #get

    @property
    def getDay(self):
        return self.day

    @property
    def getNumberDay(self):
        return self.numberDay

    @property
    def getWeight(self):
        return self.weight

    @property
    def getNumberPeople(self):
        return self.numberPeople

    @property
    def getDayIsSunday(self):
        return self.dayIsSunday


    @property
    def getWeightUpdated(self):
        return self.weightUpdated

    @property
    def getWeightDaySunday(self):
        return self.weightDaySunday

    @property
    def getPointerToPersonsDay(self):
        return self.pointerToPersonsDay

    @property
    def getPointerToPersonsAfternoon(self):
        return self.pointerToPersonsAfternoon

    @property
    def getWeightMorning(self):
        return self.weightMorning

    @property 
    def getWeightAfternoon(self):
        return self.weightAfternoon

    #set 

    @getWeightUpdated.setter
    def setWeightUpdated(self, newValue):
        self.weightUpdated = newValue


    def stockReset(self):
        self.pointerToPersonsDay = []
        self.pointerToPersonsAfternoon = []

    def __repr__(self) -> str:
        return f'(day:{self.day}/dayNumber:{self.numberDay}/weight:{self.weight}/numberPeople:{self.numberPeople}/dayIsSunday:{"yes" if self.dayIsSunday == True else "No"}/weightUpdated:{self.weightUpdated}/weightDaySunday:{self.weightDaySunday})'


    def __str__(self) -> str:
        return f'(day:{self.day}/dayNumber:{self.numberDay}/weight:{self.weight}/numberPeople:{self.numberPeople}/dayIsSunday:{"yes" if self.dayIsSunday == True else "No"}/weightUpdated:{self.weightUpdated}/weightDaySunday:{self.weightDaySunday})'