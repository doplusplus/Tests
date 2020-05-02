from sikuli import *

import shutil

def findTexts(textList, analysedString, errorSectionName) :
    errors = []
    for txt in textList:
        if txt in analysedString:
            print(txt + ' found')
        else:
            errors.append(txt) 

    if len(errors) > 0:
        print('------ '+ errorSectionName +' ------')
        for error in errors:
            print(error + ' not found')
        print('OCR reads: ', analysedString)

def screenshot(output):
    s = Screen()
    r = Region(s.x,s.y,s.w,s.h)
    filename = s.capture(r).getFile()
    shutil.move(filename,output)