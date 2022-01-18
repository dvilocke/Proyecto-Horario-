#Engineer Miguel Angel Ramirez Echeverry
from functions import *
from person import Person
from almanac import Almanac

import pandas as pd

if __name__ == '__main__':

    '''
        Documentation
        numberDays -> are the days that make up a month  -> sys.argv[1]
        starCriteria ->  is where the selected month starts -> sys.argv[2]

    '''   
    numberDays = 31
    starCriteria = 'saturday'

    #people who are going to enter the schedule

    peopleList = [
        Person(name='Miguel', weight=20), Person(name='Juan', weight=15), Person(name='Alejandro', weight=12), Person(name='Fran', weight=40),
        Person(name='Jhoana', weight=45), Person(name='Javier', weight=11), Person(name='Jaime', weight=10), Person(name='Ricardo', weight=50),
        Person(name='Ana', weight=22), Person(name='Jhon', weight=27), Person(name='Pepe', weight=33), Person(name='Jesus', weight=60)
        ]

    try:
        sundayDays = getSundaysDays(numberDays=numberDays, starCriteria=starCriteria)
        dailyWeight = generateWeight(rangeM_F=(1,50), rangeSa=(50,70), rangeSu=(70,100))
        days = generateDays(numberDays=numberDays, starCriteria=starCriteria, dailyWeight=dailyWeight, sundayDays=sundayDays)
        almanac = Almanac(days=days, persons=peopleList, starCriteria=starCriteria)

        '''
        shows the schedule without people, and shows the weight of the generated schedule without people
        '''

        #print(almanac.seeDaysWithoutThePeople())
        #print(almanac.countDaysWeightWithoutPeople())

        almanac.generateScheduleWithPeople()
        almanac.printSchedule()

    except ValueError as error:
        print(error)



