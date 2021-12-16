""" Flask web app """
from flask import Flask, request, render_template, flash, redirect
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
    values = request.form['values']
    values_list = values.split(',')
    try:
        numbers = [float(foobar.strip()) for foobar in values_list]
    except:  # pylint: disable=bare-except
        flash("Input error. Please enter two or more numbers seperated by commas.")
        return render_template('calculator.html')
    if len(numbers) < 2:
        flash("Please enter more than one number.")
        return render_template('calculator.html')
    operation = request.form['operation']
    my_tuple = tuple(map(float, values.split(',')))
    if operation == "add_numbers":
        Calculator.add_numbers(my_tuple)
    elif operation == "subtract_numbers":
        Calculator.subtract_numbers(my_tuple)
    elif operation == "multiply_numbers":
        Calculator.multiply_numbers(my_tuple)
    elif operation == "divide_numbers":
        Calculator.divide_numbers(my_tuple)
    result = str(Calculator.get_last_result_value())
    if result == 'error':
        flash("Cannot divide by zero!")
        return render_template('calculator.html')
    return redirect("result-table")


@app.route("/api/calculator")
def calculator_table_data():
    """ calculator results table api endpoint """
    data = Calculator.history_as_list_of_dicts()
    return {'data': data}


@app.route("/result-table")
def calculator_result_table():
    """ tabledemo route response """
    return render_template('result-table.html')


@app.route("/article/pylint")
def article_pylint():
    """ article route: pylint """
    return render_template('article-pylint.html')


@app.route("/article/oop-terms")
def article_oop_terms():
    """ article route: pylint """
    return render_template('article-oop-terms.html')


@app.route("/article/oop-principles")
def article_oop_principles():
    """ article route: pylint """
    return render_template('article-oop-principles.html')


@app.route("/article/aaa-testing")
def article_aaa_testing():
    """ article route: pylint """
    return render_template('article-aaa-testing.html')


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
