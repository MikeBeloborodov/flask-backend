from flask import Flask, render_template
import sqlite3
import templates

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/products")
def products():
    products = get_products()
    products_json = turn_into_json(products)
    return render_template('products.html', content=products_json)

def turn_into_json(products: list) -> dict:
    json_dict = {}
    for product in products:
        json_dict.update({product[0] : {
                                        "description" : product[1],
                                        "new_price" : product[2],
                                        "old_price" : product[3],
                                        "discount" : product[4]
                                        }})
    return json_dict

def get_products() -> list:
    connection = sqlite3.connect('content.db')
    cursor = connection.cursor()
    cursor.execute("""
            SELECT rowid, *
            FROM discounts
    """)
    products = cursor.fetchall()
    return products