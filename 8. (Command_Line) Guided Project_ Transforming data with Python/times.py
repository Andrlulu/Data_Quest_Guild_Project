import read
from dateutil.parser import parse

df = read.load_data()

def extract_hour(s):
	h = parse(s)
	return h.hour
hour = df['submission_time'].apply(extract_hour)

print(hour.value_counts())

def extract_year(s):
	y = parse(s)
	return y.year

year = df['submission_time'].apply(extract_year)

print(year.value_counts().head(50))

def extract_month(s):
	m = parse(s)
	return m.month

month = df['submission_time'].apply(extract_month)

print(month.value_counts())
