#Engineer Miguel Angel Ramirez Echeverry

from functions import *

if __name__ == '__main__':
    numberDays = 31
    starCriteria = 'saturday'
    weightRange = (1,100)
    repeatWeight = True

    try:
        sundayDays = getSundaysDays(numberDays=numberDays, starCriteria=starCriteria)
        dailyWeight = generateWeight(numberDays=numberDays, weightRange=weightRange, repeatWeights=repeatWeight)
        days = generateDays(numberDays=numberDays, starCriteria=starCriteria, dailyWeight=dailyWeight, sundayDays=sundayDays)
        print(days)

    except ValueError as error:
        print(error)



