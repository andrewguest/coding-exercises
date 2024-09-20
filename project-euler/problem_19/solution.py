from datetime import datetime, timedelta

start_date: datetime = datetime(1901, 1, 1)
end_date: datetime = datetime(2000, 12, 31)
current_date: datetime = start_date
number_of_sundays: int = 0

while current_date <= end_date:
    if current_date.weekday() == 6 and current_date.day == 1:
        number_of_sundays += 1
    current_date += timedelta(days=1)

print(number_of_sundays)
