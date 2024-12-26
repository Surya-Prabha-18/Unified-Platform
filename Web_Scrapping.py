import requests
from bs4 import BeautifulSoup

def scrape_gfg_problems(profile_url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Fetch the page
        response = requests.get(profile_url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Locate solved problems section
            solved_problem_section = soup.find('div', class_='solvedProblemContainer_head__ZyIn0')
            
            if not solved_problem_section:
                print("Solved problem section not found.")
                return
            
            # Extract problem links
            problems = solved_problem_section.find_all('a')
            
            print(f"Solved Problems ({len(problems)}):")
            for problem in problems:
                title = problem.text.strip()
                link = problem['href']
                print(f"{title}: {link}")
        else:
            print(f"Failed to fetch data from {profile_url}. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
scrape_gfg_problems("https://www.geeksforgeeks.org/user/suryapraq1ec/")



























# import requests
# from bs4 import BeautifulSoup
# import openpyxl
# # print("succesfull")
# try:
#     response = requests.get("https://www.geeksforgeeks.org/user/suryapraq1ec/")
#     soup = BeautifulSoup(response.text,'html.parser')
#     print(soup)

# except Exception as e:
#     print(e)
# import requests
# from bs4 import BeautifulSoup

# def scrape_gfg_problems(username):
#     try:
#         # GFG user profile URL
#         url = f"https://www.geeksforgeeks.org/user/bhaviyamb3n9w/?ref=header_profile"
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#         }

#         # Fetch the page
#         response = requests.get(url, headers=headers)
        
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
            
#             # Use the CSS selector you provided to locate the section with solved problems
#             solved_problem_section = soup.select_one(
#                 "#comp > div.AuthLayout_outer_div__20rxz > div > div.AuthLayout_head_content__ql3r2 > div > div > div.solvedProblemContainer_head__ZyIn0 > div.solvedProblemSection_head__VEUg4"
#             )
            
#             # Check if the section exists
#             if solved_problem_section:
#                 # Extract the text or links to the solved problems
#                 problems = solved_problem_section.find_all('a')
                
#                 # Print problem titles
#                 print(f"Problems solved by {username}:")
#                 for problem in problems:
#                     title = problem.text.strip()  # Get the text of the problem
#                     print(title)
#             else:
#                 print("Solved problem section not found.")
#         else:
#             print(f"Failed to fetch data for {username}. Status code: {response.status_code}")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# Example usage
# scrape_gfg_problems("suryapraq1ec")
# import requests
# from bs4 import BeautifulSoup

# def scrape_gfg_problems(username):
#     try:
#         # GFG user profile URL
#         url = f"https://www.geeksforgeeks.org/user/sashan6mj1/"
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#         }

#         # Fetch the page
#         response = requests.get(url, headers=headers)
        
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
            
#             # Use the CSS selector to locate the section with solved problems
#             solved_problem_section = soup.select_one(
#                 "#comp > div.AuthLayout_outer_div__20rxz > div > div.AuthLayout_head_content__ql3r2 > div > div > div.solvedProblemContainer_head__ZyIn0 > div.solvedProblemSection_head__VEUg4"
#             )
            
#             # Check if the section exists
#             if solved_problem_section:
#                 # Extract all problem links (assuming problems are listed as <a> tags)
#                 problems = solved_problem_section.find_all('a')
                
#                 # Initialize lists to store different difficulties
#                 school_problems = []
#                 easy_problems = []
#                 medium_problems = []
#                 hard_problems = []
                
#                 # Iterate over each problem
#                 for problem in problems:
#                     title = problem.text.strip()  # Get the text of the problem
#                     link = problem['href']  # Get the link to the problem
                    
#                     # Find difficulty level using the new provided selectors
#                     school_difficulty_section = soup.select_one(
#                         "#comp > div.AuthLayout_outer_div__20rxz > div > div.AuthLayout_head_content__ql3r2 > div > div > div.solvedProblemContainer_head__ZyIn0 > div.solvedProblemSection_head__VEUg4 > div.problemNavbar_head__cKSRi > div:nth-child(1)"
#                     )
                    
#                     easy_difficulty_section = soup.select_one(
#                         "#comp > div.AuthLayout_outer_div__20rxz > div > div.AuthLayout_head_content__ql3r2 > div > div > div.solvedProblemContainer_head__ZyIn0 > div.solvedProblemSection_head__VEUg4 > div.problemNavbar_head__cKSRi > div:nth-child(2)"
#                     )
                    
#                     medium_difficulty_section = soup.select_one(
#                         "#comp > div.AuthLayout_outer_div__20rxz > div > div.AuthLayout_head_content__ql3r2 > div > div > div.solvedProblemContainer_head__ZyIn0 > div.solvedProblemSection_head__VEUg4 > div.problemNavbar_head__cKSRi > div:nth-child(3)"
#                     )
                    
#                     hard_difficulty_section = soup.select_one(
#                         "#comp > div.AuthLayout_outer_div__20rxz > div > div.AuthLayout_head_content__ql3r2 > div > div > div.solvedProblemContainer_head__ZyIn0 > div.solvedProblemSection_head__VEUg4 > div.problemNavbar_head__cKSRi > div:nth-child(5)"
#                     )
                    
#                     # Classify problems based on the available difficulty sections
#                     if school_difficulty_section:
#                         school_problems.append(f"{title}: {link}")
#                     elif easy_difficulty_section:
#                         easy_problems.append(f"{title}: {link}")
#                     elif medium_difficulty_section:
#                         medium_problems.append(f"{title}: {link}")
#                     elif hard_difficulty_section:
#                         hard_problems.append(f"{title}: {link}")
#                     else:
#                         print(f"Difficulty info not found for: {title}")
                
#                 # Print categorized problems
#                 print(f"School Problems ({len(school_problems)}):")
#                 for problem in school_problems:
#                     print(problem)

#                 print(f"\nEasy Problems ({len(easy_problems)}):")
#                 for problem in easy_problems:
#                     print(problem)

#                 print(f"\nMedium Problems ({len(medium_problems)}):")
#                 for problem in medium_problems:
#                     print(problem)

#                 print(f"\nHard Problems ({len(hard_problems)}):")
#                 for problem in hard_problems:
#                     print(problem)
#             else:
#                 print("Solved problem section not found.")
#         else:
#             print(f"Failed to fetch data for {username}. Status code: {response.status_code}")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# # # Example usage
# scrape_gfg_problems("suryapraq1ec")

# import requests
# from bs4 import BeautifulSoup

# def scrape_gfg_problems(username):
#     try:
#         # Construct the GFG profile URL for the given username
#         url = f"https://www.geeksforgeeks.org/user/suryapraq1ec/"
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#         }

#         # Send GET request to fetch profile page
#         response = requests.get(url, headers=headers)

#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')

#             # Identify the section containing solved problems
#             problem_sections = soup.find_all('div', class_='solvedProblemSection_head__VEUg4')

#             if problem_sections:
#                 print(f"Problems solved by {username}:")
#                 for section in problem_sections:
#                     problems = section.find_all('a')  # Find all problem links
#                     for problem in problems:
#                         title = problem.text.strip()  # Extract problem title
#                         link = problem['href'] if 'href' in problem.attrs else 'No link'
#                         print(f"- {title}: {link}")
#             else:
#                 print("No solved problems section found on the page.")
#         else:
#             print(f"Failed to fetch the profile for {username}. HTTP Status: {response.status_code}")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# scrape_gfg_problems("suryapraq1ec")
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep

# def scrape_gfg_problems(username):
#     try:
#         # Construct the GFG profile URL for the given username
#         url = f"https://www.geeksforgeeks.org/user/bhaviyamb3n9w/?ref=header_profile"
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#         }

#         # Set up the WebDriver
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         driver.get(url)
#         sleep(3)  # Wait for the page to load

#         # Identify the section containing solved problems
#         problem_sections = driver.find_elements(By.CSS_SELECTOR, 'div.solvedProblemSection_head__VEUg4')

#         problem_links = []  # List to store problem links

#         if problem_sections:
#             print(f"Problems solved by {username}:")
#             for section in problem_sections:
#                 problems = section.find_elements(By.TAG_NAME, 'a')  # Find all problem links
#                 for problem in problems:
#                     title = problem.text.strip()  # Extract problem title
#                     link = problem.get_attribute('href')  # Get the URL of the problem
#                     if link:
#                         problem_links.append((title, link))
#                         print(f"- {title}: {link}")
#         else:
#             print("No solved problems section found on the page.")

#         # Now visit each problem link and scrape difficulty and tags
#         print("\nScraping tags and difficulty for each problem...\n")
#         for title, link in problem_links:
#             scrape_problem_details(driver, title, link)
#             break

#         driver.quit()

#     except Exception as e:
#         print(f"An error occurred: {e}")

# def scrape_problem_details(driver, title, link):
#     try:
#         # Open the problem page
#         driver.get(link)
#         sleep(3)  # Wait for the page to load

#         # Extract difficulty using the provided CSS selector
#         difficulty_element = driver.find_element(By.CSS_SELECTOR, "#scrollableDiv > div > div.undefined > div.problems_header_description__t_8PB")
#         difficulty_text = difficulty_element.text.strip() if difficulty_element else "Unknown"

#         # Extract topic tags using the provided CSS selector
#         tags_elements = driver.find_elements(By.CSS_SELECTOR, "#scrollableDiv > div > div.undefined > div.accordion.ui.problems_accordion_tags_container__zk2Um > div.problems_accordion_tags__JJ2DX.problems_active_tags__3RExF > div.content.active")
#         topic_tags = [tag.text.strip() for tag in tags_elements]

#         # Print or save the details
#         print(f"Problem: {title}")
#         print(f"Difficulty: {difficulty_text}")
#         print(f"Tags: {', '.join(topic_tags)}\n")

#     except Exception as e:
#         print(f"An error occurred while fetching details for {title}: {e}")

# # Example usage
# scrape_gfg_problems("suryapraq1ec")

