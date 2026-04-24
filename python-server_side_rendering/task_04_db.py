#!/usr/bin/python3

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def read_csv(filepath):
    products = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # This allows us to access columns by name like a dictionary
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')
            
        rows = cursor.fetchall()
        # Convert sqlite3.Row objects to standard dictionaries
        products = [dict(row) for row in rows]
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # 1. Validate Source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Fetch Data
    products = []
    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    elif source == 'sql':
        products = read_sql()
        if products is None:
            return render_template('product_display.html', error="Database error")

    # 3. Filter by ID (for JSON and CSV, SQL does this during fetch)
    if product_id:
        try:
            pid = int(product_id)
            if source == 'sql':
                # Re-fetch specific ID for SQL to demonstrate DB filtering
                products = read_sql(pid)
            else:
                products = [p for p in products if p['id'] == pid]
                
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
