
from flask import request
from app import pythonfunctions

@app.route('/jsAndFetchEx.html', methods=['GET', 'POST'])
def fetchFunct():
    xValue = request.form('xValue')
    yValue = request.form('yValue')
    print(xValue)
    output = pythonfunctions.jsAndFetchEx(xValue,yValue)
    #     with open("//Users//jacobylockman//Desktop//week2_spr22//FlaskAppStarter//app//static//fetchResultsEx.txt", "w")as e:
    #         e.write(output)
    # return "test"