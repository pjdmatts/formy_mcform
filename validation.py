months = ['January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December']

def valid_month(month):
	if month.capitalize() in months:
		return month.capitalize()

def valid_day(day):
	if day.isdigit():
		day_int = int(day)
		if day_int > 0 and day_int < 32:
			return int(day)

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if year >= 1900 and year <= 2020:
			return year
