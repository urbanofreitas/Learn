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
        logging.info(f"Data Received Type: {data_received_type} ") #Added by me (not the original code)

        logging.info(f"URL: {url}")
        logging.info(f"Status Code: {response.status_code}")
        logging.info(f"Payload Size: {payload_size} bytes")
        logging.info(f"Number of Records got: {number_of_records} ") #Added by me (not the original code)
        logging.info(f"Time Taken: {elapsed_time:.4f} seconds")
        
        return response.json()        
        
        '''
        # below is a failed 
        #Get the number of "lines" in the json response
        size_test = response.__sizeof__()
        logging.info(f"Size Test: {size_test} ") #Added by me (not the original code)

        logging.info(f"Time Taken: {elapsed_time:.4f} seconds")

        '''


    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data:{e}")
        return None
    

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    data = fetch_data(api_url)

    if data:
        print(json.dumps(data, indent=4)) # Pretty print the json data
        print(data)