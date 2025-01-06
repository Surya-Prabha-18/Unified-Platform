from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

def scrape_gfg_problems_to_json():
    base_url = "https://www.geeksforgeeks.org/explore?page=1&sortBy=submissions"
    output_file = "gfg_problems.json"

    # Set up the WebDriver
    driver = webdriver.Chrome()  # Ensure chromedriver is installed and in PATH
    driver.get(base_url)

    try:
        # Wait until the specific element is loaded (using WebDriverWait)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="scrollableDivMobile"]/div[2]/div/div[6]'))
        )

        # Locate the specific section using the provided XPath
        problem_section = driver.find_element(By.XPATH, '//*[@id="scrollableDivMobile"]/div[2]/div/div[6]')
        
        # Extract the problem links from that section
        problem_elements = problem_section.find_elements(By.TAG_NAME, 'a')  # Get all links in the section
        
        problem_data = []

        for problem in problem_elements:
            title = problem.text.strip()
            url = problem.get_attribute('href')
            if url:  # Ensure the link is not empty
                problem_data.append({"title": title, "url": url})

        # Save to JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(problem_data, f, ensure_ascii=False, indent=4)

        print(f"Scraped {len(problem_data)} problems and saved to '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_gfg_problems_to_json()
