import requests


BASE = "http://127.0.0.1:5000/api-yagoo/"


respanse = requests.put(
    BASE+"rate-poste",
    json={
        "userID": "20devlpe2021",
        "PosteID": "20Poste2021",
        "RateOnPoste": 5
    }
)
print(respanse.json())
