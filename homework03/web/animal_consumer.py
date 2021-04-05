import requests

print("Response Animals\n")

response = requests.get(url="http://localhost:5031/animals")

print(response.status_code)
print(response.json())
print(response.headers)

print("\nResponse Heads")

response2 = requests.get(url="http://localhost:5031/animals/heads")

print(response2.status_code)
print(response2.json())
print(response2.headers)

print("\nResponse Legs")

response3 = requests.get(url="http://localhost:5031/animals/legs")

print(response3.status_code)
print(response3.json())
print(response3.headers)
