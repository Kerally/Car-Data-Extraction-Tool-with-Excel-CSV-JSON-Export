from flask import Flask, render_template, request, send_file, redirect, url_for
from scrapper_finn_no import get_cars
from do_csv import save_to_csv
from do_json import save_to_json
from do_excel import save_to_excel


app = Flask(__name__)

scraped_cars = []


@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    cars = []

    if request.method == "POST":
        action = request.form.get("action")
        if action == "Scrape":
            global scraped_cars
            scraped_cars = get_cars()
            return redirect(url_for("index", show="1"))

        elif action == "Save_to_JSON":
            cars = get_cars()
            file_path = save_to_json(cars)

            return send_file(
                file_path,
                as_attachment=True,
                download_name="result_json_scrapper.json"
            )
        
        elif action == "Save_to_CSV":
            cars = get_cars()
            file_path = save_to_csv(cars)

            return send_file(
                file_path,
                as_attachment=True,
                download_name="result_csv_scrapper.csv"
            )

        elif action == "Save_to_Excel":
            cars = get_cars()   
            file_path = save_to_excel(cars)

            return send_file(
                file_path,
                as_attachment=True,
                download_name="result_excel_scrapper.xlsx"
            )

    if request.args.get("show") == "1":
        cars = scraped_cars
        if cars:
            text = f"Found {len(cars)} cars"

    return render_template("index.html", text=text, cars=cars)


if __name__ == "__main__":
    app.run(debug=True)

