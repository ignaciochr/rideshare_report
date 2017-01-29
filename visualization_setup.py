import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import and clean up dataframe
df = datasets['df2']
df = df[['user_id_r', 'first_request_time', 'first_pickup_time']]
df['first_request_time'] =  pd.DataFrame(df['first_request_time'])
df['first_pickup_time'] =  pd.DataFrame(df['first_pickup_time'])
df['wait_time'] = df['first_pickup_time'] - df['first_request_time']

# Create new column to display wait time in seconds
df['wait_time_seconds'] = df['wait_time'] / np.timedelta64(1, 's')

# Remove outliers
outlyer_idx = df['wait_time_seconds'].apply(lambda x: x<251)
df3 = df[outlyer_idx]

# Plot results with seaborn 
sns.distplot(df3['wait_time_seconds'])
sns.distplot(df3['wait_time_seconds'], rug=True, hist=False)

# Find and print min and max values
min_wait = df3['wait_time_seconds'].min(axis=0)
max_wait = df3['wait_time_seconds'].max(axis=0)
mean_wait = df3['wait_time_seconds'].mean(axis=0)
print 'Minimum wait time (seconds) was: ', min_wait
print 'Maximum wait time (seconds) was: ', max_wait
print 'Average wait time (seconds) was: ', mean_wait
print ''
print ''
print 'Wait time distribution:'
