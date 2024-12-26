from bs4 import BeautifulSoup
import requests

# URL of the problem page
url = "https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1"

# Make a GET request to fetch the raw HTML content
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the problem title
    title = soup.select_one("div.problem-header-title").get_text(strip=True)
    
    # Extract the problem description
    description = soup.select_one("div.problem-body").get_text(strip=True)
    
    # Extract the constraints (if present)
    constraints = soup.select_one("div.constraints").get_text(strip=True) if soup.select_one("div.constraints") else "No constraints found"
    
    # Extract the difficulty (if available)
    difficulty = soup.select_one("div.difficulty-level span").get_text(strip=True) if soup.select_one("div.difficulty-level span") else "Difficulty not found"
    
    # Print the extracted details
    print("Title:", title)
    print("Description:", description[:500], "...")  # Limiting output for long descriptions
    print("Constraints:", constraints)
    print("Difficulty:", difficulty)
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed and in PATH

# Open the problem page
url = "https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1"
driver.get(url)

try:
    # Wait until the problem title is visible
    title_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.problem-header-title"))
    )
    
    # Extract the problem title
    title = title_element.text
    
    # Extract the problem description
    description = driver.find_element(By.CSS_SELECTOR, "div.problem-body").text
    
    # Extract the constraints
    try:
        constraints = driver.find_element(By.CSS_SELECTOR, "div.constraints").text
    except:
        constraints = "No constraints found"
    
    # Extract the difficulty
    try:
        difficulty = driver.find_element(By.CSS_SELECTOR, "div.difficulty-level span").text
    except:
        difficulty = "Difficulty not found"
    
    # Print the extracted details
    print("Title:", title)
    print("Description:", description[:500], "...")  # Limiting output for long descriptions
    print("Constraints:", constraints)
    print("Difficulty:", difficulty)
finally:
    # Close the browser
    driver.quit()
