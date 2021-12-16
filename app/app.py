""" Flask web app """
from flask import Flask, request, render_template, flash
from calc.calculator import Calculator

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    """ index route response """
    return render_template('index.html')


@app.route("/basicform", methods=['GET', 'POST'])
def basicform():
    """ POST request handler """
    if request.method == 'POST':
        # get the values out of the form
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        # make the tuple
        my_tuple = (value1, value2)
        # this will call the correct operation
        getattr(Calculator, operation)(my_tuple)
        result = str(Calculator.get_last_result_value())
        if result == 'error':
            flash("Cannot divide by zero!")
            return render_template('basicform.html')
        return render_template('result.html', value1=value1, value2=value2,
                               operation=operation, result=result)
    # Displays the form because if it isn't a post it is a get request
    return render_template('basicform.html')


@app.route("/calculator", methods=['GET'])
def calculator_get():
    """ GET handler for csv-based calculator """
    return render_template('calculator.html')


@app.route("/calculator", methods=['POST'])
def calculator_post():
    """ POST handler for csv-based calculator """



@app.route("/tabledemo")
def tabledemo():
    """ tabledemo route response """
    return render_template('tabledemo.html')


@app.route("/api/demodata")
def demodata():
    """ tabledemo json data api endpoint """
    return {'data': [
        {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        },
        {
            "brand": "Chevy",
            "model": "Camaro",
            "year": 1967
        },
        {
            "brand": "Toyota",
            "model": "Tacoma",
            "year": 2021
        }
    ]}


@app.route("/bad/<value1>/<value2>")
def bad_calc(value1, value2):
    """ bad calculation route response """
    result = value1 + value2
    response = "The result of the calculation is: " + result + '<a href="/"> back</a>'
    return response


@app.route("/good/<float:value1>/<float:value2>")
def good_calc(value1, value2):
    """ good calculation route response"""
    my_tuple = (value1, value2)
    Calculator.add_numbers(my_tuple)
    response = "The result of the calculation is: " + \
               str(Calculator.get_last_result_value()) + \
               '<a href="/"> back</a>'
    return response
