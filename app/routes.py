# Authors: CS For Insight (Summer19 - JG)

try:
    from flask import render_template, redirect, url_for, request, send_from_directory, flash, json
except:
    print("Not able to import all of the calls needed from the Flask library.")

from crypt import methods
from sympy import python
from app import app
import os
import multiline
import ast
from bs4 import BeautifulSoup #allows us to trun html string into an html document

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for


try:
    from PIL import Image
    import PIL.ImageOps
except:
    print("Make sure to pip install Pillow")

from app import pythonfunctions  # our Python functions are in pythonfunctions.py
from app import brehfunction

#***************************JavaScript
@app.route('/aceExample') 
def aceExample():
    return render_template('aceExample.html')

@app.route('/aceExample.js') #allows us to use the ace editor
def aceExample1():
    return render_template('aceExample.js')


@app.route('/aceTheme.js') #allows us to set the theme of our text box to twilight
def aceExample3():
    return render_template('aceTheme.js')



@app.route('/script.js') #js for the front end functionality of Mudd Bat
def script():
    return render_template('script.js')

@app.route('/ace.js') #js for the textbox using the ace library
def script1():
    return render_template('ace.js')


@app.route('/javaHighlighter.js') #js for the textbox to be highlighted with python syntax
def script4():
    return render_template('javaHighlight.js')

@app.route('/pyMode.js') #js for the textbox to be highlighted with python syntax
def script2():
    return render_template('pyMode.js')

#****************************************CSS
@app.route('/css') #js for the textbox to be highlighted with python syntax
def css():
    return render_template('cssstyleexample.css')


# Home page, renders the index.html template

@app.route('/index', methods=['GET', 'POST'])
@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        submit = request.form['btnSubmit']
        print("submit value is: ", submit)
        data = request.form['data']
        print("the data is: ", data)
        # with open("jacoby.html", "w") as fo:
        #     # fo.write(data)
        #     fo.write("hello world") 
        with open("/Users/jacobylockman/Desktop/week2_spr22/FlaskAppStarter/app/templates/jacoby.html", "w") as test:
            test.write('{% extends "base.html" %}\n{% block content %}')
            test.write("<div class='test'><b><center><div id='testName'>{{submit}}</div></center></b></div>")
            test.write(data)
            test.write('{% endblock %}')
            test.close()

        return render_template('jacoby.html', submit=submit)
    return render_template('index.html', title='Home')

# Pig latin page, when we click translate, moves to text result page
@app.route('/text',methods=['GET','POST'])
def text():
    if request.method == 'POST':
        old_text = request.form['text']
        new_text = pythonfunctions.pig_translate(old_text)
        return render_template('textResults.html', old_text=old_text, new_text=new_text)
    return render_template('text.html', title='Home')

#breh latin page
@app.route('/breh',methods=['GET','POST'])
def breh():
    if request.method == 'POST':
        old = request.form['text']
        new = brehfunction.breh_translator(old)
        return render_template('brehResults.html', old=old, new=new)
    return render_template('breh.html', title='Home')
#determinant calculator page
@app.route('/determinant',methods=['GET','POST'])
def determinant():
    if request.method == 'POST':
        one_one = request.form['one_one']
        one_two = request.form['one_two']
        two_one = request.form['two_one']
        two_two = request.form['two_two']
        det = pythonfunctions.determinant(one_one, one_two, two_one, two_two)
        return render_template('determinantResults.html', det=det)
    return render_template('determinant.html', title='Home')

#loopquiz route
@app.route("/loopquiz")
def loopquiz():
    return render_template('loopquiz.html', title='Home')

#Front-button page
@app.route("/Front-button.html")
def Front_button():
    return render_template('Front-button.html', title='Home')

#program to int
@app.route("/string_to_int.html",methods=['GET','POST'])
def stringToInt():
    if request.method == 'POST':
        text = request.form['text']
        int = pythonfunctions.stringToInt(text)
        return render_template('string_to_int_Results.html', text=text, int=int)
    return render_template('string_to_int.html', title='Home')
#int to program
@app.route("/int_to_string.html",methods=['GET','POST'])
def intToString():
    if request.method == 'POST':
        num = request.form['num']
        s = pythonfunctions.newDeciInput(num)
        return render_template('int_to_string_Results.html', num=num, s=s)
    return render_template('int_to_string.html', title='Home')

@app.route("/test.html")
def testFunction():
    return render_template('test.html', title= 'Home')

