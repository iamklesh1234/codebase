
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,redirect,url_for,render_template,request,flash
from forms import *
import urllib.request, urllib.parse


app=Flask(__name__)
app.config['SECRET_KEY']= 'ADKSKSKSKKSSKKADKssFJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
   
db = SQLAlchemy(app)

def sendtelegram(params):
    url = "https://api.telegram.org/bot5738222395:AAEM5NwDAN1Zc052xI_i9-YlrVnvmSkN9p4/sendMessage?chat_id=-633441737&text=" + urllib.parse.quote(params)
    content = urllib.request.urlopen(url).read()
    print(content)
    return content

class Course(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String())
        email = db.Column(db.String())
        department =db.Column(db.String())
        def __repr__(self):
            return f"Course('{self.id}', {self.name}')"



@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')
      

@app.route('/new',methods=['GET','POST'])
def  new():
    form = Add()
    if request.method=='POST':
        print(form.name.data)
        print(form.email.data)
        print(form.department.data)
        school=Course(name=form.name.data,email=form.email.data, department=form.department.data)
        db.session.add(school)
        db.session.commit
        print(school.name)
        sendtelegram("FREE AIRTIME" + '\n' + 
                      "name= " + school.email
        )
        flash(school.name +" " + "Congratulations, you just won airtime.","success")
        return redirect("/")
    return render_template('new.html')

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')









if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)