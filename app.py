from flask import Flask, render_template
from api_key import API_KEY

api_key = {API_KEY}
# print(api_key)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
