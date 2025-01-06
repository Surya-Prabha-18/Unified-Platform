import requests
import json
import time

# Function to fetch all problems from LeetCode
def get_all_problems():
    url = "https://leetcode.com/graphql"

    # GraphQL query to fetch all problems
    query = """
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
        problemsetQuestionList: questionList(
            categorySlug: $categorySlug
            limit: $limit
            skip: $skip
            filters: $filters
        ) {
            total: totalNum
            questions: data {
                acRate
                difficulty
                freqBar
                frontendQuestionId: questionFrontendId
                isFavor
                paidOnly: isPaidOnly
                status
                title
                titleSlug
                content
                topicTags {
                    name
                    id
                    slug
                }
                hasSolution
                hasVideoSolution
            }
        }
    }
    """

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    problems_list = []  # To store all problems

    skip = 0
    limit = 100  # Fetch 100 problems per request

    while True:
        variables = {
            "categorySlug": "",
            "skip": skip,
            "limit": limit,
            "filters": {}
        }

        payload = {
            "query": query,
            "variables": variables
        }

        # Send the POST request
        response = requests.post(url, json=payload, headers=headers)

        # Check if the response is successful
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            print(response.json())
            break

        # Parse the JSON response
        response_data = response.json()

        if "errors" in response_data:
            print(f"Error message: {response_data['errors']}")
            break

        questions = response_data['data']['problemsetQuestionList']['questions']
        total = response_data['data']['problemsetQuestionList']['total']

        if not questions:  # No more questions
            break

        # Collect the problem details into a list
        for question in questions:
            problem = {
                "title": question['title'],
                "description": question.get('content', 'No description available'),
                "tags": [tag['name'] for tag in question['topicTags']],
                "difficulty": question['difficulty'],
                "acceptance_rate": question['acRate'],
                "status": question['status'],
                "slug": question['titleSlug'],
                "frontend_id": question['frontendQuestionId']
            }
            problems_list.append(problem)

        skip += limit

        # Stop scraping once we have retrieved all problems
        if skip >= total:
            break

        time.sleep(1)  # Sleep to avoid hitting rate limits

    print(f"Total problems scraped: {len(problems_list)}")

    # Save the problems to a JSON file
    with open('leetcode_problems.json', 'w', encoding='utf-8') as f:
        json.dump(problems_list, f, ensure_ascii=False, indent=4)

# Example Usage:
get_all_problems()
