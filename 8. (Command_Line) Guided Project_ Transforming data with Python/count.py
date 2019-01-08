import collections
import read
import pandas as pd
import numpy as np

df = read.load_data()

combined_headline = ""

for i in range(len(df['headline'])):
	combined_headline += str(df['headline'].iloc[i])

headline_word_list = combined_headline.lower().split(' ')


c = collections.Counter(headline_word_list).most_common(100)
print(c)

