import requests

level=input("Enter level (easy,medium,hard): ")
response = requests.get(f"https://sugoku.herokuapp.com/board?difficulty={level}")
grid = response.json()['board']

print(grid)

