from flask import Flask,render_template
app=Flask(__name__, static_folder='static')
@app.route('/')
def index1():
    return render_template("index.html")
#index route
@app.route('/index.html')
def index():
    return render_template("index.html")
#home route
@app.route('/home.html')
def home():
    return render_template("home.html")
#about route
@app.route('/about.html')
def about():
    return render_template("about.html")
#contacts route
@app.route('/contact.html')
def contact():
    return render_template("contact.html")
if __name__=="__main__":
    app.run(debug=True)