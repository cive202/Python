import requests


try:
    url = "https://example.com/students"

    response = request.get(url)

    datas = response.json()
except request.exceptions.ConnectionError:
    print("Cannot connect to the server")
except request.exceptions.Timeout:
    print("Request Time Out")
except request.exception.HTTPError as e:
    print(f"HTTPError {e.reponse.status_code}")
except request.expection.ValueError as e:
    print("Response is invalid Json")

for data in datas:
    print(f"{data['StudentID']}==> {data['Score']}")
