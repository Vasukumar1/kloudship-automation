#I am using python and selenium as it is more easy to implement 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

# Set up the driver i am using chrome
driver = webdriver.Chrome()

# Application credentials
url = "https://ecspro-qa.kloudship.com"
username = "kloudship.qa.automation@mailinator.com"
password = "Password1"

# Test Case 01: Add Package
def add_package():
    driver.get(url)
    
    # Step 1: Login to the application
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    
    time.sleep(2)  # Wait for the page to load
    
    # Step 2: Navigate to "Package Types"
    driver.find_element(By.LINK_TEXT, "Package Types").click()
    
    time.sleep(2)
    
    # Step 3: Click on "Add Manually"
    driver.find_element(By.ID, "add-manually").click()
    
    # Step 4: Fill in package details
    driver.find_element(By.ID, "package-name").send_keys("FirstName_LastName")
    random_dimension = random.randint(1, 20)  # Random dimension less than 20
    driver.find_element(By.ID, "package-dimension").send_keys(str(random_dimension))
    
    # Step 5: Save the package
    driver.find_element(By.ID, "save-button").click()
    
    time.sleep(2)  # Wait for save to complete
    
    # Step 6: Logout
    driver.find_element(By.ID, "logout-button").click()
    
    time.sleep(2)

# Test Case 02: Delete Package
def delete_package():
    driver.get(url)
    
    # Step 1: Login to the application
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    
    time.sleep(2)
    
    # Step 2: Navigate to "Package Types"
    driver.find_element(By.LINK_TEXT, "Package Types").click()
    
    time.sleep(2)
    
    # Step 3: Find and delete the package added in Test Case 01
    # Assuming the newly added package has a specific name, such as "FirstName_LastName"
    package_row = driver.find_element(By.XPATH, "//tr[td[text()='FirstName_LastName']]")
    delete_button = package_row.find_element(By.CLASS_NAME, "delete-button")
    delete_button.click()

    # Step 4: Logout
    driver.find_element(By.ID, "logout-button").click()
    
    time.sleep(2)

def main():
    try:
        # Execute Test Case 01 (Add Package)
        add_package()
        
        # Re-login to verify the added package (Test Case 01)
        driver.get(url)
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Package Types").click()
        time.sleep(2)
        
        # Verify the package exists (after Test Case 01)
        package_exists = len(driver.find_elements(By.XPATH, "//tr[td[text()='FirstName_LastName']]")) > 0
        assert package_exists, "Package was not added successfully."
        
        # Execute Test Case 02 (Delete Package)
        delete_package()
        
        # Re-login to verify the package is deleted (Test Case 02)
        driver.get(url)
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Package Types").click()
        time.sleep(2)
        
        # Verify the package is deleted (after Test Case 02)
        package_exists_after_delete = len(driver.find_elements(By.XPATH, "//tr[td[text()='FirstName_LastName']]")) == 0
        assert package_exists_after_delete, "Package was not deleted successfully."
    
    finally:
        # Quit the browser after execution
        driver.quit()

# Run the automation script
if __name__ == "__main__":
    main()
