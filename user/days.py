from datetime import date, timedelta

yesterday = (date.today() + timedelta(days=-2)).strftime("%Y-%m-%d")
print(yesterday)