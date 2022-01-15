#Engineer Miguel Angel Ramirez Echeverry

from functions import *

if __name__ == '__main__':
    numberDays = 31
    starCriteria = 'saturday'
    repeatWeight = True

    try:
        sundayDays = getSundaysDays(numberDays=numberDays, starCriteria=starCriteria)
        dailyWeight = generateWeight(rangeM_F=(1,50), rangeSa=(50,70), rangeSu=(70,100))
        days = generateDays(numberDays=numberDays, starCriteria=starCriteria, dailyWeight=dailyWeight, sundayDays=sundayDays)
        print(days)

    except ValueError as error:
        print(error)