# @app.route("/jsAndFetchEx.html")
# def jsAndFetchEx():
#     return render_template('jsAndFetchEx.html', title = 'Home')


@app.route("/jsAndFetchEx.html", methods=['GET','POST'])
def jsAndFetchEx():
    if request.method == 'POST':
        old_text = request.form['king']
        # new_text = pythonfunctions.pig_translate(old_text)
        return old_text + "jacoby"
    # if request.method == 'POST':
    #     # xValue = request.form('xValue')
    #     # yValue = request.form('yValue')
    #     # output = pythonfunctions.jsAndFetchEx(xValue,yValue)
    #     melon = request.form('test1')
    #     return render_template('donkey.html', melon=melon)
    return render_template('jsAndFetchEx.html', title='Home')
        
# this is a test to try and recieve data from the server and put it on the txt file
# with open("//Users//jacobylockman//Desktop//week2_spr22//FlaskAppStarter//app//static//fetchResultsEx.txt", "w")as e:
#     if request == 'POST':
#         xValue = request.form('xValue')
#         yValue = request.form('yValue')
#         output = pythonfunctions.jsAndFetchEx(xValue,yValue)
#         # return render_template('jsAndFetchEx.txt', output=output)
#     e.write(output)

# @app.route("/cool")
# def cool():
#     return "cool"

@app.route("/dynamicAddCol", methods=['GET', 'POST'])
def tableSandbox1():
    return render_template('dynamicAddCol.html', title='Home')

@app.route("/tableSandbox", methods=['GET', 'POST'])
def tableSandbox():
    return render_template('tableSandbox.html', title='Home')

#this is the url that is being fetched for the fetch example page
@app.route("/idk", methods=['GET','POST'])
def joe():
    if request.method == 'POST':
        input1 = request.form['test1']
        input2 = request.form['test2']
        output = pythonfunctions.jsAndFetchEx(input1, input2)
        # new_text = pythonfunctions.pig_translate(old_text)
        return output
    return "this didn't get the post"
    # return render_template('donkey.html') #in the front end fetch ...../idk
#MuddBat
@app.route("/mango", methods=['GET', 'POST'])
def fruit():
    return render_template('prototype.html', title='Home')
    # return "mango"

@app.route("/mango1", methods=['GET', 'POST'])
def fruit1():
    if request.method =='POST':
        output = request.form['text']
        # list=[]
        # inlist= list.extend([request.form['one'], request.form['two'], request.form['three'], request.form['four'], request.form['five']])
        # # inlist = [1,2,3,4,5]
        # newlist = list.append(request.form['one'])
        # newnewlist= list.append(request.form['two'])
        # test = list.append(request.form['one'])
        test1 = request.form['one']
        test2 = pythonfunctions.myAppend([],test1)
        test3 = pythonfunctions.myAppend(test2, request.form['two'])
        test4 = pythonfunctions.myAppend(test3, request.form['three'])
        test5 = pythonfunctions.myAppend(test4, request.form['four'])
        test6 = pythonfunctions.myAppend(test5, request.form['five']) # this list will be passed as a string accross the wire, the elements will also be string because request.form passes data over the wire
        result = pythonfunctions.compEx5(output, test6)
        result = pythonfunctions.compEx5(output, test3)

        # result = pythonfunctions.compEx3(output, inlist)
        return jsonify(result)
        # return jsonify(str(result))
    return "this didn't work"

@app.route("/asyncPract", methods=['GET', 'POST'])
def practice():
    return render_template('asyncPract.html', title='Home')

@app.route("/fetchDiff", methods=['GET', 'POST'])
def asdf():
    return render_template('FetchDiffDicts.html', title='Home')

@app.route("/fetchDiff1", methods=['GET', 'POST'])
def asdfa():
    return render_template('FetchDiffDicts1.html', title='Home')

@app.route("/fetchDiff2", methods=['GET', 'POST'])
def asdfaa():
    return render_template('FetchDiffDicts2.html', title='Home')

@app.route("/fetchDiff3", methods=['GET', 'POST'])
def asdfaaa():
    if request.method == 'POST':
        add = request.form['back'] #the form data that we want to updat the incoming json with.
        test = request.form['json'] # gets the form data which is the string of a json object
        testj = json.loads(test) # converts from a string into an actual dictionary
        outputList = testj['expected'] #notation for accessing key value pairs in the dict
        if add == '': #if/else statements handle the case when nothing is submitted, we keep the value as an empty list
            return str(testj)
        else:
            outputList.append(add) #append add into list which is the value for the key 'expected'
            return str(testj) 
    return "This didn't post"

