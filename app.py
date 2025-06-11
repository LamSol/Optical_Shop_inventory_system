from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    print("✅ Starting the Flask server...")
    app.run(debug=True)