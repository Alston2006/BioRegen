from flask import Flask,render_template,request,redirect,url_for

'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template('home_pg.html')


@app.route("/busdashboard.html")
def josh():
    return render_template('busdashboard.html')
@app.route("/activities")
def reward():
    return render_template('inddashboard.html')

"""@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')"""

@app.route('/submit',methods=['GET','POST'])
def submit():
    
    if request.method=='POST':
        email=request.form['email']
        m=str(email)
        password=request.form['password']
        return f'Hello {email}!'
    return render_template('LL.html')

 #<input type="text" id="name" name="name">
 #<input type="submit" value="Submit">




@app.route("/signin.html")
def index():
    return render_template('signin.html')

@app.route("/login.html")
def about():
    return render_template('login.html')
@app.route("/rewards")
def rewardss():
    return render_template('benefits.html')
@app.route("/inddashboard.html")
def rew():
    return render_template('inddashboard.html')                                                              

if __name__=="__main__":
    app.run(debug=True)              #/inddashboard.html