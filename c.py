import requests
import time  # Import the time module

# Define the API endpoint and parameters
url = "http://indianrailapi.com/api/v2/AllTrainOnStation/apikey/c02a7f58ba2f351d65241ff5c4fe2a08/StationCode/SNKL"

try:
    # Start the timer
    start_time = time.time()

    # Make the GET request with a timeout of 600 seconds
    response = requests.get(url, timeout=600)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()  # Parse the JSON response

    # Stop the timer
    end_time = time.time()
    time_taken = end_time - start_time

    # Print the train details
    if "Trains" in data:
        print("Trains arriving at or departing from the station:")
        for train in data["Trains"]:
            print(f"Train No: {train['TrainNo']}, Train Name: {train['TrainName']}, "
                  f"Arrival: {train['ArrivalTime']}, Departure: {train['DepartureTime']}")
    else:
        print("No trains found or invalid response format.")

    # Print the time taken
    print(f"Time taken for the request: {time_taken:.2f} seconds")
except requests.exceptions.Timeout:
    print("Request timed out")
except Exception as e:
    print(f"Error: {e}")