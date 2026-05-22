import json
import datetime
import os

def update_status():
    status_file = 'wiki/docs/assets/build_status.json'
    
    data = {
        "last_build": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Operational",
        "environment": "Bare Metal / ProperDocs",
        "version": "1.2.0"
    }
    
    os.makedirs(os.path.dirname(status_file), exist_ok=True)
    with open(status_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    update_status()
