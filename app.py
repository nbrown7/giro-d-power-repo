from power import *
from flask import Flask, render_template

app = Flask(__name__)

#default value for numMin
numMin = 20

#default value for file
fileName = "FTP_TEST.CSV"

data = calculateXMinPower(numMin, fileName)

#route for front page
@app.route("/")
def main():
    return render_template("index.html")
    
#route for power calculation
@app.route("/power")
def power():
    return render_template("power.html", dataList = data)
