# Specification

## Purpose
The purpose of the app is to track the spendings while traveling, divide them into cathegories, and see the statistics (total, per day, per cathegory, the cheapest and the most expensive) of both current and past trips. 

## Users
The program is used by one user at the time. Each user has an unique username and a non-empty password. Users do not interact with other users. Each user has its own trips with statistics. 

## User interface plan
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

### Viewing a trip

### Adding an expense

### Statistics of a trip

## Further development
- users interact with each other, for example splitting the costs 
- expense and trip deletion
- user deletion
