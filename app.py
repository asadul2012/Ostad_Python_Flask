from flask import Flask, request, render_template, jsonify
import requests


app = Flask(__name__)



@app.route("/")
def homepage():
    return "Welcome to Flask";



@app.route("/hello")
def hello():
    return "Hello World";



@app.route("/project")
@app.route("/project/flask")
def project():
    return "Flask is a python web framework";



@app.route("/user")
@app.route("/user/<name>")
def user(name="Guest"):
    return f"Hello {name}";



@app.route("/posts/<int:post_id>/comments/<int:comment_id>")
def posts(post_id, comment_id):
    return f"Posts ID: {post_id}, Comments ID: {comment_id}"



@app.route("/welcome")
def welcome():
   extra = "Wow, The Flask is easy!!"
   x = 19
   languages = ["Python", "Ruby", "C++", "C", "Javascript", "Go", "Java"]
   return render_template('index.html', info = extra, b = x, languages = languages)




@app.route("/login", methods = ["GET", "POST"])
def login():
    error = True
    if request.method == "POST":
        # username = request.form['username']
        username = request.form.get('username')
        password = request.form.get('password')

        # return(f" This is a post with username: { username }")
        # return(f" This is a post with username/password: { username, password }")

        if username == 'admin' and password == 'admin':
            error = False
            return render_template('login.html', username = username, error = error)
        else:
            error = True
            return render_template('login.html', error = error)
    
    return render_template("login.html")




@app.route("/api/countries")
def countries():
    countries = ["Bangladesh", "USA", "UK", "Japan"]
    return jsonify({"countries":countries})



@app.route("/api/person")
def person():
    person = {
        "name": "asad",
        "age": 35,
        "city": "Dhaka"
    }
    return jsonify(person)



@app.route("/all_posts")
def all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    return jsonify(data)



@app.route("/all_posts/<int:post_id>")
def single_posts(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    data = response.json()
    return jsonify(data)




if __name__ == "__main__":
    app.run(debug=True)