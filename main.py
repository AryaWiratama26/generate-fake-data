from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_fake_data():
    get_numb_rows = request.form.get('numRows')
    get_fields = request.form.getlist('fields')
    
    return f"Jumlah Data : {get_numb_rows}, {get_fields}"


if __name__ == '__main__':
    app.run(debug=True, port=9078)