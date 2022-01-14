def getSundaysDays(numberDays:int, starCriteria:str):
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
        return False