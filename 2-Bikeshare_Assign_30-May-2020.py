# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:54:33 2020

@author: soha.ali
"""


import time
import datetime
import pandas as pd
import statistics as st
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! This is Soha Let\'s have some fun and explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()

    while(True):
        if(city == 'chicago' or city == 'new york' or city == 'washington' or city == 'all'):
            break
        else:
            city = input('Enter Correct city: ').lower()
            
    # get user input for month (all, january, february, ... , june)
    month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()
     #lower is used to get input in any format

    while(True):
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
            break
        else:
            month = input('Enter valid month\n').lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day =  input('Which day ? monday, tuesday, wednesday, thursday, friday, saturday , sunday or all to display data of all days?\n').lower()
   
    while(True):
        
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
            break
        else:
            day = input('Enter Correct day: ').lower()
            
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

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

print load_data

def common_month(df):
    df['month'] = df['Start Time'].dt.month_name()
    popular_month=df['month'].mode()[0]
    print('Most Popular Start Month:',popular_month)
    
#definition of most common day function
def common_day(df):
    df['day'] = df['Start Time'].dt.day_name()
    popular_day=df['day'].mode()[0]
    print('Most Popular Day:',popular_day)
    
#definition of most common start hour function
def common_start_hour(df):
    df['hour'] = df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('Most Popular Start Hour:',popular_hour)
    
#definition of most frequent times of travel function
def time_stats(df, month, day):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if(month=='all' and day=='all'):
        # display the most common month
        common_month(df)
        # display the most common day of week
        common_day(df)
        # display the most common start hour
        common_start_hour(df)
    elif(month!='all' and day=='all'):
        # display the most common day of week
        common_day(df)
        # display the most common start hour
        common_start_hour(df)
    elif(month=='all' and day!='all'):
        # display the most common start hour
        common_start_hour(df)
        # display the most common month
        common_month(df)
    elif(month!='all'and day!='all'):
        common_start_hour(df)
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

     # display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('Most Popular Start Station:',popular_start_station)
    
    # display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('Most Popular End Station:',popular_end_station)
    
    # display most frequent combination of start station and end station trip
    combination_trip = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    most_frequent_trip = combination_trip.value_counts().idxmax()
    print('\nMost popular trip is from {}\n'.format(most_frequent_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total Travel Time:',total_travel_time)


    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean Travel Time:',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    no_of_subscribers = df['User Type'].str.count('Subscriber').sum()
    no_of_customers = df['User Type'].str.count('Customer').sum()
    print('\nNumber of subscribers are {}\n'.format(int(no_of_subscribers)))
    print('\nNumber of customers are {}\n'.format(int(no_of_customers)))

    # Display counts of gender
    if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('\nNumber of male users are {}\n'.format(int(male_count)))
        print('\nNumber of female users are {}\n'.format(int(female_count)))


    # Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        most_common_birth_year = st.mode(df['Birth Year'])
        print('\n Oldest Birth Year is {}\n Youngest Birth Year is {}\n Most popular Birth Year is {}\n'.format(int(earliest_year), int(recent_year), int(most_common_birth_year)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    count=0
    end=5
    while True:
        
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: \n')
        if answer.lower() == 'yes':
            print(df.iloc[count:end])
            count+=5
            end+=5
       
        elif  answer.lower() == 'no':
            break                
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

## assignement number two
if __name__ == "__main__":
	main()

    
