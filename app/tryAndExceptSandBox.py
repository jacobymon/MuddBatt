from sys import breakpointhook
import time
import threading

        

# def testFunc():
#     try:
#        eval( '''def func(string, integer):
#                         breh = integer + 1
#                         return string + " " + str(breh)''')
#         # eval('print(x)')

#     # except SyntaxError:
#     #     print("you can not do that") 
    
#     except Exception as e:
#         # template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#         # message = template.format(type(e).__name, e.args)
#         # print(message)
#         print(e)
#         return e

def testFunc():
    
    cmd = '''def bad(b):
                return "hello"
    '''
 
    try:
        exec(cmd)

    except SyntaxError as err:
        # print(err.lineno)
        # print(err)
        # print(dir(err))
        # print("the text is: ", err.text)
        # print("the message is: ", err.msg)
        

        return err.msg + " on line " + str(err.lineno)
    except Exception as logicErr:
        print(logicErr)
        return logicErr

def extraTab(string):
    new = string.replace('\n','\n    ')
    return new

def infiniteloop():
    sample = '''
a = 1
    while a == 1:
        print("breh")'''
    
    if "while" or "for" in sample:

        newSample = sample + '''start_time = time.time()
        seconds = 4

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            print(elapsed_time)

            if elapsed_time > seconds:
                print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
                break'''
        print(newSample)
        exec(newSample)
        # try:
        #     eval(newSample)
                
        # except:
        #     return


def test():
    start_time = time.time()
    seconds = 2
    a = 1
    while a == 1:
        
        print("breh")
        current_time = time.time()
        elapsed_time = current_time - start_time
        # print(elapsed_time)
        if elapsed_time > seconds:
            print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
            return "error, infinite loop"


def timer():
    start = time.time()
    sample = '''a = 1\nwhile a == 1:\n  print("breh")'''
    while True:
        current = time.time()
        elapsed = current - start
        try:
            exec(sample)
        except:
            return
        print(elapsed)


def test1():
    start = time.time()
    print('the start is ', start)
    currentTime = time.time()
    print("hello")
    print('the current time is : ', currentTime)
    # end = time.time()
    # print("the start is : ", start)
    # print("the end is : ", end)
    # print(end - start)


def nico():
    otherTimer = '\n    current_time = time.time()\n    elapsed_time = current_time - start_time\n    print(elapsed_time)\n    if elapsed_time > 2:\n      return "error, infinite loop"'

    sample = '''def sample():\n  a = 1\n  while a == 1:\n    print("breh")
            '''


    for k in range(len(sample)): # insert srart time at top of function
        if sample[k] == ":":
            sample = sample[:k + 1] + "\n  start_time = time.time()\n" + sample[k+1:]
            break
    

    
    if "while" in sample: #insert timer in the while loop
        for i in range(len(sample)):
            if sample[i] + sample[i + 1] + sample[i + 2] + sample[i + 3] + sample[i + 4] == 'while':
                newstring = sample[i:]
    
                for j in range(len(newstring)):
                    if newstring[j] == ':':
                        print(sample[:i] + sample[i:] + otherTimer)
                        output = sample[:i] + sample[i:] + otherTimer
                        exec(output)

                        return eval('sample()')


def j():
    exec('nico()')
    return eval('sample()')

def delly():
    exec('def sample():\n  start_time = time.time()\n\n  a = 1\n  while a == 1:\n    print("breh")\n            \n    current_time = time.time()\n    elapsed_time = current_time - start_time\n    print(elapsed_time)\n    if elapsed_time > 2:\n      return "error, infinite loop"')
    return eval('sample()')

def jen():
    j = 'def n():\n while True:\n   return "hello"'
    exec(j)
    return eval('n()')

def lock():
    print('def sample():\n  start_time = time.time()\n\n  a = 1\n  while a == 1:\n    print("breh")\n            \n    current_time = time.time()\n    elapsed_time = current_time - start_time\n    print(elapsed_time)\n    if elapsed_time > 2:\n      return "error, infinite loop"')