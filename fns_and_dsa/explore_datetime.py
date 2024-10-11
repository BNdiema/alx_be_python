from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime('%Y-%m-%d %H:%M:%S'))


def calculate_future_date():
    number_of_days = input("Entre the number of days to add to the current date:")
    number_of_days = int(number_of_days)
    date_now = datetime.now()
    future_date = date_now + timedelta(days=number_of_days)
    print("Future date: ", future_date.strftime('%Y-%m-%d'))
