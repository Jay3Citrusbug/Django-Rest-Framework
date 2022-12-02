import requests

r=requests.get(url="http://127.0.0.1:8000/stu_data/")

data=r.json()
print(data)

