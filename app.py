from flask import Flask,render_template
from models import db

app = Flask(__name__)

#Configue the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

# Intialize the database with the Flask app
db.init_app(app)

# Home route just to test if app runs

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    print("✅ Starting the Flask server...")
    app.run(debug=True)