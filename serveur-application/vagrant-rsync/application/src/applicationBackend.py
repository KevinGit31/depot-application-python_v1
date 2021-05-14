import requests

url = "http://172.30.1.7:8081/service/rest/v1/components?repository=nexus-python"
payload = {}
headers = {
  'Authorization': 'Basic YWRtaW46bmV4dXNfcHl0aG9u'
}


def getComponents():
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()["items"]
    # print(response)
    return response
