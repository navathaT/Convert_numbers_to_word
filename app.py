from flask import Flask, request
from converter import converter   # ✅ import your existing function

app = Flask(__name__)

@app.route("/")
def home():
    return "Number to Word API is running!"

@app.route("/convert")
def convert_number():
    number = request.args.get("number")

    if not number:
        return "Please provide a number like ?number=123", 400

    try:
        int(number)  # validate input
        result = converter(number)
        return f"{number} --> {result}"
    except ValueError:
        return "Invalid number!", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
