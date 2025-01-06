import requests
import json

# Initialize a list to store all problems
all_results = []

# Loop through the pages (adjust the range as needed)
for page in range(1, 234):  # Adjust the upper limit of the range based on the total number of pages
    try:
        # Make an API request for the current page
        response = requests.get(
            f"https://www.codechef.com/api/list/problems?page={page}&limit=20&sort_by=difficulty_rating&sort_order=asc&search=&category=rated&start_rating=0&end_rating=5000&topic=&tags=&group=all&"
        )
        
        # Check if the response is successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract problems from the current page
            for problem in data.get("data", []):
                # Create a dictionary for each problem
                problem_data = {
                    "problem_name": problem.get("name", ""),
                    "problem_code": problem.get("code", ""),
                    "difficulty_rating": problem.get("difficulty_rating", ""),
                    "total_submissions": problem.get("total_submissions", ""),
                    "successful_submissions": problem.get("successful_submissions", ""),
                    "partially_successful_submissions": problem.get("partially_successful_submissions", ""),
                    "contest_code": problem.get("contest_code", ""),
                    "intended_contest_id": problem.get("intended_contest_id", ""),
                }
                # Add the problem data to the results list
                all_results.append(problem_data)
        else:
            print(f"Failed to fetch data for page {page}: HTTP {response.status_code}")
            break
    except Exception as e:
        print(f"An error occurred on page {page}: {e}")
        break

# Save all the collected problem data to a JSON file
with open("problems.json", "w") as json_file:
    json.dump(all_results, json_file, indent=4)

print("Data has been stored in problems.json")
