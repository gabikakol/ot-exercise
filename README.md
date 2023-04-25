Software development course (Ohjelmistotekniikka), spring 2023, University of Helsinki <br/>
https://ohjelmistotekniikka-hy.github.io/

# Travel budget app
Application allows you to track your travel expenses and view statistics. 

## Documentation
- [user manual](travel-budget-app/documentation/user_manual.md)
- [specification](travel-budget-app/documentation/specification.md)
- [architecture](travel-budget-app/documentation/architecture.md)
- [testing](travel-budget-app/documentation/testing.md)
- [changelog](travel-budget-app/documentation/changelog.md)
- [time accounting](travel-budget-app/documentation/time-accounting.md)

## Command line functions
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
poetry run coverage-report
```
### Pylint
Pylint analysis can be viewed with the command: 
```
poetry run invoke lints
```
### Formatting
Code can be formatted using autopep8 with the command: 
```
poetry run invoke format
```
