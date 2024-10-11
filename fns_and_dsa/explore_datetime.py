import datetime

from future.backports.datetime import timedelta


def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date)


def calculate_future_date():
    number_of_days = input("Enter number of days to add to the current date: ")
    number_of_days = int(number_of_days)
    date_now = datetime.datetime.now()
    future_date = date_now + datetime.timedelta(days=number_of_days)
    print(f"Future date: {future_date}")


