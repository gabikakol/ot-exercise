# Specification

## Purpose
The purpose of the app is to track the spendings while traveling, divide them into cathegories, and see the statistics (total, per day, per cathegory, the cheapest and the most expensive) of both current and past trips. 

## Users
The program is used by one user at the time. Each user has an unique username and a non-empty password. Users do not interact with other users. Each user has its own trips with statistics. 

## User interface
<img src="UI-plan.jpg"> 

## Functionality

### Before login
- New user:
    - creates an unique username
    - created a valid password
- Existing user:
    - logs in using the previosuly created username and the corresponding password
    - system informs if the username is not found or the password is incorrect

### After login
User chooses one of 3 functionalities:
1. My trips
    - redirects to the "My trips" menu 
3. Add new trip
    - redirects to the "New trip" window
5. Sign out
    - back to login menu 

### Creating new trip
User is asked to input:
- name of the trip
- duration (in days)
- location (optional)
- picture (optional)

### Viewing a trip
- list of expenses displayed
- for each expense:
    - name of expense
    - cost
    - cathegory

### Adding an expense
User is asked to input:
- name/description
- cathegory (choose from: groceries, transportation, accommodation, restaurants, bars, cafes, shopping, activities, entertainment, currency exchange comissions, laundry, other)
- amount (costs in EUR)

### Statistics of a trip
- spent in total
- spent per day (in average)
- spent each day (display in a table)
- spent per cathegory
- cheapest and the most expensive item/expense
- cheapest and the most expensive days 
- cheapest and the most expensive cathegory

## Further development
- users interact with each other, for example splitting the costs 
- expense and trip deletion
- user deletion
- currency exchange calculator
