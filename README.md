Software development course (Ohjelmistotekniikka), spring 2023, University of Helsinki <br/>
https://ohjelmistotekniikka-hy.github.io/

# Travel budget app
Application allows you to track your travel expenses and view statistics. 

## Documentation
- [user manual](travel-budget-app/documentation/user-manual.md)
- [specification](travel-budget-app/documentation/specification.md)
- [architecture](travel-budget-app/documentation/architecture.md)
- [testing](travel-budget-app/documentation/testing.md)
- [changelog](travel-budget-app/documentation/changelog.md)
- [time accounting](travel-budget-app/documentation/time-accounting.md)

## Instalation of the Program
Run the following commands in ```/software-dev-exercises/travel-budget-app```
1. Install dependencies with the command:
```
poetry install
```
2. Initialize the project with the command:
```
poetry run invoke build
```
3. Start the program with the command:
```
poetry run invoke start
```
For further instructions, please read [user manual](travel-budget-app/documentation/user-manual.md).

## Command line functions
The following commands must be ran in ```/software-dev-exercises/travel-budget-app```

### Program initialization
The application is first initialized with the following command:
```
poetry run invoke build
```

### Program execution
The application is executed with the command:
```
poetry run invoke start
```
### Testing
Tests are executed with the command:
```
poetry run invoke test
```
### Test coverage
Test coverage is generated with the command:
```
poetry run invoke coverage-report
```
### Pylint
Pylint analysis can be viewed with the command: 
```
poetry run invoke lint
```
### Formatting
Code can be formatted using autopep8 with the command: 
```
poetry run invoke format
```
