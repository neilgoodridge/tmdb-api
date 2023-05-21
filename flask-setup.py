import os


def create_flask_app(app_name):
    os.makedirs(f"{app_name}/static/css", exist_ok=True)
    os.makedirs(f"{app_name}/static/js", exist_ok=True)
    os.makedirs(f"{app_name}/templates", exist_ok=True)

    with open(f"{app_name}/app.py", "w") as app_file:
        app_file.write('''from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
''')

    with open(f"{app_name}/templates/index.html", "w") as index_file:
        index_file.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Flask App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
    <h1>Welcome to My Flask App!</h1>
</body>
</html>
''')

    with open(f"{app_name}/static/css/main.css", "w") as css_file:
        css_file.write('''body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 0;
}

h1 {
    text-align: center;
    color: #333;
}
''')

    with open(f"{app_name}/static/js/main.js", "w") as js_file:
        js_file.write('''function myFunction() {
    let text="Choose a button!";
    if (confirm(text) == true) {
        text="You pressed OK! JavaScript confirmed as working.";
    } else {
        text="You cancelled! JavaScript confirmed as working.";
    }
    document.getElementById("demo").innerHTML = text;
}''')


if __name__ == "__main__":
    app_name = input("Enter the name of your Flask app: ")
    create_flask_app(app_name)
    print(f"Flask app '{app_name}' created successfully!")
