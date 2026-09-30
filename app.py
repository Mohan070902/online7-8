from flask import Flask, render_template, request, redirect, url_for, session, make_response
import jwt

app = Flask(__name__)

SECRET_KEY = "my-secret-key"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login", methods=["POST"]) 
def login(): 
 
    username = request.form["username"] 
    password = request.form["password"] 
 
    if username == "Mohan" and password == "1234": 
 
        token = jwt.encode({"user_id": 1,
                            "username": "Mohan",
                            "password" : 1234}, 
                            SECRET_KEY, 
                            algorithm="HS256") 
 
        return { 
            "message": "Login Successful", 
            "token": token 
        } 
 
    return { 
        "message": "Invalid Login" 
    }, 401


if __name__ == "__main__":
    app.run(debug=True)