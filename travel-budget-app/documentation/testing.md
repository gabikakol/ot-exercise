# Testing
The application has been tested with automated unit and integration tests using unittest and with manually performed system level tests. 

## Unit and integration testing

### Application logic
Each class of the application logic is tested with its own test classes.</br>
The classes that require permanents storage run on dummy databases, which are initialized in the same way as the application's databases, but with their own files, in */tests/testing_env* forlder. </br>
The dummy files contaian the configuration of the file names, initialization of database *test_database.sqlite*, initialization of connections, and creation of test repositories. The file names can be configures in the *.env.test* file. 

### Repository classes
Repository classes `UserRepository`, `TripRepository`, and `ExpenseRepository` are also tested with the dummy files from */tests/testing_env* forlder. Each repository class has its own test class. 

### Testing coverage
Tests exclude the user interface layer. The branching coverage of the application testing in 100%. </br> </br>
<img src="pictures/coverage-report.png"> 

## System testing
System testing of the application has been performed manually. 

### Installation and configuration
The application has been downloaded and tested as described in the [user manual](user-manual.md) for the Linux environment. 

### Functionalities

## Issues left in the application
