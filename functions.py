from itertools import count
from typing import List, Tuple
import random
from day import Day

def getSundaysDays(numberDays:int, starCriteria:str) -> List:
    #function to get sundays ---  it works
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if numberDays in (28,29,30,31) and starCriteria.lower() in weekdays:
        sundaysDays = [] 
        counter = weekdays.index(starCriteria)
        days = [day for day in range(1, numberDays+1)]

        for day in days:

            if counter == len(weekdays):
                counter = 0

            if weekdays[counter] == 'sunday':
                sundaysDays.append(day)

            counter += 1

        return sundaysDays

    else:
        raise ValueError('getSundaysDays - wrong arguments')


def checkRange(weightRange:Tuple) -> bool:
    #function to check the range argument, if it meets the standards --- it works

    if len(weightRange) == 2:
        if weightRange[0] > 0 and weightRange[1] > 0:
            if weightRange[0] < weightRange[1]:
                return True
    return False


def generateWeight(numberDays:int, weightRange:Tuple, repeatWeights = True) -> List:
    #function to generate the weights of the days of the week --- it works
    if numberDays in (28,29,30,31):
        if type(weightRange) == tuple:
            if checkRange(weightRange):
                dailyWeight = []

                if repeatWeights:
                    for _ in range(1, numberDays+1):
                        weight = random.randint(weightRange[0], weightRange[1])
                        dailyWeight.append(weight)

                    return dailyWeight[::-1]

                else:
                    while True:
                        weight = random.randint(weightRange[0], weightRange[1])
                        if weight not in dailyWeight:
                            dailyWeight.append(weight)

                        if len(dailyWeight) == numberDays:
                            break

                    return dailyWeight[::-1]
            else:
                raise ValueError('generateDailyWeight - the argument weightRange does not meet standards')
        else:
            raise ValueError('generateDailyWeight - the argument weightRange does not meet standards')
    else:
        raise ValueError('generateDailyWeight - wrong arguments')


def generateDays(numberDays:int, starCriteria:str,  dailyWeight:List, sundayDays:List) -> List:
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if numberDays in (28,29,30,31) and starCriteria.lower() in weekdays:
        listDays = []
        counter = weekdays.index(starCriteria)
        objectDay = any  #Day(day=, numberDay=, weight=, dayIsSunday=False, numberPeople=2)

        for day in range(1, numberDays+1):

            if counter == len(weekdays):
                counter = 0

            if weekdays[counter] == 'sunday' and day in sundayDays:
                #You have to update the weight because Sundays are worth two
                objectDay = Day(day=weekdays[counter], numberDay=day, weight=dailyWeight[day-1], dayIsSunday=True, numberPeople=2)
                objectDay.setWeightUpdated = objectDay.getWeight * objectDay.getWeightDaySunday
                listDays.append(objectDay)

            else:
                objectDay = Day(day=weekdays[counter], numberDay=day, weight=dailyWeight[day-1])
                listDays.append(objectDay)
                pass

            counter += 1
        
        return listDays

    else:
        raise ValueError('generateDays - wrong arguments')