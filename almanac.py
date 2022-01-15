from turtle import pd, st
from typing import List
import pandas as pd


class Almanac:
    def __init__(self, days:List, persons:List) -> None:
        self.days = days
        self.persons = persons

        

    def seeDaysWithoutThePeople(self) -> str:
        #function that shows the days with less information, that's why the components were created -- it works
        index = [day.getNumberDay for day in self.days]
        readyToShow = []
        for day in self.days:
            component = f'day:{day.getDay}, weight:{day.getWeight}, weightUpdated:{day.getWeightUpdated}'
            readyToShow.append(component)

        return pd.Series(data=readyToShow, index=index)

    def countDaysWeightWithoutPeople(self)  -> str:
        #function that calculates the total of the days according to their weight without the people  -- it works
        return f'The sum total of the weights without the people is:{sum([day.getWeightUpdated for day in self.days])}'
