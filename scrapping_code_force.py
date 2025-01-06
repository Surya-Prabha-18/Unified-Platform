import requests
import json

url = "https://codeforces.com/api/problemset.problems"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convert response to JSON
    if data['status'] == 'OK':
        # Save the data to a JSON file
        with open("codeforces_problems.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Data successfully saved to 'codeforces_problems.json'")
    else:
        print(f"API Error: {data.get('comment', 'Unknown error')}")
else:
    print(f"HTTP Error: {response.status_code}")
