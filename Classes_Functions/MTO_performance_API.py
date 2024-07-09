import time
import pytest
import requests
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import api
import base64
from urllib.parse import urlencode


def sso_00_token():
    print('sso')
    token_url = 'https://adfsonekey-auth.login.sys.uat.cf.az.cihs.gov.on.ca/oauth/token'
    username = '53c40844-99ca-4147-8719-78efa536bcf4'
    password = '22438e67-77cf-40ed-957e-28a261c82fe0'
    headers = {
        'Authorization': f'Basic {base64.b64encode(f"{username}:{password}".encode()).decode()}',
        'Content-Type': 'application/x-www-form-urlencoded',  # Adjust the content type based on your API's requirements
    }
    data = {
        'grant_type': 'client_credentials'
    }
    # Encode the data in x-www-form-urlencoded format
    encoded_data = urlencode(data)

    # Make the API request
    response = requests.post(token_url, data=encoded_data, headers=headers)
    print(response.status_code)  # 204
    print(response.text)
    response_json = response.json()
    access_token = response_json.get('access_token')
    print(access_token)
    return response.text


# Response times
def api_01_response_time_delete_online_offering():
    print('Response_time')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-uat/OnlineOffering/wah-131"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NmIxOWYwYjdlMTA0N2E3YTc5MmQ3MzI0OTgzM2Y4YyIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDU2NzQ2MTgsImV4cCI6MTcwNTcxNzgxOCwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.nretAA6xgczpnXalSfUTGomYOSqP1Qr_d63_6Mf92KJ4xq5qDG9owoeVarvWJLh2ne1jWg7fgH4Ky77sYDhlQlwccWRj0rfE4W4IHfEa8GnnjvbX68eZCJI8KhlACFgiJMSgJpgIU9nEqULUWa0n3Df9oboxHnwltQG1A6RuVPN_Kdb4a0CD6hE669NvGEn1M6qG71QzSUf5J1J_nXls-5cKg6ms3sEMicJ8eZGNR4A15IZ1JjYnqoeeK20FigSXB-4ffuDvUB5XfcKy3WMENRTz7LZ4zw-wNW4ngd0Luu3fTpDFJwj9ckrQLDwLzJWliDw5fnSHC_tUm0tfr7PlcQ",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json; charset=utf-8"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.delete(url, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)


def api_02_response_time_delete_class_offering():
    print('Response_time')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-uat/ClassOffering/wah-131"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NmIxOWYwYjdlMTA0N2E3YTc5MmQ3MzI0OTgzM2Y4YyIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDU2NzQ2MTgsImV4cCI6MTcwNTcxNzgxOCwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.nretAA6xgczpnXalSfUTGomYOSqP1Qr_d63_6Mf92KJ4xq5qDG9owoeVarvWJLh2ne1jWg7fgH4Ky77sYDhlQlwccWRj0rfE4W4IHfEa8GnnjvbX68eZCJI8KhlACFgiJMSgJpgIU9nEqULUWa0n3Df9oboxHnwltQG1A6RuVPN_Kdb4a0CD6hE669NvGEn1M6qG71QzSUf5J1J_nXls-5cKg6ms3sEMicJ8eZGNR4A15IZ1JjYnqoeeK20FigSXB-4ffuDvUB5XfcKy3WMENRTz7LZ4zw-wNW4ngd0Luu3fTpDFJwj9ckrQLDwLzJWliDw5fnSHC_tUm0tfr7PlcQ",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.delete(url, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)


