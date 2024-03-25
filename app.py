import os
from numberFile import number
from flask import Flask,render_template,request
from tracker import track_number

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
# app=Flask(__name__)
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
# tracker route
@app.route('/tracknumber.html',methods=['GET','POST'])
def tracker_route():
    num = "+254745567568"
    if request.method =='POST':
        num2=request.form.get('num') 
        print(num2)
    else:
        print("Can't fetch num")
    # initiate num value
    # swap num value with the user input value
    num,num2=num2,num
    print(num2)
    print(num)
    country, Service_provider = track_number(num)
    return render_template("tracknumber.html", num=num, country=country, Service_provider=Service_provider)
if __name__=="__main__":
    app.run(debug=True)