from db import get_all_data, NUM_FEATURES
import collections

data = []
target = []

for row in get_all_data():
    data.append([row['feat' + str(i)] for i in range(NUM_FEATURES)])
    target.append(row['sign'])
