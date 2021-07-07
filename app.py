# Building Flask general app
from flask import Flask, render_template
import numpy
import pandas as pd
from SQLquerying import last_tendata
from SQLquerying import check_anamoly
from Send_notification import send_msg

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=["GET", "POST"])
def main_type():
    #Get the most recent 10 data values from the SQL database
    datas = last_tendata()
    #Sending email to the required authorities
    send_msg()
    return render_template('index.html', datas=datas)


@app.route('/about.html')
def about():
    #Simple about page
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
