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

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import traceback

# def scrape_difficulty_and_topics(problem_url):
#     try:
#         # Setup the webdriver (using Chrome in this example)
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         driver.get(problem_url)

#         # Wait for the topics section container to load (increase wait time if necessary)
#         wait = WebDriverWait(driver, 20)  # increased wait time to 20 seconds
#         topics_section = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="scrollableDiv"]/div/div[1]/div[6]/div[2]')))
        
#         # Extract all topics which are inside <a> tags
#         topics = [topic.text for topic in topics_section.find_elements(By.TAG_NAME, 'a')]

#         # Wait for the difficulty section to load
#         difficulty_elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="scrollableDiv"]/div/div[1]/div[2]/span[1]')))
        
#         # Extract difficulty level
#         difficulty = difficulty_elem.text

#         # Print results
#         print(f"Problem URL: {problem_url}")
#         print(f"Difficulty: {difficulty}")
#         print(f"Topics: {', '.join(topics)}")

#         driver.quit()

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         print("Error traceback:", traceback.format_exc())
#         driver.quit()

# # Example usage
# scrape_difficulty_and_topics("https://www.geeksforgeeks.org/problems/find-the-number-of-islands/0")
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def get_problem_topics(url, xpath):
#     # Set up ChromeDriver service
#     service = Service(r'C:\chromedriver\chromedriver-win64\chromedriver.exe')
#     options = webdriver.ChromeOptions()
#     options.add_argument('--ignore-certificate-errors')  # Optional: Ignore SSL errors
#     driver = webdriver.Chrome(service=service, options=options)

#     try:
#         # Open the problem link
#         driver.get(url)

#         # Wait for the topics section to load
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

#         # Find the topics element
#         topics_element = driver.find_element(By.XPATH, xpath)

#         # Extract and return the text content
#         return topics_element.text.split("\n")
#     finally:
#         driver.quit()

# # Inputs
# problem_link = "https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&sortBy=submissions"
# xpath_to_topics = '//*[@id="scrollableDiv"]/div/div[1]/div[6]/div[2]/div[3]/div'

# # Fetch topics
# topics = get_problem_topics(problem_link, xpath_to_topics)
# print("Topics:", topics)


# # ---------------------company tags------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def get_problem_topics(url, xpath):
#     # Set up ChromeDriver service
#     service = Service(r'C:\chromedriver\chromedriver-win64\chromedriver.exe')
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(service=service, options=options)

#     try:
#         # Open the problem link
#         driver.get(url)

#         # Wait for the topics section to load
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

#         # Find all <a> elements within the topics section
#         topic_elements = driver.find_elements(By.XPATH, xpath)

#         # Extract and return the text content from each <a> element
#         topics = [topic.text for topic in topic_elements]
#         return topics
#     finally:
#         driver.quit()

# # Inputs
# problem_link = "https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&sortBy=submissions"
# xpath_to_topics = '//div[@class="ui labels"]/a'

# # Fetch topics
# topics = get_problem_topics(problem_link, xpath_to_topics)
# print("Topics:", topics)
# # ---------------------company tags------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_problem_topics(url, xpath):
    # Set up ChromeDriver service
    service = Service(r'C:\chromedriver\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Open the problem link
        driver.get(url)

        # Wait for the topics section to load (increase wait time)
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

        # Print inner HTML for debugging
        element = driver.find_element(By.XPATH, '//*[@id="scrollableDiv"]/div/div[1]/div[6]/div[2]/div[3]/div')
        print(element.get_attribute('innerHTML'))

        # Find all <a> elements within the topics section
        topic_elements = driver.find_elements(By.XPATH, xpath)

        # Extract and return the text content from each <a> element
        topics = [topic.text for topic in topic_elements if topic.text.strip()]
        return topics
    finally:
        driver.quit()

# Inputs
problem_link = "https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&sortBy=submissions"
xpath_to_topics = '//*[@id="scrollableDiv"]/div/div[1]/div[6]/div[2]/div[3]/div//a'

# Fetch topics
topics = get_problem_topics(problem_link, xpath_to_topics)
print("Topics:", topics)
