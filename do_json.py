import json


def save_to_json(cars):
    file_path = "results_scrapper.json"

    with open(file_path, mode='w') as file:
        json.dump(cars, file, indent=4, ensure_ascii=False)

    
    return file_path