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

    #person
    peopleList = [Person(name='Miguel', weight=20), Person(name='Juan', weight=15)]

    try:
        sundayDays = getSundaysDays(numberDays=numberDays, starCriteria=starCriteria)
        dailyWeight = generateWeight(rangeM_F=(1,50), rangeSa=(50,70), rangeSu=(70,100))
        days = generateDays(numberDays=numberDays, starCriteria=starCriteria, dailyWeight=dailyWeight, sundayDays=sundayDays)
        almanac = Almanac(days=days, persons=peopleList)


        print(almanac.seeDaysWithoutThePeople())
        print(almanac.countDaysWeightWithoutPeople())


    except ValueError as error:
        print(error)



