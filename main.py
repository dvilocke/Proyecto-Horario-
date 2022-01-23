#Engineer Miguel Angel Ramirez Echeverry
from functions import *
from person import Person
from almanac import Almanac
import sys

import pandas as pd

if __name__ == '__main__':

    '''
        Documentation
        numberDays -> are the days that make up a month  -> sys.argv[1]
        starCriteria ->  is where the selected month starts -> sys.argv[2]
    '''   

    numberDays = int(sys.argv[1])
    starCriteria = sys.argv[2]
    numberOperations = int(sys.argv[3])

    '''
    numberDays = 31
    starCriteria = 'saturday'
    numberOperations = 2
    '''

    schedules = []

    scores = []
    #scoresCopy = []

    #people who are going to enter the schedule

    peopleList = [
        Person(name='Miguel', weight=20), Person(name='Juan', weight=15), Person(name='Alejandro', weight=12), Person(name='Fran', weight=40),
        Person(name='Jhoana', weight=45), Person(name='Javier', weight=11), Person(name='Jaime', weight=10), Person(name='Ricardo', weight=50),
        Person(name='Ana', weight=22), Person(name='Jhon', weight=27), Person(name='Pepe', weight=33), Person(name='Jesus', weight=60)
        ]

    dailyWeight = generateWeight(rangeM_F=(1,50), rangeSa=(50,70), rangeSu=(70,100))

    try:
        for i in range(numberOperations):
            sundayDays = getSundaysDays(numberDays=numberDays, starCriteria=starCriteria)
            days = generateDays(numberDays=numberDays, starCriteria=starCriteria, dailyWeight=dailyWeight, sundayDays=sundayDays)
            almanac = Almanac(days=days, persons=peopleList, starCriteria=starCriteria)

            '''
            shows the schedule without people, and shows the weight of the generated schedule without people
            '''

            #print(almanac.seeDaysWithoutThePeople())
            #print(almanac.countDaysWeightWithoutPeople())

            '''
            shows the schedule with the people already assigned, it also shows the total weight with assigned people and without people
            '''

            schedule = almanac.generateScheduleWithPeople()

            #almanac.printSchedule()

            scores.append(list(schedule.keys())[0])
            #scoresCopy.append(list(schedule.keys())[0])

            schedules.append(schedule)

            print(f'calculated hour counter{i+1}')

            if len(scores) == 10:
                lowerScore = min(scores)
                indexMinor = scores.index(lowerScore)
                bestSchedule = schedules[indexMinor]

                scores = []
                schedules = []

                scores.append(lowerScore)
                schedules.append(bestSchedule)

        bestScore = getBestScore(scores=scores)
        #print(scoresCopy)

        finalSchedule = getBestSchedule(schedules=schedules, bestScore=bestScore, numberOperations=numberOperations)

        #print(scores)

    except ValueError as error:
        print(error)



