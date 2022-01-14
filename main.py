#Engineer Miguel Angel Ramirez Echeverry

from functions import *

if __name__ == '__main__':
    numberDays = 31
    starCriteria = 'saturday'
    try:
        sundayDays = getSundaysDays(numberDays=numberDays, starCriteria=starCriteria)
        print(sundayDays)
        result = generateWeight(numberDays=numberDays, weightRange=(1,100), repeatWeights=True)
        print(result)

    except ValueError as error:
        print(error)



