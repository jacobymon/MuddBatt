
try:
    from flask import render_template, redirect, url_for, request, send_from_directory, flash
except:
    print("Not able to import all of the calls needed from the Flask library.")

from sympy import python
from app import app
import os

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

try:
    from PIL import Image
    import PIL.ImageOps
except:
    print("Make sure to pip install Pillow")

from app import pythonfunctions  # our Python functions are in pythonfunctions.py
from app import brehfunction

@app.route("/jacoby")
def jl():
    return "Hi from Jacoby!!!!"

@app.route("/jsAndFetchEx.txt")
def jsAndFetchE():
    if request == 'POST':
        xValue = request.form('xValue')
        yValue = request.form('yValue')
        output = pythonfunctions.jsAndFetchEx(xValue,yValue)
        return render_template('jsAndFetchEx.txt', output=output)
    # return render_template('jsAndFetchEx.html', title='Home')

#this is a test to try and recieve data from the server and put it on the 
with open("//Users//jacobylockman//Desktop//week2_spr22//FlaskAppStarter//app//static//fetchResultsEx.txt", "w")as e:
    if request == 'POST':
        xValue = request.form('xValue')
        yValue = request.form('yValue')
        output = pythonfunctions.jsAndFetchEx(xValue,yValue)
        # return render_template('jsAndFetchEx.txt', output=output)
    e.write(output)
    


# Substitutions page, when we click submit, it substitutes!
@app.route('/subs',methods=['GET','POST'])
def subs():
    if request.method == 'POST':
        # larger textarea
        old_textarea = request.form['textarea_input']
        # old words and new words (their replacements)
        old_word1 = request.form['original_text1']
        old_word2 = request.form['original_text2']
        old_word3 = request.form['original_text3']
        new_word1 = request.form['replacement_text1']
        new_word2 = request.form['replacement_text2']
        new_word3 = request.form['replacement_text3']
        # create a dictionary of substitutions
        substitutions = {}
        substitutions[old_word1] = new_word1
        substitutions[old_word2] = new_word2
        substitutions[old_word3] = new_word3
        # do the transformation in Python
        new_text = pythonfunctions.substitute(old_textarea, substitutions)
        return render_template('subsResults.html', 
                                old_text=old_textarea, 
                                new_text=new_text)
    else:
        return render_template('subs.html', title='Home')
    