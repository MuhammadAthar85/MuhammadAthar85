import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run_sanity_test(base_url: str):
    """Example sanity test using Selenium WebDriver.

    This test logs in, performs a payment, and verifies the confirmation.
    Replace element locators and flows with those specific to your app.
    """
    driver = webdriver.Firefox()
    driver.get(base_url)

    try:
        # Login flow (update IDs for your application)
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("password")
        driver.find_element(By.ID, "login").click()

        # Wait for dashboard/homepage after login
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # Payment flow
        driver.find_element(By.ID, "pay_button").click()
        driver.find_element(By.ID, "amount").send_keys("10")
        driver.find_element(By.ID, "submit_payment").click()

        # Check for confirmation
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "payment-confirmation"))
        )
        print("Payment flow succeeded")

    finally:
        time.sleep(1)
        driver.quit()


if __name__ == "__main__":
    run_sanity_test("https://example.com")
