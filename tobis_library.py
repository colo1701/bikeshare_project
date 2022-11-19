def daint_to_dastring(day: int) -> str:
    '''convert day integers to strings respective

    Returns:
        (str) "Monday" if x = 0
        (str) "Tuesday" if x = 1...
    '''
    if day == 0: return "Monday"
    elif day == 1: return "Tuesday"
    elif day == 2: return "Wednesday"
    elif day == 3: return "Thursday"
    elif day == 4: return "Friday"
    elif day == 5: return "Saturday"
    elif day == 6: return "Sunday"
    else: return "Value for day is invalid!"

def dastring_to_daint(day: str) -> int:
    '''convert month strings to integers respective

    Returns:
        (int) 0 if x = "Monday"
        (int) 1 if x = "Tuesday"...
    '''
    if day == "monday": return 0
    elif day == "tuesday": return 1
    elif day == "wednesday": return 2
    elif day == "thursday": return 3
    elif day == "friday": return 4
    elif day == "saturday": return 5
    elif day == "sunday": return 6
    else: return "Value for day is invalid!"

def moint_to_mostring(month: int) -> str:
    '''convert month integers to strings respective

    Returns:
        (str) "January" if x = 1
        (str) "February" if x = 2...
    '''
    if month == 1: return "January"
    elif month == 2: return "February"
    elif month == 3: return "March"
    elif month == 4: return "April"
    elif month == 5: return "May"
    elif month == 6: return "June"
    else: return "Value for month is invalid!"

def mostring_to_moint(month: str) -> int:
    '''convert month strings to integers respective

    Returns:
        (int) 1 if x = "January"
        (int) 1 if x = "February"...
    '''
    if month == "january": return 1
    elif month == "february": return 2
    elif month == "march": return 3
    elif month == "april": return 4
    elif month == "may": return 5
    elif month == "june": return 6
    else: return "Value for month is invalid!"

# from here it's just graphic stuff

def empty_line():
    print(("#" + " "*78 + "#"))

def full_line():
    print("#"*80)

def header():
    full_line()
    print("#                     __  __       _   _            _                          #")
    print("#                    |  \/  | ___ | |_(_)_   ____ _| |_ ___                    #")
    print("#                    | |\/| |/ _ \| __| \ \ / / _' | __/ _ \                   #")
    print("#                    | |  | | (_) | |_| |\ V / (_| | ||  __/                   #")
    print("#                    |_|  |_|\___/ \__|_| \_/ \__,_|\__\___|                   #")
    empty_line()
    full_line()
    print()
