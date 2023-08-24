import requests
import api
import pytest





def get_tasks():
    response = requests.get("https://example-api.com/tasks")
    return response.json()
def test_get_tasks_status_code():
    response = api.get_tasks()
    assert response.status_code == 200
def test_get_tasks_data():
    response = api.get_tasks()
    assert "tasks" in response


BASE_URL = "https://example-api.com"
HEADERS = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}  # Replace with your actual access token
def get_tasks():
    response = requests.get(f"{BASE_URL}/tasks", headers=HEADERS)
    return response
def create_task(title):
    data = {"title": title}
    response = requests.post(f"{BASE_URL}/tasks", json=data, headers=HEADERS)
    return response
def update_task(task_id, title):
    data = {"title": title}
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=data, headers=HEADERS)
    return response
def delete_task(task_id):
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}", headers=HEADERS)
    return response.status_code
def test_get_tasks_status_code():
    response = get_tasks()
    assert response.status_code == 200
def test_get_tasks_data():
    response = get_tasks()
    assert "tasks" in response.json()
def test_create_task():
    new_task_title = "New Task"
    response = create_task(new_task_title)
    assert response.status_code == 200
    assert response.json()["title"] == new_task_title
def test_update_task():
    task_id = 1
    updated_task_title = "Updated Task"
    response = update_task(task_id, updated_task_title)
    assert response.status_code == 200
    assert response.json()["title"] == updated_task_title
def test_delete_task():
    task_id = 1
    response = delete_task(task_id)
    assert response == 204


import requests
import api
import pytest
'''
Given the user would like to create a learning record using an API
When they access the MLTSD CMS API Learning Records endpoint
Then they can execute a call to create a learning record
And the request headers and parameters should mirror the parameters identified in the documentation link above
When the learner unique id does not exist in the system
Then insert the learning record
When the learner unique id does exist in the system
Then update the learning record
'''
def get_data_new():  # Add Learning Record AP
    print('Add Learning Record AP')
    url = "https://private-anon-78376c118a-bluedrop360apiv2network.apiary-mock.com/api-v2/learning-records"
    headers = {
        "Content-Type": "application/json",
    }
    body = {
      "learningRecordId": "4108123e-7f35-4097-928a-5bccd5fe4111",
      "trainingStandardKey": "WAH-E-B",
      "completionDate": "2018-11-21T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "external-class-111",
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-121",
        "firstname": "Peter",
        "lastname": "Johnson",
        "personalEmail": "perter.johnson@example.com",
        "birthYear": 1995,
        "address": {
          "street-address": "1230 Main Street",
          "extended-address": "PO Box 1234",
          "locality": "Toronto",
          "region": "ON",
          "postal-code": "M7A 1T7",
          "country-name": "Canada"
        },
        "mobilePhone": "6047771234",
        "homePhone": "7782225678"
      }
    }

    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)  # 204
    # print(response.json())
    # print(response.text)


get_data_new()