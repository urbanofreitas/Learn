import requests
import logging
import time
import json


# Configure logging
logging.basicConfig(filename='api_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_data(url):
    start_time = time.time()
    try:
        response = requests.get(url)
        response.raise_for_status() #Raise an exception for bad status codes (4xx or 5xx)
        end_time = time.time()
        elapsed_time = end_time - start_time
        payload_size = len(response.content)
        number_of_records = len(response.json())#Added by me (not the original code)
        data_received_type = type(response.json())
        data_received_size = len(response.json())


        logging.info(f"URL: {url}")
        logging.info(f"Status Code: {response.status_code}")
        logging.info(f"Payload Size: {payload_size} bytes")
        logging.info(f"Number of Records got: {number_of_records} ") #Added by me (not the original code)
        logging.info(f"Data Received Type: {data_received_type} ") #Added by me (not the original code)
        logging.info(f"Data Received Size: {data_received_size} ") #Added by me (not the original code)
        logging.info(f"Time Taken: {elapsed_time:.4f} seconds")


        return response.json()        
        

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data:{e}")
        return None
    

def fetch_paginated_data(base_url, num_pages=5): # Simulate pagination
    all_data = []
    for page in range(1, num_pages + 1):
        url = f"{base_url}/{page}"
        data = fetch_data(url)
        if data:
            all_data.append(data)
    return all_data

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/todos"
    all_data = fetch_paginated_data(base_url)

    if all_data:
        print(json.dumps(all_data, indent=4))