@app.route("/fetchDiff4", methods=['GET', 'POST'])
def asdfaaaa():
    return render_template('FetchDiffDicts4.html', title='Home')

@app.route("/fetchDiff5", methods=['GET', 'POST'])
def asdfaaaaa():
    return render_template('FetchDiffDicts5.html', title='Home')


@app.route("/banana", methods=['GET', 'POST'])
def fruit2():
    return render_template('twoInput.html', title='Home')
    # return "mango"

@app.route("/banana1", methods=['GET', 'POST'])
def fruit3():
    if request.method =='POST':
        output = request.form['text']
        test1 = request.form['one']
        test2 = pythonfunctions.myAppend([],test1)
        test3 = pythonfunctions.myAppend(test2, request.form['two'])
        test4 = pythonfunctions.myAppend(test3, request.form['three'])
        test5 = pythonfunctions.myAppend(test4, request.form['four'])
        test6 = pythonfunctions.myAppend(test5, request.form['five']) # this list will be passed as a string accross the wire, the elements will also be string because request.form passes data over the wire
        result = pythonfunctions.compEx5(output, test6) #we can't return this dictionary because the keys are tuples
        newresult = pythonfunctions.specialSauce(str(result)) #special suace just puts it into the form of a workable json object

        # result = pythonfunctions.compEx3(output, inlist)
        return jsonify(newresult)
        # return jsonify(str(newresult))
        # return jsonify(str(result))
        # return str(test5)

    return "this didn't work"

@app.route("/banana3", methods=['GET', 'POST'])
def fruit4():
    return render_template('twoInput1.html', title='Home')

@app.route("/banana4", methods=['GET', 'POST'])
def fruit5():
    if request.method =='POST':
        output = request.form['text']
        test1 = request.form['one1']
        test2 = pythonfunctions.myAppend([],test1)
        test3 = pythonfunctions.myAppend(test2, request.form['two1'])
        test4 = pythonfunctions.myAppend(test3, request.form['three1'])
        test5 = pythonfunctions.myAppend(test4, request.form['four1'])
        test6 = pythonfunctions.myAppend(test5, request.form['five1']) # this list will be passed as a string accross the wire, the elements will also be string because request.form passes data over the wire
        result = pythonfunctions.compEx5(output, test6) #we can't return this dictionary because the keys are tuples
        testresult = pythonfunctions.dictHelper(str(result))
        newresult = pythonfunctions.specialSauce1(testresult)

        test = "data: [" + str(result) + "]"

        # result = pythonfunctions.compEx3(output, inlist)
        # return jsonify(newresult)
        # return str(testresult)
        return jsonify(newresult)
    return "This didn't work"

@app.route("/banana5", methods=['GET', 'POST'])
def fruit6():
    return render_template('twoInput2.html', title='Home')

@app.route("/banana6", methods=['GET', 'POST'])
def fruit7():
    return render_template('muddBat.json', title='Home')

@app.route("/banana7", methods=['GET', 'POST'])
def fruit8():
    return render_template('twoInput4.html', title='Home')

@app.route("/banana8", methods=['GET', 'POST'])
def fruit9():
    # if request.method == 'POST':
    #     o = request.form['input1']
    #     return render_template('muddBat1.json' + 'o')
    return render_template('muddBat2.json', title='Home')

