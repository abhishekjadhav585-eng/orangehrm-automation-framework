# Test Automation Framework

##  Project Description
- This project is a Selenium-based test automation framework developed using Python and PyTest.  
- It automates major functionalities of a web-based employee management system such as login, employee creation, search, deletion, and logout.

##  Tools & Technologies Used
- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- WebDriverWait & Expected Conditions

##  Features Automated
- Valid Login
- Add Employee
- Delete employee
- Search Employee
- Employee list

##  Project Structure
tests/  Contains all test cases
pages/  Page Object Model files 
drivers/  Driver setup and browser configuration
utilities/  Logger and reusable utilities
logs/  Execution log files
conftest.py - PyTest fixture for driver setup
pytest.ini - PyTest configuration file
requirements.txt - Required libraries

##   How to Run Tests
1. Open the project folder in Visual Studio Code
2. Install required libraries
   pip install -r requirements.txt

3. Run all test cases
   pytest -v

4. Run a specific test file
   pytest tests/test_login.py -v      
