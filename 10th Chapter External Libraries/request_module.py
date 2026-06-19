import requests 

r = requests.get("https://api.github.com/events")

q = requests.get("https://api.github.com/users/aarnavkothawade")

print(q)
print(q.text)