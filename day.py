class Day:
    def __init__(self,day:str, numberDay:int, weight:int, dayIsSunday:bool = False, numberPeople:int = 2) -> None:
        self.day = day 
        self.numberDay = numberDay
        self.weight = weight
        self.numberPeople = numberPeople
        self.dayIsSunday = dayIsSunday


    def __str__(self) -> str:
        return f'dia:{self.day}, numeroDia:{self.numberDay}, peso:{self.weight}, numeroPersonas:{self.numberPeople}'