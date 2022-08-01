# Starting code for our Flask web application

#
# Name(s):
#

from curses.ascii import isdigit
from email.mime import base
from ntpath import join
import re
import json
import time
import numpy as np
import asyncio
import ast
import json


from pytest import Instance
from sqlalchemy import false, true
from sympy import EX


def fn(s):
    try:
        c = compile(s, "usercode", "exec")
    except Exception as exc:
        print("I caught exc\n")
        print(exc)
        print("exc.text:", exc.text)
        print(exc.filename)
        print(exc.lineno)
        print(exc.msg)
        print(exc.offset)
        return exc


def substitute(old_text, dictionary_of_substitutions):
    """ our substitution engine:

        old_text: the body of text in which to make substitutions

        dictionary_of_substitutions:
          a Python dictionary with
            keys ~ the strings to replace (get rid of)
            values ~ the strings to replace the keys with! 

        return value, nex_text: the new text, with substitutions made!

        This is the function to change, to create xkcd-type substitutions!
    """
    print(f"Not yet using the dictionary_of_substitutions: {dictionary_of_substitutions}")

    # right now, we replace every letter 'e' with the letter 'E'
    string_to_replace = 'e'
    replacement = 'E'

    # use re.sub
    new_text = re.sub( string_to_replace, replacement, old_text )
    
    # return the result
    return new_text



def seconds_since_1970(input=''):
    """ returns a json structure with two key-value pairs:
            'seconds': <the floating-point # of seconds since 1/1/1970>
            'origin': '1/1/1970'

        the input isn't used, but could be in the future
    """
    elapsed_seconds = time.time()  # built-in, counts seconds since 1970

    d = { 'seconds': elapsed_seconds, 
          'origin' : '1/1/1970' }

    string_version = json.dumps(d)  # using the json library to "dump" a string

    return string_version

    # then, try grabbing this json data -- using requests!

    


# Function takes in a string, and returns on which has been 
# translated into pig latin
def pig_translate(S):
    """ pig latin converter from '19 (with thanks to Justin G.!) """
    retStr = ''
    V = ['a','A','e','E','i','I','o','O','u','U']
    currFront = S[0]
    seen_vowel = False
    for i in range(len(S)):
        if S[i] == ' ':
            if currFront in V:
                retStr += 'by '
            else:
                retStr += currFront.lower() + 'by '
        elif i == len(S)-1:
            if currFront in V:
                retStr += S[i]+ 'by'
            else:
                retStr += S[i] + currFront.lower() + 'ay'
        else:
            if S[i-1] == ' ' or i == 0:
                seen_vowel = False
                currFront = S[i]
                if currFront in V:
                    retStr += S[i]
                    seen_vowel = True
            else:
                if S[i] in V:
                    seen_vowel = True
                    retStr += S[i]
                else:
                    if not seen_vowel:
                        currFront += S[i]
                    else:
                        retStr += S[i]
    return retStr

def determinant(one_one, one_two, two_one, two_two):
    """returns the determinant of a 2x2 matrix"""
    det = ((int(one_one)*int(two_two)) - (int(one_two)*int(two_one)))
    return det

