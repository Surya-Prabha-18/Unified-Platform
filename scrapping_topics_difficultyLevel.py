# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def scrape_difficulty_and_topics(problem_url):
#     try:
#         # Setup the webdriver (using Chrome in this example)
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         driver.get(problem_url)

#         # Wait for the difficulty section and topics section to be visible
#         wait = WebDriverWait(driver, 10)  # waits for up to 10 seconds
#         difficulty_elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="scrollableDiv"]/div/div[1]/div[2]/span[1]')))
        
#         # Ensure we're targeting the right XPath for topics
#         topics_section = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="scrollableDiv"]/div/div[1]/div[6]/div[2]')))

#         # Extract difficulty level
#         difficulty = difficulty_elem.text

#         # Extract topics using the <a> tags inside the topics section
#         topics = [topic.text for topic in topics_section.find_elements(By.TAG_NAME, 'a') if topic.text.strip() != '']

#         # Print results
#         print(f"Problem URL: {problem_url}")
#         print(f"Difficulty: {difficulty}")
#         print(f"Topics: {', '.join(topics)}" if topics else "No topics available.")

#         driver.quit()

#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# scrape_difficulty_and_topics("https://www.geeksforgeeks.org/problems/find-the-number-of-islands/0")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

def scrape_difficulty_and_topics(problem_url):
    try:
        # Setup the webdriver (using Chrome in this example)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(problem_url)

        # Wait for the topics section container to load (increase wait time if necessary)
        wait = WebDriverWait(driver, 20)  # increased wait time to 20 seconds
        topics_section = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="scrollableDiv"]/div/div[1]/div[6]/div[2]')))
        
        # Extract all topics which are inside <a> tags
        topics = [topic.text for topic in topics_section.find_elements(By.TAG_NAME, 'a')]

        # Wait for the difficulty section to load
        difficulty_elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="scrollableDiv"]/div/div[1]/div[2]/span[1]')))
        
        # Extract difficulty level
        difficulty = difficulty_elem.text

        # Print results
        print(f"Problem URL: {problem_url}")
        print(f"Difficulty: {difficulty}")
        print(f"Topics: {', '.join(topics)}")

        driver.quit()

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Error traceback:", traceback.format_exc())
        driver.quit()

# Example usage
scrape_difficulty_and_topics("https://www.geeksforgeeks.org/problems/find-the-number-of-islands/0")
