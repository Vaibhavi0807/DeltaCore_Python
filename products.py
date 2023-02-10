from flask import Flask, render_template

app = Flask(__name__)

@app.route('/products')
def products():
    products = [
        {
            'Product Id': 1001,
            'Name': 'Tools Gears',
            'Description': 'Gear tools production specification'
        },
        {
            'Product Id': 1002,
            'Name': 'Panels',
            'Description': 'Switch Gear Panels'
        },
        {
            'Product Id': 1003,
            'Name': 'DocTonar',
            'Description': 'Document Solar Objects'
        }
    ]
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run()