#page that holds the json data sent to the back end
@app.route("/banana9", methods=['GET', 'POST'])
def fruit10():
    if request.method == 'POST':
        test = request.form['json'] # gets the form data which is the string of a json object
        testj = json.loads(test) # converts from a string into an actual dictionary
        problemName = request.form['problemName'] #accesses the name of the problem
        userFunct = request.form['text']#gets the user's code that they input to solve the problem
        errString = testj[problemName]['error']

        print("the UserFunct is: *******************************************************************************************************", userFunct)

        if userFunct == "":
            errString.append("Please type into the text box.")
            return ast.literal_eval(str(testj))
        if "eval()" or "exec()" in userFunct:
            errString.append("Code can not contain eval() or exec()")
            return ast.literal_eval(str(testj))
        try:
            exec(userFunct)

        except SyntaxError as err:
            # print(err.lineno)
            # print(err)
            # print(dir(err))
            # print("the text is: ", err.text)
            # print("the message is: ", err.msg)
            errString.append(err.msg + " on line " + str(err.lineno))
            print("the json data is : ", ast.literal_eval(str(testj)))
            return ast.literal_eval(str(testj))


        except Exception as logicErr:
            print("this is the logicErr: ", logicErr)
            print(str(type(logicErr)) + " " +  str(logicErr))

            errString.append(str(type(logicErr)) + " " + str(logicErr))
            print(ast.literal_eval(str(testj)))
            return ast.literal_eval(str(testj))
        

        exec(userFunct)#compiles the user's code so that we can evaluate it when pluggin
        userFunctName = pythonfunctions.functFinder(userFunct) #gets the name of the user's function
        
        print("this is testj: ", testj)
        print("this is a test: ", testj['TwoInput']['correctFunc'])
        correctFunc = testj[problemName]['correctFunc'] #the code for the correct function
        exec(correctFunc) #compiles the code so that we can evaluate it when plugging input values into it.
        outList = testj[problemName]['out']
        expected = testj[problemName]['expected'] #the list that we will add the expected values to.
        inList = testj[problemName]['in'] #list of strings of the inputs
        correctFunctName = pythonfunctions.functFinder(correctFunc) #finds the name of the function so we can concatenate it with inputs and eval!!!
        newUserFunc = pythonfunctions.extraTab(userFunct) #puts an extra 4 spaces (a tab) wherever there is a new line in a string in order
                                                        #to correctly format the userFunct for running it through the following try and excepts
        for i in inList: #iterates through all the inputs and evaluates them with the correct function and the user's function. then it store these values in the expected
            expectedOut = eval(correctFunctName + i)
            expected.append(expectedOut)
            a = '''def bad(x): 
            return bad(x + 1)'''
            print("---------------------", a)
            print(a == userFunct)
            try:
                # print("hello")
                print("----------------------", newUserFunc)
                s =f"""
def fruit10():
    {newUserFunc}
    return {userFunctName + i}
fruit10()"""
                print("++++++++++++++++++++++++++++++", s)
                exec(s)
            except Exception as e:
                print("__________________________________", e)
                errString.append(str(e))
                return ast.literal_eval(str(testj))


            userOut = eval(userFunctName + i)
            outList.append(userOut)
        
        return ast.literal_eval(str(testj))

    return "This didn't post"
#address for muddBat6
@app.route("/banana10", methods=['GET', 'POST']) #work on fixing the action buttons on index
def fruit11():
    if request.method == 'POST':
        data = request.form['data']
        htmlData = BeautifulSoup(data)
        print("the Data is: ", data)
        print("the html data is: ", htmlData.get_text())
        
        # return htmlData.get_text()
        return data

    return "This didn't work"

#page to create your own problem
@app.route("/banana11", methods=['GET', 'POST']) #work on fixing the action buttons on index
def fruit12():
    if request.method == 'POST':
        return 
    return render_template('create.html')

    

@app.route("/jacoby", methods=['GET','POST'])
def jl():
    # if request == 'POST':
    #     xValue = request.form('xValue')
    #     yValue = request.form('yValue')
    #     output = pythonfunctions.jsAndFetchEx(xValue,yValue)
    #     return output
    # dog = request.args
    # cat = dog['test1']
    # mouse = dog['test2']
    # return mouse + cat
    

    # d = { "king": 42, "jacoby": 9001}
    d = request.args
    result_of_d_of_a = d['a']
    result_of_d_of_b = d['b']
    return str( result_of_d_of_a + "Hi Jacoby!" + result_of_d_of_b )
   


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

# Used for uploading pictures
@app.route('/<filename>')
def get_file(filename):
    return send_from_directory('static',filename)


# Image uploading page, 
@app.route('/image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # if the image is valid, do the following
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Create a path to the image in the upload folder, save the upload
            # file to this path
            save_old=(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(save_old)
            # Take the image, make a new one that is inverted
            img = Image.open(save_old)
            rbg_img = img.convert('RGB')
            inverted_image = PIL.ImageOps.invert(rbg_img)
            save_new=(os.path.join(app.config['UPLOAD_FOLDER'], 'new_'+filename))
            inverted_image.save(save_new)
            # Render template with inverted picture
            rt = render_template('imageResults.html', filename='new_'+filename)
            return rt
    return render_template('image.html')

# allowed image types 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['ALLOWED_EXTENSIONS']=ALLOWED_EXTENSIONS

# is file allowed to be uploaded?
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']