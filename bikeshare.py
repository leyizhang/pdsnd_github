import numpy as np
import pandas as pd
import time
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# get user input for month (all, january, february, ... , june)
MONTHS = ("all", "january", "february", "march" , "april", "may", "june")
# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
CITIES = ('chicago', 'new york city', 'washington')
# get user input for day of week (all, monday, tuesday, ... sunday)
DAYS_OF_WEEK = ("all", "monday", "tuesday", "wednesday" , "thursday", "friday", "saturday", "sunday")

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        try:
            city = str(input(
            """Please Enter a city from following cities:
            chicago
            new york city
            washington: """)).lower()
            if city in CITIES:
                break
            else:
                print("""ERROR: Please only enter one city from:
                chicago
                new york city
                washington: """)
        except KeyboardInterrupt:
            break


    while True:
        try:
            month = str(input("""Please Enter a month (all, january, february, ... , june): """)).lower()
            if month in MONTHS:
                break
            else:
                print("ERROR, Please enter one month from (all, january, february, ... , june): ")
        except KeyboardInterrupt:
            break

    while True:
        try:
            day = str(input("""Please Enter day of week (all, monday, tuesday, ... , sunday): """)).lower()
            if day in DAYS_OF_WEEK:
                break
            else:
                print("ERROR, Please enter one day from (all, monday, tuesday, ... , sunday): ")
        except KeyboardInterrupt:
            break

    print('-'*40)
    return city, month, day

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('most common month: {}'.format(df['month'].value_counts().idxmax()))

    # display the most common day of week
    print('most common day of week: {}'.format(df['day_of_week'].value_counts().idxmax()))

    # display the most common start hour
    print('most common start hour: {}'.format(df['hour'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('most commonly used start station: {}'.format(df['Start Station'].value_counts().idxmax()))

    # display most commonly used end station
    print('most commonly used end station: {}'.format(df['End Station'].value_counts().idxmax()))

    # display most frequent combination of start station and end station trip
    print('most frequent combination of start station and end station: {} & {}'\
          .format(df[['Start Station','End Station']].mode()['Start Station'][0],df[['Start Station','End Station']].mode()['End Station'][0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("total travel time (in seconds): {}".format(total_time))

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("average travel time (in seconds): {}".format(mean_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("counts of user types: ")
    for i in range(0,len(user_types)):
        print("{}: {}".format(user_types.index[i],
                              user_types.data[i]))

    # Display counts of gender
    if "Gender" in df.columns:
        user_gender = df['Gender'].value_counts()
        print("counts of user gender: ")
        for i in range(0,len(user_gender)):
            print("{}: {}".format(user_gender.index[i],
                              user_gender.data[i]))
    else:
        print("\n There is no gender informaiton in this dataset!")

    # Display earliest, most recent, and most common year of birth

    if "Birth Year" in df.columns:
        user_birth_earliest = int(df['Birth Year'].min())
        user_birth_most_recent = int(df['Birth Year'].max())
        user_birth_common = int(df['Birth Year'].mode())

        print("The earliest year of birth: {}".format(user_birth_earliest))
        print("The most recent year of birth: {}".format(user_birth_most_recent))
        print("The most common year of birth: {}".format(user_birth_common))
    else:
        print("\n There is no year of birth informaiton in this dataset!")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    #seperate the raw data as every 5 lines:
    
    for i in range(0, len(df), 5):        
        show_raw_data = input("\nWould you like to reivew 5 lines of raw data for the dateset?\
                              \nPlease Enter 'yes'/'no' ").lower()
        if show_raw_data != 'yes':
            break
        print(df.iloc[i: i + 5])
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
