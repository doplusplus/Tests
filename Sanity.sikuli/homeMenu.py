from sikuli import *
    
def testMenu( menuIcon, mainSection,navSection,catchPhrase,menuName):
   # wheel(Button.WHEEL_UP,6)
    type(Key.PAGE_UP)
    click("1588168667750.png")
    sleep(1)
    click(menuIcon)
    aboutMainOK = exists(mainSection) is not None  
    aboutNavOK  =  navSection is None or exists(navSection) is not None
    aboutCatchphraseOK = catchPhrase is None or exists(catchPhrase) is not None
    print( menuName+' is ok' if aboutMainOK and aboutNavOK and aboutCatchphraseOK else menuName +' Fail')


def checkFooter(footerImage):
    #wheel(Button.WHEEL_DOWN,6)
    type(Key.PAGE_DOWN)
    footerOK = exists(footerImage) is not None
    print('footer is OK' if footerOK else 'Footer failed' )

    
def testHomeMenu():
    testMenu( "1588165738701.png" , "aboutMainOK.png" , "aboutNavOK.png" , "aboutCatchphrase.png",'about')
    checkFooter("1588167075715.png")
    
    testMenu("1588167234927.png","1588167336199.png","1588167352705.png","1588167364132.png",'ranking')
    checkFooter("1588167075715.png")
    
    testMenu("1588167245201.png","1588167467706.png","1588167479022.png","1588167489300.png", 'advised')
    checkFooter("1588167075715.png")
    
    testMenu("1588167256223.png","1588167521023.png","1588167533133.png","1588167542634.png", 'rate it')
    checkFooter("1588167075715.png")
    
    testMenu("1588167283918.png","1588167694199.png",None,None, 'account')
    
    checkFooter("1588168041745.png")           
    click("1588261542895.png")