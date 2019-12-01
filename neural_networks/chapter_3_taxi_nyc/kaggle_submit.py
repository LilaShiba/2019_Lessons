import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import scale


def process_data(df):

    # get pickup times
    df['year'] = df['pickup_datetime'].dt.year
    df['month'] = df['pickup_datetime'].dt.month
    df['day'] = df['pickup_datetime'].dt.day
    df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
    df['hour'] = df['pickup_datetime'].dt.hour
    
    def create_time_features(df):
        df_key = pd.DataFrame(data = df['key'])
        df['year'] = df['pickup_datetime'].dt.year
        df['month'] = df['pickup_datetime'].dt.month
        df['day'] = df['pickup_datetime'].dt.day
        df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
        df['hour'] = df['pickup_datetime'].dt.hour
        df = df.drop(['pickup_datetime'], axis=1)
        #df = df.drop(['key'], axis=1)
        return df
    
    # preprocess data
    def preprocessing(df):
        print(df.isnull().sum())
        df = df.dropna()
        print(df.describe())
        return df
            
    # remove fare outliers
    def remove_fare_outliers(df,lower_bound, upper_bound):
        df = df[ (df['fare_amount'] > lower_bound) & (df['fare_amount'] <= upper_bound)]
        return df
        
    # replace rider outliers 
    def replace_passenger_outliers(df):
        df.loc[ df['passenger_count']==0, 'passenger_count']= 1 
        return df

    # check for geolocation outliers
    def check_geolocation(df):
        df.plot.scatter('pickup_longitude', 'pickup_latitude')
        plt.show()

    # only consider locations inside nyc
    def remove_lat_lon_outliers(df):
        nyc_min_lon = -74.05
        nyc_max_lon = -73.75

        nyc_min_lat = 40.63
        nyc_max_lat = 40.85
        
        for long in ['pickup_longitude', 'dropoff_longitude']:
            df = df[(df[long] > nyc_min_lon) & (df[long] < nyc_max_lon) ]

        for lat in ['pickup_latitude', 'dropoff_latitude']:
            df = df[(df[lat] > nyc_min_lat) & (df[lat] < nyc_max_lat)]
        return df
    
    # create distance feature
    def make_distance(df):
        def euc_distance(lat1, lon1, lat2, lon2):
            return (((lat1-lat2)**2 +(lon1-lon2)**2)**0.5)
        df['distance'] = euc_distance(df['pickup_latitude'], df['pickup_longitude'], df['dropoff_latitude'], df['dropoff_longitude'])
        #df.plot.scatter('fare_amount', 'distance')
        #plt.show()
        return df

    # copy main data
    #df2 = df.copy(deep=True)
    # dr
    print('Removing Null values')
    df = preprocessing(df)   
    print('Removing fare outliers') 
    df = remove_fare_outliers(df, lower_bound=0, upper_bound=100)
    print('Replacing passenger count outliers')
    df = replace_passenger_outliers(df)
    print('Removing location outliers')
    df = remove_lat_lon_outliers(df)
    print('Creating time features')
    df = create_time_features(df)
    print('Creating distance features')
    df = make_distance(df)
    print('Processing data done')
    return df

def visualize(df):
    # dict of landmarks in NYC to overlay rides 
    landmarks = {
        'JFK':(-73.78, 40.643),
        'LGA':(-73.87, 40.77),
        'Midtown':(-73.98, 40.76),
        'Lower Manhattan':(-74.00, 40.72),
        'Upper Manhattan':(-73.94, 40.82),
        'Brooklyn':(-73.94, 40.66)
        }   
    # hour
    def hour(df):
        df['hour'].plot.hist(bins=24, ec='blue')
        plt.title('Rides by Hour')
        plt.xlabel("Ride per Hour")
        plt.show()

    # day of week
    def day_of_week(df):
        df['day_of_week'].plot.hist(bins=np.arange(8)-0.5, ylim= (60000, 75000), ec='black')
        plt.title("Rides by Day of the Week")
        plt.xlabel("Day of the Week: 0=Monday 6=Sunday")
        plt.show()

    # fare amount
    def fare_amount(df):
        df['fare_amount'].hist(bins=500)
        plt.title("Fare Amount")
        plt.xlabel("Fare")
        plt.show()
            
    # pickup locations
    def pickup_locations(df):
        df.plot.scatter('pickup_longitude', 'pickup_latitude')
        plt.show()

    # drop off
    def drop_off(df):
        df.plot.scatter('dropoff_longitude', 'dropoff_latitude')
        plt.show()

    # Scatter Plot
    def plot_lat_lon(df, landmarks, points='Pickup'):
        plt.figure(figsize=(12,12))
        if points == 'pickup':
            plt.plot(list(df.pickup_longitude), list(df.pickup_latitude), '.', markersize=1)
        else:
            plt.plot(list(df.dropoff_longitude), list(df.dropoff_latitude), '.', markersize=1)
        
        for landmark in landmarks:
            plt.plot(landmarks[landmark][0], landmarks[landmark][1], '*', markersize=15, alpha=1, color='r')
            plt.annotate(landmark, (landmarks[landmark][0]+.005,
            landmarks[landmark][1]+.005), color='r', backgroundcolor='w')
            
        plt.title("{} Locations in NYC Illustrated".format(points))
        plt.grid(None)
        plt.xlabel('Lat')
        plt.ylabel('lon')
        plt.show()

    plot_lat_lon(df, landmarks, points='Pickup')
    plot_lat_lon(df, landmarks, points='Dropoff')

def scale_data(df):
    df_keys = pd.DataFrame(df, columns=['key', 'fare_amount'])
    df_scaled = df.drop(['fare_amount'], axis=1)
    df_scaled = df_scaled.drop(['key'], axis=1)
    
    print('starting fare amount scale')
    
    for fare in ['fare_amount']:
        df_keys = df_keys[(df_keys[fare] > 0)]
        

    # scale features
    print('scaling data')
    df_scaled = scale(df_scaled)
    df_keys = scale(df_scaled)

    # transform into pd data frame 
    # add in fare amount from prescale
    cols = df.columns.tolist()
    df_keys_cols = df_keys.columns.tolist()
    cols.remove('fare_amount')
    cols.remove('key')
    df_scaled = pd.DataFrame(df_scaled, columns=cols, index=df.index)
    df_keys = pd.DataFrame(df_keys, columns=df_keys_cols, index=df_keys.index)
    #final_data = pd.get_dummies(df_scaled)
    #df_scaled = pd.concat([df_scaled, df['fare_amount']], axis=1)
    
    return df_scaled, df_keys
    
# feature engineering    

print('loading data')
df = pd.read_csv('../../../../kaggle_data/nyc_taxi.csv', parse_dates=['pickup_datetime'], nrows=50000)

# keep data
# clean and feature engineering
df = process_data(df)
df, df_key = scale_data(df)

print(df.head(10))
# test train split
from sklearn.model_selection import train_test_split
X = df
y = df_key.drop(['key'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

# try tree
from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
predictions = dtree.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,predictions))
