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
    



