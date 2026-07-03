from openpyxl import Workbook


def save_to_excel(cars):
    file_path = "results_scrapper.xlsx"
    wb = Workbook()
    ws = wb.active
    ws.title = "Cars"

    columns = ["name", "cost", "year", "mileage", "rekkevidde", "img"]

    ws.append(columns)

    for car in cars:
        ws.append([
            car["name"],
            car["cost"],
            car["year"],
            car["mileage"],
            car["rekkevidde"],
            car["img"]
        ])

    wb.save(file_path)
    return file_path