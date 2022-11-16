import numpy as np
from flask import Flask,render_template,request
import pickle


app = Flask(__name__)
model = pickle.load(open('wqi.pkl','rb'))
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/')
def home() :
    return render_template("predict.html")
@app.route('/bod')
def bod():
    return render_template("bod.html")
@app.route('/col')
def col():
    return render_template("col.html")
@app.route('/do')
def do():
    return render_template("do.html")
@app.route('/nit')
def nit():
    return render_template("nit.html")
@app.route('/ph')
def ph():
    return render_template("ph.html")
@app.route('/cond')
def cond():
    return render_template("cond.html")
@app.route('/analysis')
def analysis():
    return render_template("analysis.html")
@app.route('/login',methods = ['POST'])
def login() :
    year = request.form["year"]
    do = request.form["do"]
    ph = request.form["ph"]
    co = request.form["co"]
    bod = request.form["bod"]
    na = request.form["na"]
    tc = request.form["tc"]
    total = [[int(year),float(do),float(ph),float(co),float(bod),float(na),float(tc)]]
    y_pred = model.predict(total)
    print(y_pred)
    y_pred =y_pred[[0]]
    if(y_pred >= 95 and y_pred <= 100) :
        return render_template("predict.html",showcase = 'Excellent,The predicted value is '+ str(y_pred)+' No Purification or Treatment of Water is needed.')
    elif(y_pred >= 89 and y_pred <= 94) :
        return render_template("predict.html",showcase = 'Very good,The predicted value is '+str(y_pred)+' Minor Purification or Treatment of Water is needed.')
    elif(y_pred >= 80 and y_pred <= 88) :
        return render_template("predict.html",showcase = 'Good,The predicted value is'+str(y_pred)+' Conventional Purification or Treatment of Water is needed.')
    elif(y_pred >= 65 and y_pred <= 79) :
        return render_template("predict.html",showcase = 'Fair,The predicted value is '+str(y_pred)+' Extensive Purification or Treatment of Water is needed.')
    elif(y_pred >= 45 and y_pred <= 64) :
        return render_template("predict.html",showcase = 'Marginal,The predicted value is '+str(y_pred)+' Doubtful in purifying and treating the water so as to get Pure Water.')
    else :
        return render_template("predict.html",showcase = 'Poor,The predicted value is '+str(y_pred)+' The Water is not fit for to be used for Drinking.')
    
    
if __name__ == '__main__' :
    app.run()