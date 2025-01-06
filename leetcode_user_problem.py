import leetcode
from datetime import date

def fetch_solved_problems(username, leetcode_session, csrf_token):
    # Configure the API client
    configuration = leetcode.Configuration()
    configuration.api_key["x-csrftoken"] = csrf_token
    configuration.api_key["LEETCODE_SESSION"] = leetcode_session
    configuration.debug = False

    # Initialize API client
    api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))

    try:
        # Verify user session
        graphql_query = leetcode.GraphqlQuery(
            query="""
            query {
                user {
                    username
                    isCurrentUserPremium
                }
            }
            """,
            variables=leetcode.GraphqlQueryVariables(),
        )
        user_response = api_instance.graphql_post(body=graphql_query)

        # Validate username
        if user_response.data.user.username != username:
            return {"error": "Invalid username or session details."}

        # Fetch solved problems
        problems_response = api_instance.api_problems_topic_get(topic="algorithms")
        solved_problems = []

        for question in problems_response.stat_status_pairs:
            if question.status == "ac":  # Check if the problem is solved
                solved_problems.append(question.stat.question__title)

        return {
            "username": username,
            "solved_count": len(solved_problems),
            "solved_problems": solved_problems,
            "last_updated": date.today().isoformat(),
        }

    except leetcode.ApiException as e:
        return {"error": f"API Exception: {e}"}


# Example usage
if __name__ == "__main__":
    leetcode_username = "bharathwaj8282"
    leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTMwMjY4NDYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYmU1ZTEyOWYyZWI3YjI5YjczN2RmZGFiZjIwZTYyZmYwM2MyNWNmNTE0NDEyODRiMDJmYjM3NDg0MTcyNzQxIiwic2Vzc2lvbl91dWlkIjoiYjQzNmRlNmQiLCJpZCI6MTMwMjY4NDYsImVtYWlsIjoiYmhhcmF0aHdhajgyODJAZ21haWwuY29tIiwidXNlcm5hbWUiOiJiaGFyYXRod2FqODI4MiIsInVzZXJfc2x1ZyI6ImJoYXJhdGh3YWo4MjgyIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2JoYXJhdGh3YWo4MjgyL2F2YXRhcl8xNzEyOTk2MjExLnBuZyIsInJlZnJlc2hlZF9hdCI6MTczNjA3MDgyOCwiaXAiOiIyNDAxOjQ5MDA6NjdhYTpkZjNkOjEwY2U6YzM4ZjoyYTE0OmM3MyIsImlkZW50aXR5IjoiZjUxYmI0ODJjNjYwZDBlZWFkZDFmMDU4MDU4YTJiMzUiLCJkZXZpY2Vfd2l0aF9pcCI6WyJjNDFjYzJmY2FmMDkyMGY1ZDhlNGE1NmU1YmZhNzAxNiIsIjI0MDE6NDkwMDo2N2FhOmRmM2Q6MTBjZTpjMzhmOjJhMTQ6YzczIl0sIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.ZHgcM0l8RdiTfP52x88GtwbHSAjj52d2UYUUUjPVs50"
    csrf_token = "iR3KrBXJIBLalT5K9WP0C76ryPz8xqpxEWXPfeUck2s0qBpZVJoIYdILbmgtQ4Ds"
    result = fetch_solved_problems(leetcode_username, leetcode_session, csrf_token)
    if "error" in result:
        print(result["error"])
    else:
        print(f"User: {result['username']}")
        print(f"Solved Problems Count: {result['solved_count']}")
        print(f"Last Updated: {result['last_updated']}")
        print("Solved Problems:")
        for problem in result["solved_problems"]:
            print(f"- {problem}")