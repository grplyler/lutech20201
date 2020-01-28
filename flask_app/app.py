from flask import Flask, escape, request, render_template

app = Flask(__name__)


# Home Page
@app.route('/')
def index():
    return render_template('index.html')


# Calculator Form Page
@app.route('/calc', methods=['GET'])
def calc():
    return render_template('calc.html')

# Calculator Reults Page
@app.route('/calc', methods=['POST'])
def calc_results():

    # Perform Loan Calculation
    years = int(request.form['years'])
    n = years * 12
    interest = float(request.form['interest'])
    i = interest / 12
    PVa = int(request.form['present_value'])


    monthly_payment = (i * PVa) / (1 - pow(1+i, -n))
    monthly_payment = "{:.2f}".format(monthly_payment)

    # Results
    results = {
        PVa: PVa,
        interest: interest,
        years: years,
        monthly_payment: monthly_payment
    }

    return render_template('calc_results.html', monthly_payment=monthly_payment)

if __name__ == "__main__":
    app.run(debug=True)