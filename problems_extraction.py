from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up WebDriver
driver_path = r"C:\chromedriver\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Maximize the browser window
driver.maximize_window()

# URL to scrape
base_url = "https://www.geeksforgeeks.org/explore?page=11&sortBy=submissions"
driver.get(base_url)

try:
    # Wait for the problem container to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="scrollableDiv"]/div/div'))
    )
    print("Page loaded successfully!")

    # Extract the first two problems
    problem_containers = driver.find_elements(By.XPATH, '//*[@id="scrollableDivMobile"]/div[2]/div/div[6]/div/div')[:2]

    problems = []
    for container in problem_containers:
        try:
            # Extract problem title using the XPath you provided
            title = container.find_element(By.XPATH, '//*[@id="scrollableDiv"]/div/div[1]/div[1]/div/h3').text.strip()

            # Extract problem description using the XPath you provided
            description = container.find_element(By.XPATH, '//*[@id="scrollableDiv"]/div/div[1]/div[4]/div/p[1]/span').text.strip()

            # Extract difficulty using the XPath you provided
            difficulty = container.find_element(By.XPATH, '//*[@id="scrollableDiv"]/div/div[1]/div[2]/span[1]').text.strip()

            # Extract tags using the XPath you provided
            tags_element = container.find_element(By.XPATH, '//*[@id="scrollableDiv"]/div/div[1]/div[6]/div[2] ')
            tags = [tag.text.strip() for tag in tags_element.find_elements(By.TAG_NAME, 'a')]

            # Append to problems list
            problems.append({
                "title": title,
                "description": description,
                "difficulty": difficulty,
                "tags": tags,
            })
        except Exception as e:
            print(f"Error extracting problem: {e}")

    # Print the extracted problems
    for i, problem in enumerate(problems, 1):
        print(f"Problem {i}:")
        print(f"Title: {problem['title']}")
        print(f"Description: {problem['description']}")
        print(f"Difficulty: {problem['difficulty']}")
        print(f"Tags: {', '.join(problem['tags'])}")
        print("-" * 50)
finally:
    # Close the browser
    driver.quit()
