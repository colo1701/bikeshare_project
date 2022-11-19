import pandas as pd
import tobis_library as tol

locs = {"chicago": "chicago.csv",
        "new york": "new_york_city.csv",
        "washington": "washington.csv"}

# city comparison for gender and birth year statistics
gen_locs = ["new york", "chicago"]

# month and day comparison for filter
fil_months = ["january", "february", "march", "april", "may", "june"]
fil_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

city = ""
fil_month = ""
fil_day = ""

tol.header()
print("Welcome!")
print("In the following you will be provided with bike sharing data by Motivate.")
print("You can choose a city first and then set some filters.\n")

# Ask user for location, validate the input and load csv-file:
while True:
    city = input("Which city do you want to see information about?\n(Chicago, New York or Washington): ").lower()
    if city in locs:
        df = pd.read_csv(locs[city])
        print("OK, your city of choice is {}.\n".format(city.title()))
        tol.full_line()
        print()
        break
    else: print("It looks like your input was incorrect. \nPlease choose one of the cities offered.\n")

# Convert "Start Time" strings to datetime:
df['Start Time'] = pd.to_datetime(df['Start Time'])

# Add columns for important variables:
df['Hour'] = df['Start Time'].dt.hour
df['Month'] = df['Start Time'].dt.month
df['Weekday'] = df['Start Time'].dt.dayofweek

# Set some filters, i.e. a favourite month or the favourite day of the week
while True:
    fil_month = input("Do you want to see information about a certain month?\nIf yes enter the month, if not just "
                      "press the Enter button.\n(January to June):").lower()
    if fil_month in fil_months:
        print("OK, the data will be filtered by {}.\n".format(fil_month.capitalize()))
        fil_month = tol.mostring_to_moint(fil_month)
        break
    elif fil_month == "":
        print("OK, no month filter will be set.\n")
        break
    else: print("It looks like your input was incorrect. \nPlease choose a month or press the Enter button to not set "
                "a month filter.\n")

while True:
    fil_day = input("Do you want to see information about a certain day of the week?\nIf yes, enter the day, if not "
                    "just press the Enter button: ").lower()
    if fil_day in fil_days:
        print("OK, the data will be filtered by {}.\n".format(fil_day.capitalize()))
        fil_day = tol.dastring_to_daint(fil_day)
        tol.full_line()
        print()
        break
    elif fil_day == "":
        print("OK, no day filter will be set.\n")
        tol.full_line()
        print()
        break
    else: print("It looks like your input was incorrect. \nPlease choose a day or press the Enter button to not set "
                "a day filter.\n")

if fil_day != "" and fil_month != "":
    df = df[(df.Month == fil_month) & (df.Weekday == fil_day)]
elif fil_day != "":
    df = df[(df.Weekday == fil_day)]
elif fil_month != "":
    df = df[(df.Month == fil_month)]

# Compute information
popular_hour = df['Hour'].mode()[0]
popular_month = tol.moint_to_mostring(df['Month'].mode()[0])
popular_weekday = tol.daint_to_dastring(df['Weekday'].mode()[0])

popular_start = df['Start Station'].mode()[0]
popular_stop = df['End Station'].mode()[0]
popular_route = df.groupby(['Start Station', 'End Station']).size().idxmax()

drive_time_tot = df["Trip Duration"].sum()
drive_time_avg = int(round(df["Trip Duration"].describe()[1], 1))

tot_time_days =  drive_time_tot // 86400
tot_time_hours = (drive_time_tot - (tot_time_days * 86400)) // 3600
tot_time_min = (drive_time_tot - (tot_time_days * 86400 + tot_time_hours *3600)) // 60
tot_time_sec = round(drive_time_tot - (tot_time_days * 86400 + tot_time_hours *3600 + tot_time_min * 60), 1)
avg_time_min = int(drive_time_avg // 60)
avg_time_sec = int(round(drive_time_avg % 60, 1))

tot_users = df.groupby("User Type").size()["Customer"] + df.groupby("User Type").size()["Subscriber"]
customers = df.groupby("User Type").size()["Customer"]
subscribers = df.groupby("User Type").size()["Subscriber"]

# Print general information about the hole data set
print("Here's the information about {}:\n".format(city.title()))

if fil_month == "": print("month with the highest amount of rides:              {}".format(popular_month))
if fil_day == "": print("day of the week with the highest amount of rides:    {}".format(popular_weekday))
print("hour of the day with the highest amount of rides:    {}\n".format(popular_hour))

print("most common start station:                           {}".format(popular_start))
print("most common final station:                           {}".format(popular_stop))
print("most common route:                                   {}".format(popular_route[0]))
print("                                                  to {}\n".format(popular_route[1]))

print("total rental time:                                   {}d {}h {}m {}s".format(int(tot_time_days),
                                                                                    int(tot_time_hours),
                                                                                    int(tot_time_min),
                                                                                    int(tot_time_sec)))
print("average rental time:                                 {}m {}s\n".format(avg_time_min, avg_time_sec))

print("customers:                                           {} (~{}%)".format(customers, round(customers*100/tot_users,
                                                                                               1)))
print("subscribers:                                         {} (~{}%)\n".format(subscribers,
                                                                                round(subscribers*100/tot_users, 1)))

if city in gen_locs:
    # Compute specific information for New York and Chicago only
    male = df.groupby("Gender").size()["Male"]
    female = df.groupby("Gender").size()["Female"]
    oldest = int(df["Birth Year"].min())
    youngest = int(df["Birth Year"].max())
    med_age = int(df["Birth Year"].median())

    # Print specific information for New York and Chicago only
    print("female users:                                        {} (~{}%)".format(female,
                                                                                  round(female*100/(male+female), 1)))
    print("male users:                                          {} (~{}%)\n".format(male,
                                                                                    round(male*100/(male+female), 1)))
    print("oldest user's birth year:                            {}".format(oldest))
    print("youngest user's birth year:                          {}".format(youngest))
    print("most common birth year:                              {}\n".format(med_age))
    tol.full_line()
    print()
else:
    tol.full_line()
    print()

data_it = 0
more_loop = False

while True:
    show_raw = input("Do you also want to see the raw data? (yes/no): ").lower()
    print()
    if show_raw == "no":
        print("OK, feel free to rerun the program and have a look on some other data!\n")
        tol.full_line()
        break
    elif show_raw == "yes":
        print(df.iloc[data_it:data_it+5])
        print()
        data_it = 5
        more_loop = True
        break
    else: print("It looks like your input was incorrect. Please type 'yes' or 'no'.\n")

if more_loop:
    while True:
        show_more = input("Do you also want to see the next 5 line sof data? (yes/no): ").lower()
        print()
        if show_more == "no":
            print("OK, feel free to rerun the program and have a look on some other data!\n")
            tol.full_line()
            break
        elif show_more == "yes":
            print(df.iloc[data_it:data_it+5])
            print()
            data_it += 5
        else: print("It looks like your input was incorrect. Please type 'yes' or 'no'.\n")