from typing import List, Tuple
import random

from day import Day

def getSundaysDays(numberDays:int, starCriteria:str) -> List:
    #function to get sundays ---  it works
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if type(numberDays) == int and type(starCriteria) == str:
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
            raise ValueError('getSundaysDays - the arguments do not meet the standard')
    else:
        raise ValueError('getSundaysDays - wrong argument(type)')


def checkRange(weightRange:Tuple) -> bool:
    #function to check the range argument, if it meets the standards --- it works
    if len(weightRange) == 2:
        if weightRange[0] > 0 and weightRange[1] > 0:
            if weightRange[0] < weightRange[1]:
                return True
    return False


def generateWeight(rangeM_F:Tuple, rangeSa:Tuple, rangeSu:Tuple) -> list:
    #function that generates the weight from Monday to Friday, then on Saturday and finally on Sunday, complies with the control parameters --- it works
    if type(rangeM_F) == tuple and type(rangeSa) == tuple and type(rangeSu) == tuple:
        if checkRange(rangeM_F) and checkRange(rangeSa) and checkRange(rangeSu):
            if rangeM_F < rangeSa:
                if rangeSa < rangeSu:
                    return [random.randint(rangeM_F[0], rangeM_F[1]), random.randint(rangeSa[0], rangeSa[1]), random.randint(rangeSu[0], rangeSu[1])]
                else:
                    raise ValueError('the ranges do not respect the order rangeM_F < rangeSa and rangeSa < rangeSu')
            else:
                raise ValueError('the ranges do not respect the order rangeM_F < rangeSa and rangeSa < rangeSu')
        else:
         raise ValueError('ranges do not meet standard')

    else:
        raise ValueError('generateWeight - wrong arguments(type)')


def generateDays(numberDays:int, starCriteria:str,  dailyWeight:List, sundayDays:List) -> List:
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    if type(numberDays) == int and type(starCriteria) == str and type(dailyWeight) == list and type(sundayDays) == list:
        if numberDays in (28,29,30,31) and starCriteria.lower() in weekdays:
            listDays = []
            counter = weekdays.index(starCriteria)
            objectDay = any  #Day(day=, numberDay=, weight=, dayIsSunday=False, numberPeople=2)

            for day in range(1, numberDays+1):

                if counter == len(weekdays):
                    counter = 0

                #dailyWeight[n] n->0(Monday-friday), n->1(saturday), n->2(sunday)

                if weekdays[counter] == 'sunday' and day in sundayDays:
                    #You have to update the weight because Sundays are worth two
                    objectDay = Day(day=weekdays[counter], numberDay=day, weight=dailyWeight[2], dayIsSunday=True)
                    objectDay.setWeightUpdated = objectDay.getWeight * objectDay.getWeightDaySunday
                    listDays.append(objectDay)

                elif weekdays[counter] == 'saturday':
                    objectDay = Day(day=weekdays[counter], numberDay=day, weight=dailyWeight[1])
                    objectDay.setWeightUpdated  =  objectDay.getWeight
                    listDays.append(objectDay)


                else:
                    objectDay = Day(day=weekdays[counter], numberDay=day, weight=dailyWeight[0])
                    objectDay.setWeightUpdated  =  objectDay.getWeight
                    listDays.append(objectDay)

                counter += 1
            
            return listDays

        else:
            raise ValueError('generateDays - the arguments do not meet the standard')
    else:
        raise ValueError('generateDays - wrong arguments(type)')


def getBestSchedule(schedules:List, bestScore:int, numberOperations:int) -> str:
    finalSchedule = None
    for schedule in schedules:
        if bestScore == list(schedule.keys())[0]:
            finalSchedule = schedule[bestScore]
    
    print(f'-------------------after {numberOperations} operations, the final schedule is-------------------')
    if finalSchedule is not None:
        print(f'schedule weight:{bestScore}\n')
        for day in finalSchedule:
            msg = f"{day.getDay}({day.getWeight})({day.getWeightUpdated}):{[f'{person.getName}({person.getWeight})' for person in day.getPointerToPersonsDay]}, {[f'{person.getName}({person.getWeight})' for person in day.getPointerToPersonsAfternoon]}"
            print(msg)
    else:
        raise ValueError('getBestSchedule - error finalschedule is None')
        

def getBestScore(scores:List) -> int:
    orderedList = sorted(scores)
    return orderedList[0]



