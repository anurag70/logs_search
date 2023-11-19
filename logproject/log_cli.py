import requests

BASE_URL = "http://localhost:8000" 

def search_logs(params):
    try:
        response = requests.get(f"{BASE_URL}/log/search", params={"search": ",".join(params)})
        response.raise_for_status()
        logs = response.json()
        display_logs(logs)
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

def display_logs(logs):
    if not logs:
        print("No logs found.")
        return

    header = ["Level", "Message", "Resource ID", "Timestamp", "traceId", "spanId","metadata","resourceId"]
    print("{:<10} {:<40} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*header))

    for log in logs:
        log_data = [
            log.get("level", ""),
            log.get("message", ""),
            log.get("resourceId", ""),
            log.get("timestamp", ""),
            log.get("traceId",""),
            log.get("spanId",""),
            log.get("metadata",{}),
            log.get("resourceId",""),
        ]
        print("{:<10} {:<40} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*log_data))

if __name__ == "__main__":
   search_params = input("Enter search parameters in the format 'level:INFO,message:....' ... in this way: ").split(",")
    
   search_logs(search_params)