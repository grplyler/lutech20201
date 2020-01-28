from flask import Flask, escape, request, render_template


# Create Flask App
app = Flask(__name__)


# Home Page
@app.route('/')
def index():
    return render_template('index.html')


# Calculator Form Page
@app.route('/calc', methods=['GET'])
def calc():
    return render_template('calc.html')


if __name__ == "__main__":
    app.run(debug=True)