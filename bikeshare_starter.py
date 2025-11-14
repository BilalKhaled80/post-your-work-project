import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'post-your-work-project\chicago.csv',
              'new york city': 'post-your-work-project\new_york_city.csv',
              'washington': 'post-your-work-project\washington.csv' }

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
    while True:
        city = input("Pls choose a city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input")

    # get user input for month (all, january, february, ... , june)
    months = [all, 'january', 'febraury', 'march', 'april', 'may', 'june']
    while True:
        month = input("Pls choose a month: ").lower()
        if month in months:
            break
        else:
            print("Invalid input")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = [all, 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Pls choose a day: ").lower()
        if day in days:
            break
        else:
            print("Invalid input")

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
    df = pd.read_csv(CITY_DATA[city])
    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month and day of week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    
    # Filter by month
    if month != all:
        months = ['january', 'febraury', 'march', 'april', 'may', 'june']
        month_index = months.index(month) + 1
        df = df[df['month'] == month_index]
    
    # Filter by day
    if day != all:
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month:" , popular_month)

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("Most common day_of_week:" , popular_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common hour:" , popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station:" , popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station:" , popular_end_station)

    # display most frequent combination of start station and end station trip
    combi_trip = (df['Start Station'] + " -> " + df['End Station']).mode()[0]
    print("Most Frequent Combination:" , combi_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time:" , total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time:" , mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("Gender is not available")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Birth Year Stats:")
        print(f"Earliest: {int(df['Birth Year'].min())}")
        print(f"Most recent: {int(df['Birth Year'].max())}")
        print(f"Most common: {int(df['Birth Year'].mode()[0])}")
    else:
        print("\nBirth Year data not available.")

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


if __name__ == "__main__":
	main()
