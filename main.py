from flask import Flask, render_template, request
from fake_data import generate_data
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_fake_data():
    get_numb_rows = request.form.get('numRows')
    get_fields = request.form.getlist('fields')
    
    fix_file = generate_data(get_fields, get_numb_rows)
    filename_fix = os.path.basename(fix_file)
    return render_template('index.html', fix_file=filename_fix)


if __name__ == '__main__':
    app.run(debug=True, port=9078)