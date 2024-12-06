**Automation Code Using Python and Selenium**
step 1 :Install Required Packages: First, you need to install Selenium and WebDriver( I am using google chrome in this case):
Step 2 :Automation code. I have provided this code automation.py
Explanation of Code:
Login: Uses the provided credentials to log into the application.
Test Case 1 (Add Package): Navigates to "Package Types" and adds a new package with random dimensions.
Test Case 2 (Delete Package): Locates the package added in Test Case 1 and deletes it.
Assertions: After Test Case 01 and Test Case 02, it checks whether the package was added and deleted correctly by verifying the presence or absence of the package on the page.
How to Run the Code:
Install Selenium using pip install selenium.
Download the appropriate WebDriver for your browser (e.g. chrome)
Save the code to a Python file
Run the script by executing above file
This script will automate both the "Add Package" and "Delete Package" test cases, and it will verify the results as expected.
