import pandas as pd
import numpy as np
def load_data():
	data = pd.read_csv('hn_stories.csv', names = ['submission_time', 'upvotes', 'url', 'headline'])
	return data

if __name__ == "__main__":
	print(load_data().head())
