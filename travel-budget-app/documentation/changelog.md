# Changelog

## Week 3
- project initialized
- UI: login and create user view
- sqlite database for username and password created
- adding and finding user (username and password) in database tested

## Week 4
- creating user and login in, database connected to UI (if user doesn't exist, login not allowed)
- main menu view with options: ```My trips```, ```Create new trip```, ```Log out```
- ```My trips``` view:
    - header "hello *username*!"
    - ```Create new trip``` option
    - ```Back to menu``` option
- ```Create new trip``` view:
    - "New trip" header
    - name of the trip
    - duration of the trip in days 
    - ```Save``` option

## Week 5
- database for trips created and connected to UI
- database for expenses created and connected to UI
- user's main menu:
    - ```My trips``` view:
        - user's trips displayed
        - ```Show more``` option for each trip:
            - header "Expenses of the *trip name*"
            - trip's expenses displayed (expense description, amount paid, category of the expense)
        - ```Add expense``` option
            - header "Add an expense"
            - inputs: description of the expense, amount paid, category (select from option menu)
            - ```Save``` option saves the expense to the trip
            - ```Cancel``` option
        - ```Trip statistics``` option
            - Statistics of the trip displayed
        - ```Back to trips menu``` option
    - ```Create new trip``` view:
        - ```Cancel``` option added (leads back to user's main menu)
    - ```User statistics``` view added to user's main menu
        - General statistics of the user displayed

## Week 6
Further development in user statistics. *No trips yet* displayed under 'user's trips' if user did not add any trips yet, or *No expenses yet* displayed under 'trip's expenses' if user did not add any expenses to the particular trip yet. Errors (such as empty input or non-numerical value for input of travel days or cost of the expense) are now handled (file ```errors_handling.py``` in the folder ```errors```)
