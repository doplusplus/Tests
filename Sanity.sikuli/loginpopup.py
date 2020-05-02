from sikuli import *
from tools import *

def testLoginPopup():
    type(Key.PAGE_UP)
    sleep(3)
    click("1588147750988.png")
    r = wait("1588147921833.png",2)
    t = r.left(50)\
    
    # NOT READY YET FOR SCREEN CAPTURE        
    #screen = Screen()
    #file = screen.capture(screen.getBounds())
    #print(file)
    click(t)
    sleep(1)
    identical = exists('popupscreen.png')
    print(identical)
    message = "as expected: screen didn't change"  if identical is not None else "something changed" 
    print(message)
    
    
    #log in text verification
    popupRegion = exists(Pattern("popup.png").similar(0.90))
    buttonsRegion = exists("1588158181201.png")
    popupText=popupRegion.text()
    buttonText=buttonsRegion.text()
    WhiteText= ['Log in' , 'Cancel']
    TextToFind =['Would you like to log In' , 'Username' ,  'Password' ,'Register' ]
    findTexts(TextToFind , popupText , 'missing pop up text' )
    
    #Register Texts verification
    click("1588162307379.png")
    registerText = popupRegion.text()
    registerTextList = ['username', 'password', 'back', 'cancel', 'send' ]
    findTexts(registerTextList , registerText , 'missing register text' )
    
    #click on back
    backToLogin = exists(Pattern("popup.png").similar(0.90)) is not None
    print( 'PASS: back to login' if backToLogin else 'FAIL: login content not found' )
    click("1588149431776.png")
    
    backToHome = exists("1588163016384.png") is not None
    print('PASS: back to home' if backToHome else 'not in the home menu')
