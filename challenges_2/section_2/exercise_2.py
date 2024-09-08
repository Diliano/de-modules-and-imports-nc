# ADD YOUR IMPORTS HERE
import datetime as dt

# PLEASE DO NOT MAKE CHANGES BELOW THIS LINE


def get_todays_date():
    today = dt.datetime.now().strftime("%d %B, %Y")
    return today


print(get_todays_date())
