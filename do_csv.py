import csv


def save_to_csv(cars):
    file_path = "results_scrapper.csv"

    with open(file_path, mode='w', newline='') as file:
        columns = ["name", "cost", "year", "mileage", "rekkevidde", "img"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(cars)

    return file_path