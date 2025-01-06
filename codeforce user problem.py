import requests
import json
from json import JSONDecodeError

def fetch_solved_problems_with_tags(handle):
    result_data = []  # List to store the result data
    
    try:
        # Fetch all solved problems for the user
        user_url = f"https://codeforces.com/api/user.status?handle={handle}"
        problemset_url = "https://codeforces.com/api/problemset.problems"

        # Fetch user's submissions with exception handling
        user_response = requests.get(user_url, timeout=10)
        user_response.raise_for_status()  # Raise an error for bad status codes
        user_data = user_response.json()

        # Check if user data is valid
        if user_data.get('status') != 'OK' or not user_data.get('result'):
            print(f"Error: No submissions found for user '{handle}'.")
            return

        # Fetch problemset data (for tags)
        problemset_response = requests.get(problemset_url, timeout=10)
        problemset_response.raise_for_status()
        problemset_data = problemset_response.json()

        # Prepare a dictionary mapping (contestId, index) to tags
        problem_tags = {}
        for problem in problemset_data['result']['problems']:
            key = (problem['contestId'], problem['index'])
            problem_tags[key] = {
                'name': problem['name'],
                'tags': problem['tags']
            }

        # Filter solved problems with topic tags
        solved_problems = set()
        for submission in user_data['result']:
            try:
                if submission.get('verdict') == 'OK':
                    contest_id = submission['problem']['contestId']
                    index = submission['problem']['index']
                    key = (contest_id, index)
                    # Fetch problem name and tags
                    if key in problem_tags:
                        problem_info = problem_tags[key]
                        solved_problems.add((
                            f"{contest_id}{index}",
                            problem_info['name'],
                            ", ".join(problem_info['tags'])
                        ))
            except (KeyError, TypeError):
                print("Error: Invalid data format received for a submission.")

        # Prepare result data to store in JSON file
        if solved_problems:
            print(f"\nSolved Problems with Tags for {handle}:")
            for problem in sorted(solved_problems):
                # Collecting the results to be written in JSON
                result_data.append({
                    'problem_id': problem[0],
                    'problem_name': problem[1],
                    'tags': problem[2]
                })
        else:
            print(f"No solved problems found for {handle}.")

        # Write the result data to a JSON file
        if result_data:
            with open(f"{handle}_solved_problems.json", 'w') as json_file:
                json.dump(result_data, json_file, indent=4)
            print(f"Results saved in {handle}_solved_problems.json.")

    except requests.exceptions.ConnectionError:
        print("Error: Network connection issue.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except JSONDecodeError:
        print("Error: Failed to decode JSON response.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
fetch_solved_problems_with_tags("Letscode_sundar")