def numToBaseB(N, B):
    """takes a non negative interger 'N' (in base 10) and a base 'B' and returns
    that number in base B"""
    if N == 0:
        return ''
    else:
        return   numToBaseB(N//B, B) + str(N%B)

def numToBin(N):
    """takes in an int in base 10 and turns it into the complete 8 bit binary version"""
    if N == 0:
        return ''
    a = numToBaseB(N//2, 2) + str(N%2)
    while len(a) != 8:
        if len(a) > 8:
            return "Error: the length of the base 10 int in binary is longer than 8."
        b = str(0) + a
        a = b
    return a

def baseBToNum(S, B):
    """accepts a string 'S' and a base 'B'. 's'
    is a number in base 'B' where B is between 2
    and 10 inclusive."""
    if S == '':
        return 0

    # if the last digit is a '1'...
    elif S[-1] ==  '1':
        return   B*baseBToNum(S[:-1], B) + int(S[-1])

    else: # last digit must be '0'
        return  B*baseBToNum(S[:-1], B) + 0

def baseToBase(B1, B2, s_in_B1):
    """takes a number in 's_in_B1' which is in B1 and 
    converts it into base B2"""
    t = baseBToNum(s_in_B1, B1)
    return numToBaseB(t, B2)



def stringToInt(text):
    """official String to unique int function. Takes in a string and outputs a unique integer in decimal form"""
    list = []
    for i in (text):
        b = (ord(i)) # gets the corresponding ascii value of the ith character in the given string and turns the value into a string
        c = numToBin(b) # turns the given number in base 10 to base 2 in full 8 bit form. Only works when the binary length is <8
        list.append(str(c))
    king =("".join(list))
    cole = baseToBase(2,10,king)
    return cole
    # nico= bin(int(king))[2:]
    # while len(nico)%8 != 0:
    #     delly = str(0) + nico
    #     nico = delly
    # print (nico)
    #return king
    #nico = bin(king)[2:]

    # list1 = []
    # for x in nico:
    #     e = baseToBase(2,10,x)
    #     list1.append(e)
    # return "".join(list1)# I wanted to return a literal int, but when I cast it to an int, python takes off the leading 
    # #          #zeroes and I need these to make a unique integer.


    # d = "".join(list)
    # return d 

def intToString(s):
    """this was a prototype for converting an int to a string but doesn't do as well becuase it only works for 
    binary string whose length is divisible by 8 evenly"""
    """input is a binary string that must be divisible by 8"""
    if len(s)%8 != 0: # checks to see if the legth of the given binary int is evenly divisible by 8
                    #It neeeds to be divisible by 8 because ascii memory is used in 8 bits, when including
                    #the leading zeros. We need it to be divisible by 8 because we can't guess where to put the zeros
        return "Error, the length of the binary integer must be divisible by 8"
    else:    
        list= []
        n = 8 #the number that will decide the grouping of ints in the list
        for i in range(0, len(s), n):
            list.append(s[i: i + n]) #createse a list of 8 but segments of the given string
        list1= [] # new list that will store the converted character
        for x in list: #loop through the list and convert each element to decimal, and perform chr() to get the ascii character
            c = int(baseToBase(2,10,x))
            d = chr(c)
            list1.append(d)
    return "".join(list1) #joins everything in the list into one string.

def decimalInput(In):
    """this was the old decimal input function, it doesn't work as well becuase it only accepts decimal numbers
    that are evenly divisible by 3 unless the length of the string of numbers is less than 3"""
    if len(In) < 3 and len(In)%3 != 0:
        while len(In) != 3:
           e = str(0) + In
           In = e
        return chr(int(e))
    elif len(In)%3 == 0:
        list=[]
        n=3
        for i in range(0, len(str(In)), n):
            list.append(In[i: i + n])
        list1=[]
        for x in list:
            d = chr(int(x))
            list1.append(d)
        return "".join(list1)
    else:
            return "Error, the length of the decimal integer must be evenly divisible by 3 (unless it contains less than three character)"

#just another base converter
DIGITS = '0123456789abcdef'        
def convert_to_base(decimal_number, base):
    remainder_stack = []

    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base

    new_digits = []
    while remainder_stack:
        new_digits.append(DIGITS[remainder_stack.pop()])

    return ''.join(new_digits)
    

def newDeciInput(N):
    """the final product!!!"""
    """Takes in a decimal input, outputs a unique program"""
    a = bin(int(N))[2:] #converts N to the binary version, and slices off the first two character's since they're irrellevent
    while (len(a)%8 != 0): #append 0's to the front if the length is not evenly divisible by 8
        b = str(0) + a
        a = b
    list= []
    n = 8 #the number that will decide the grouping of ints in the list
    print(a)
    for i in range(0, len(a), n):
        list.append(a[i: i + n]) #createse a list of 8 but segments of the given string
    list1= [] # new list that will store the converted character
    for x in list: #loop through the list and convert each element to decimal, and perform chr() to get the ascii character
        c = baseToBase(2,10,x)
        d = chr(int(c))
        list1.append(d)
    h = "".join(list1) 
    return h #joins everything in the list into one string.

def jsAndFetchEx(xValue,yValue):
    number =  int(xValue) + int(yValue)
    return str(number)

# def compEx(str):
#     c = compile(str, "usercode", "exec")
#     exec(c)
#     if sleep_in(False, False)!=True:
#         return "fail"
#     else:
#         return "pass"

# def compEx0(str):
#     c = compile(str, "usercode", "exec")
#     return exec(c)

def compEx2(st):
    st = str(st)
    c = compile(st, "usercode", "exec")

    exec(c)
    result = eval("f(41)")
    if result == 42:
        print("correct")
    else:
        print("wrong")

def compEx3(funct, lst):
    dict = {}
    exec(funct)
    for i in lst:
        # if i.isdigit() == False and isinstance(i,str) == True: #what if the specified input is a number? We need a way to check if the input
        #                                                         #should be evaluated as a number or an int?
        #     i = "'"+ i + "'"   
        # if isdoublestring(i) == True:        #remove the extra "'" from i if the input is a string
        #     i = i[1:-1]
        s = functFinder(funct) + "(" + str(i) + ")"
        # print (s)
        if i.isdigit() == True:
            i = int(i) 
        a = eval(s)
        if isdoublestring(i) == True:        #remove the extra "'" from i if the input is a string
            i = i[1:-1]
        dict[i] = a
    return dict

def compEx4(funct, lst):
    dict = {}
    lst1 = []
    exec(funct)
    for i in lst:
        s = functFinder(funct) + "(" + str(i) + ")"
        if type(i) == tuple:
            lst2 = list(i)
            lst1.append(lst2)
    if lst1 != []:
        for x in lst1:
            for c in range(len(x)):
                if x[c].isdigit() == True:
                    x[c] = int(x[c])
        for d in lst1:
            for h in range(len(d)):
                print(d[h])
                print(isinstance(d[h],str))
                if isinstance(d[h],str) == True: #need to take the extra ' off of the string
                    p = d[h]
                    h = p[1:-1]
                    print(h)
            print(d)
            print("d[0] is ", d[0])
            l = d[0]
            l[1:-1]
            print("the new d[0] ")
            d = str(d)[1:-1] # remove the brackets on the list
            # print(d)
            # if d.isdigit() == True:
            #     d = int(i) 
            t = functFinder(funct) + "(" + repr(d) + ")"
            # b = eval(t)
            # print(str(t))
    #         for h in d:
    #             if isdoublestring(h) == True:        #remove the extra "'" from i when input is a string
    #                 d = d[1:-1]
    #         dict[d] = b
    # return dict
            
            # for x in i:
            #     # list.append(x)
            #     # print(list)
            #     for c in list:
            #         if c.isdigit() == True:
            #             # c = int(c)
            #             c = 211231
            #             print(c)
            #             print(type(c))
            #             print(list)
        # print(list)
                # print(x)
                # print(x.isdigit())
                # if x.isdigit() == True:
                #     x = int(x)
                #     newtuple = ()
                #     print(x)
                #     print("x is now a: ", type(x))
                # print(lst)
    #     else:
    #         if i.isdigit() == True:
    #             i = int(i) 
    #         a = eval(s)
    #         if isdoublestring(i) == True:        #remove the extra "'" from i when input is a string
    #             i = i[1:-1]
    #         dict[i] = a
    # return dict

def compEx5(funct, lst):
    loc= {}
    dict = {}
    exec(funct)

    lst = inWireFix(lst)
    print(lst)
    for i in lst:
        if type(i) == tuple:
            s = functFinder(funct) + str(i)
        else:
            i = repr(i)
            s = functFinder(funct) + "(" + str(i) + ")"    
        a = eval(s)
        if isdoublestring(i) == True:        #remove the extra "'" from i if the input is a string so that the dict reads cleanly
                i = i[1:-1]
        dict[i] = a
    return dict

def compEx6(funct, lst):
    dict = {}
    exec(funct)

    lst = inWireFix(lst)
    print(lst)
    for i in lst:
        if type(i) == tuple:
            s = functFinder(funct) + str(i)
        else:
            i = repr(i)
            s = functFinder(funct) + "(" + str(i) + ")"    
        a = eval(s)
        if isdoublestring(i) == True:        #remove the extra "'" from i if the input is a string so that the dict reads cleanly
                i = i[1:-1]
        dict[i] = a
    return dict

def specialSauce(input):
    d1={}
    input = ast.literal_eval(input)
    # print(input)
    # print(type(input))
    for key in input:
        if type(key) == tuple:
            newkey = str(key)
            # print(key)
            # print(type(key))
        d1[newkey] = input[key]
    # print(d1)
    # print(type(d1))
    for i, k in enumerate(d1):
        print(i,k)
    listd1 = list(d1)
    print(list(d1))
    print(listd1[0])
    print(d1[listd1[0]])
    return d1

def specialSauce1(input):
    d1={}
    d1["ioPairs"] = input 
    d1["name"] = "twoInput1"
    print(d1)
    return d1

#helper function that is used in routes to 
def specialSauce2(input):
    comp


def twoInput4():
	breh = integer + 1
	return string[:1] + ' ' + str(breh)


def dictHelper(n):
    u = []
    u1 = []
    n = ast.literal_eval(n)
    for key,value in n.items():
        # print(key, value)
        # print("the key type is: ", type(key))
        value = "'" + value + "'"
        # print("the new value is: ", value)
        if type(key) == tuple:
            key = str(key)
        f = "{" + "\"" +str(key)+ "\"" +": " + str(value) + "}"
        # print("f is ", f)
        # f = ast.literal_eval(f)
        u.append(f)
    for i in u:
        i = ast.literal_eval(i)
        # print("i is : ", i)
        u1.append(i)
    return u1


    




def inWireFix(data):
    """helper function that deals with the incoming stringified data from the front end.
    it unstringifies the list to get an actual list with elements that do not have any extra quotes around them."""
    list1 = []
    if isinstance(data,str) == True: #conditional for when the input is string of a list, ie "['1','2','3']"
        newData= ast.literal_eval(data)
        print(newData)
        
        for i in newData:
            if i.isdigit() == True:
                i = int(i)
                list1.append(i)
            elif isinstance(i,str):
                list1.append(i)
        return list1
    if isinstance(data,list):
        for i in data:
            if i.isdigit() == True:
                i = int(i)
                list1.append(i)
            if isinstance(i,str) == True and i[0]== '(': #need to check if the element i is tuple or a regular string input
                i = ast.literal_eval(i)
                list1.append(i)
            else:
                list1.append(i)
        return list1



#this works for numbers, but we need to see how a list of string is recieved from the front end



    

def paramCounter(funct):
    """Helper function that returns how many parameter and given function has"""
    for i in range(len(funct)):
        if funct[i] == '(':
            newfunct = funct[i:]
    
    for x in range(len(newfunct)):
        if newfunct[x] == ')':
           newnewfunct = newfunct[:x]
           print(newnewfunct)
    counter = 0
    for z in newnewfunct:
        if z == ",":
            counter+=1
    return counter

def stringAndInt(string, integer):
    newint = integer + 1
    return string[:3] + " " +  str(newint)

        
def testFunc():
    a = '''def bad(x):
        return bad(x + 1)'''
    b = '''bad(1)'''
    try:
        s = f"""
def testFunc():
    {a}
    return {b}
testFunc() """
        print(s)
        exec(s)
    except Exception as e:
        print(e)
        return e

#     s="""
# def testFunc():
#     def factorial(x):
#         if x==0: return 1
#         return x*factorial(x-1)
#     print(factorial(10))
# testFunc()"""

   


def wan(w):
    '''weird helper function that converts the "list" recieved from the server's form data into a regular list'''
    newW = []
    for i in w:
        i = int(i)
        newW.append(i)
    return newW

def isdoublestring(any):
    if isinstance(any, int) == True:
        return

    if any[:1] == "'":
        return True
    else:
        return False

def myAppend(list,nico):
    newlist = []
    if list == []:
        # list =[]
        list.append(nico)
        return list
    else:
        list.append(nico)
    return list
        


def functFinder(funct):
    """helper function that finds the name of a function that is being defined. ie, the name of def breh(): is 'breh'. Warning this doesn't 
    account for the syntax error of naming a function with spaces"""
    funct = str(funct)
    old_funct = funct[:4]
    funct = funct[4:]
    list = []
    
    if old_funct[:4] != "def ":
        raise Exception('The function needs to start with "def ". The first 4 characters of your function are: {}'.format(old_funct[:4]))
    for i in range(len(funct)):
        
        if funct[i] == '(':
            return funct[:i]
        # else:
        #     raise Exception('The function has a syntax error: most likely a missing parenthesis')
    
            


    




    # eval(c)
    # compEx0(str)
    # if exec("f(1)") != 2:
    #     return "fail"
    # else:
    #     return "pass"

# def check():
#     if f(2) == 3:
#         return True
#     else:
#         return False

# def f(x):
#     return x+1



