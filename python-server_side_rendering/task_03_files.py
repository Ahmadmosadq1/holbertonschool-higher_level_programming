from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get("source", "").lower()
    user_id = request.args.get("user_id")
    item_list = []
    error = None

    try:
        if source == "json":
            with open("products.json", "r") as file:
                all_items = json.load(file)
                if user_id:
                    item_list = [item for item in all_items if str(item["id"]) == str(user_id)]
                else:
                    item_list = all_items
                if user_id and not item_list:
                    error = "Product not found."

        elif source == "csv":
            with open("products.csv", "r") as file:
                reader = csv.DictReader(file)
                if user_id:
                    item_list = [row for row in reader if row.get("id") == str(user_id)]
                else:
                    item_list = list(reader)
                if user_id and not item_list:
                    error = "Product not found."

        else:
            error = "Wrong source"

    except Exception as e:
        error = "Error reading file: " + str(e)

    return render_template("product_display.html", items=item_list), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)