def api_03_response_time_add_class_offering():
    print('Response_time')
    num_requests = 100  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-uat/ClassOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NmIxOWYwYjdlMTA0N2E3YTc5MmQ3MzI0OTgzM2Y4YyIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDU2NzQ2MTgsImV4cCI6MTcwNTcxNzgxOCwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.nretAA6xgczpnXalSfUTGomYOSqP1Qr_d63_6Mf92KJ4xq5qDG9owoeVarvWJLh2ne1jWg7fgH4Ky77sYDhlQlwccWRj0rfE4W4IHfEa8GnnjvbX68eZCJI8KhlACFgiJMSgJpgIU9nEqULUWa0n3Df9oboxHnwltQG1A6RuVPN_Kdb4a0CD6hE669NvGEn1M6qG71QzSUf5J1J_nXls-5cKg6ms3sEMicJ8eZGNR4A15IZ1JjYnqoeeK20FigSXB-4ffuDvUB5XfcKy3WMENRTz7LZ4zw-wNW4ngd0Luu3fTpDFJwj9ckrQLDwLzJWliDw5fnSHC_tUm0tfr7PlcQ",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json"
    }
    body = {
        "offeringId": "wah-383",  # need to make a new ID any new call
        "trainingStandardKey": "JHSC-2014-2-10096",  # related to the Class ID inside the training programs schedules
        "deliveryMethod": "in-person",
        "courseName": "Working At Heights",
        "seatsRemaining": 10,
        "contactForPricing": False,
        "price": 300,
        "address": {
            "street-address": "169 fort york",
            "extended-address": "PO Box 1234",
            "locality": "Toronto",
            "region": "ON",
            "postal-code": "M5V 0C8",
            "country-name": "Canada"
        },
        "events": [
            {
                "start": "2023-11-24T10:30:00.000Z",
                "end": "2023-11-24T12:00:00.000Z"
            }
        ],
        "externalRegistrationUrl": "https://training-provider.com/reserve-seats/10012",
        "virtualClassUrl": "https://virtual-class-example.com/10001"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.post(url, json=body, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)


def api_04_response_time_update_class_offering():
    print('Response_time')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-uat/ClassOffering/wah-383"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NmIxOWYwYjdlMTA0N2E3YTc5MmQ3MzI0OTgzM2Y4YyIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDU2NzQ2MTgsImV4cCI6MTcwNTcxNzgxOCwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.nretAA6xgczpnXalSfUTGomYOSqP1Qr_d63_6Mf92KJ4xq5qDG9owoeVarvWJLh2ne1jWg7fgH4Ky77sYDhlQlwccWRj0rfE4W4IHfEa8GnnjvbX68eZCJI8KhlACFgiJMSgJpgIU9nEqULUWa0n3Df9oboxHnwltQG1A6RuVPN_Kdb4a0CD6hE669NvGEn1M6qG71QzSUf5J1J_nXls-5cKg6ms3sEMicJ8eZGNR4A15IZ1JjYnqoeeK20FigSXB-4ffuDvUB5XfcKy3WMENRTz7LZ4zw-wNW4ngd0Luu3fTpDFJwj9ckrQLDwLzJWliDw5fnSHC_tUm0tfr7PlcQ",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json; charset=utf-8"
    }
    body = {
      "courseName": "Working At Heights",
      "seatsRemaining": 15,
      "contactForPricing": False,
      "price": 400,
      "address": {
        "street-address": "1230 Main Street",
        "extended-address": "PO Box 1234",
        "locality": "Toronto",
        "region": "ON",
        "postal-code": "M7A 1T7",
        "country-name": "Canada"
      },
      "events": [
        {
          "start": "2023-11-25T10:30:00.000Z",
          "end": "2023-11-25T12:00:00.000Z"
        }
      ],
      "externalRegistrationUrl": "https://training-provider.com/reserve-seats/10012",
      "virtualClassUrl": "https://virtual-class-example.com/10001"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.patch(url, json=body, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)


def api_05_response_time_add_online_offering():
    print('Response_time')
    num_requests = 30  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-uat/OnlineOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NmIxOWYwYjdlMTA0N2E3YTc5MmQ3MzI0OTgzM2Y4YyIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDU2NzQ2MTgsImV4cCI6MTcwNTcxNzgxOCwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.nretAA6xgczpnXalSfUTGomYOSqP1Qr_d63_6Mf92KJ4xq5qDG9owoeVarvWJLh2ne1jWg7fgH4Ky77sYDhlQlwccWRj0rfE4W4IHfEa8GnnjvbX68eZCJI8KhlACFgiJMSgJpgIU9nEqULUWa0n3Df9oboxHnwltQG1A6RuVPN_Kdb4a0CD6hE669NvGEn1M6qG71QzSUf5J1J_nXls-5cKg6ms3sEMicJ8eZGNR4A15IZ1JjYnqoeeK20FigSXB-4ffuDvUB5XfcKy3WMENRTz7LZ4zw-wNW4ngd0Luu3fTpDFJwj9ckrQLDwLzJWliDw5fnSHC_tUm0tfr7PlcQ",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json"
    }
    body = {
      "offeringId": "wah-131",    # need to make a new ID any new call
      "trainingStandardKey": "JHSC-2014-2-10096",  # related to the Class ID inside the training programs schedules
      "courseName": "JHSC - Part One",
      "price": 111,
      "courseDuration": 4,
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.post(url, json=body, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)


def api_06_response_time_update_online_offering():
    print('Response_time')
    num_requests = 30  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-uat/OnlineOffering/wah-131"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NmIxOWYwYjdlMTA0N2E3YTc5MmQ3MzI0OTgzM2Y4YyIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDU2NzQ2MTgsImV4cCI6MTcwNTcxNzgxOCwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.nretAA6xgczpnXalSfUTGomYOSqP1Qr_d63_6Mf92KJ4xq5qDG9owoeVarvWJLh2ne1jWg7fgH4Ky77sYDhlQlwccWRj0rfE4W4IHfEa8GnnjvbX68eZCJI8KhlACFgiJMSgJpgIU9nEqULUWa0n3Df9oboxHnwltQG1A6RuVPN_Kdb4a0CD6hE669NvGEn1M6qG71QzSUf5J1J_nXls-5cKg6ms3sEMicJ8eZGNR4A15IZ1JjYnqoeeK20FigSXB-4ffuDvUB5XfcKy3WMENRTz7LZ4zw-wNW4ngd0Luu3fTpDFJwj9ckrQLDwLzJWliDw5fnSHC_tUm0tfr7PlcQ",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json"
    }
    body = {
      "courseName": "JHSC - Part One",
      "price": 222,
      "courseDuration": 3,
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.patch(url, json=body, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)


def api_07_response_time_add_learning_record():
    print('Response_time')
    num_requests = 30  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-uat/LearningRecord"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NmIxOWYwYjdlMTA0N2E3YTc5MmQ3MzI0OTgzM2Y4YyIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDU2NzQ2MTgsImV4cCI6MTcwNTcxNzgxOCwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.nretAA6xgczpnXalSfUTGomYOSqP1Qr_d63_6Mf92KJ4xq5qDG9owoeVarvWJLh2ne1jWg7fgH4Ky77sYDhlQlwccWRj0rfE4W4IHfEa8GnnjvbX68eZCJI8KhlACFgiJMSgJpgIU9nEqULUWa0n3Df9oboxHnwltQG1A6RuVPN_Kdb4a0CD6hE669NvGEn1M6qG71QzSUf5J1J_nXls-5cKg6ms3sEMicJ8eZGNR4A15IZ1JjYnqoeeK20FigSXB-4ffuDvUB5XfcKy3WMENRTz7LZ4zw-wNW4ngd0Luu3fTpDFJwj9ckrQLDwLzJWliDw5fnSHC_tUm0tfr7PlcQ",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json"
    }
    body = {
      "learningRecordId": "wah-350",
      "trainingStandardKey": "JHSC-2014-2-10096",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-999",
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
    for i in range(num_requests):
        start_time = time.time()
        response = requests.post(url, json=body, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)


body1 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam1.johnson@example.com",  # need to be changed for new record creations within the same class
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
body2 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam2.johnson@example.com",  # need to be changed for new record creations within the same class
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
body3 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam3.johnson@example.com",  # need to be changed for new record creations within the same class
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
body4 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam4.johnson@example.com",  # need to be changed for new record creations within the same class
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
body5 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam5.johnson@example.com",  # need to be changed for new record creations within the same class
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
body6 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam6.johnson@example.com",  # need to be changed for new record creations within the same class
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
body7 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam7.johnson@example.com",  # need to be changed for new record creations within the same class
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
body8 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam8.johnson@example.com",  # need to be changed for new record creations within the same class
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
body9 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam9.johnson@example.com",  # need to be changed for new record creations within the same class
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
body10 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam10.johnson@example.com",  # need to be changed for new record creations within the same class
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
listofbodyapi = [body1, body2, body3, body4, body5, body6, body7, body8, body9, body10]


def api_08_response_time_add_10_learning_records():
    print('Response_time')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-uat/LearningRecord"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NmIxOWYwYjdlMTA0N2E3YTc5MmQ3MzI0OTgzM2Y4YyIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDU2NzQ2MTgsImV4cCI6MTcwNTcxNzgxOCwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.nretAA6xgczpnXalSfUTGomYOSqP1Qr_d63_6Mf92KJ4xq5qDG9owoeVarvWJLh2ne1jWg7fgH4Ky77sYDhlQlwccWRj0rfE4W4IHfEa8GnnjvbX68eZCJI8KhlACFgiJMSgJpgIU9nEqULUWa0n3Df9oboxHnwltQG1A6RuVPN_Kdb4a0CD6hE669NvGEn1M6qG71QzSUf5J1J_nXls-5cKg6ms3sEMicJ8eZGNR4A15IZ1JjYnqoeeK20FigSXB-4ffuDvUB5XfcKy3WMENRTz7LZ4zw-wNW4ngd0Luu3fTpDFJwj9ckrQLDwLzJWliDw5fnSHC_tUm0tfr7PlcQ",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json"
    }
    body = {
      "learningRecordId": "wah-350",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-999",
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
    for i in range(num_requests):
        start_time = time.time()
        response = requests.post(url, json=listofbodyapi[i], headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)