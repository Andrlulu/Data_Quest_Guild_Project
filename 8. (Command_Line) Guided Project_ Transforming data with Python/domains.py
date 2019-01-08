import read
import pandas as pd

pd.set_option('display.max_rows', 500)

df = read.load_data()

c_domain = df['url'].value_counts()

for name, row in c_domain[:100].items():
	print("{0}: {1}".format(name, row))

