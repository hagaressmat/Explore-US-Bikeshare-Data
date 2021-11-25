import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("please enter the city")
    city = input("chicago or new york city or washington: ")
    city = city.lower()
    while True:
        if city not in ('chicago', 'washington', 'new york city', 'new york'):
            print("please enter the city again")
            city = input("chicago or new york city or washington: ")
            continue
        else:
            break



    # get user input for month (all, january, february, ... , june)
    print("please enter month name or all 'for all months'")
    print("month list is January, February, March, April, May, June ")
    month = input("month name or all: ")
    month = month.capitalize()
    while month  not in ('January', 'February', 'March', 'April', 'May', 'June','All'):
        print("please enter the month again")
        month = input("month name or all: ")
        



    # get user input for day of week (all, monday, tuesday, ... sunday)
    print("please enter month name or all 'for all days'")
    print("days list is Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday")
    day = input("day name or all: ")
    day = day.capitalize()
    while day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',"All"):
        print("please enter the day again")
        day = input("day name or all: ")


    print('-'*40)
    return city, month, day


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
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print("most common month : ",most_common_month)

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_day = df['day_of_week'].mode()[0]
    print("most common day of week : ",most_common_day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("most common start hour : ",most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_Station = df['Start Station'].value_counts().max()
    print("most commonly used start station : ",popular_start_Station)


    # display most commonly used end station
    popular_end_Station = df['End Station'].value_counts().max()
    print("most commonly used end station : ",popular_end_Station)


    # display most frequent combination of start station and end station trip
    popular_trip = matches.groupby(["Start Station", "End Station"]).count().max(level=0)
    print("most popular trip : ",popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print("total travel time is : " , total_travel_time)


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time is : " , mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\ncounts of user types:\n', user_types)

    # Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\ncounts of gender:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available.")
    # Display earliest, most recent, and most common year of birth
    
    try:
      earliest_year_of_birth = df['Birth Year'].min()
      print('\nearliest year of birth:\n', earliest_year_of_birth)
    except KeyError:
      print("\nearliest year of birth:\nNo data available.")
      
    try:
      most_recent_year_of_birth = df['Birth Year'].max()
      print('\nmost recent year of birth:\n', most_recent_year_of_birth)
    except KeyError:
      print("\nmost recent year of birth:\nNo data available.")


    try:
      year_of_birth = df['Birth Year'].value_counts().max()
      print('\nmost common year of birth:\n', year_of_birth)
    except KeyError:
      print("\nmost common year of birth:\nNo data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
        start_loc = 0
        while view_data.lower() is "yes":
            print(df.iloc[start_loc:(start_loc+5)])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
            if view_data.lower() != 'yes':
                  break


if __name__ == "__main__":
	main()
