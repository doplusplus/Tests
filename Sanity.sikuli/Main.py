from sikuli import *

import webbrowser
import Resources
import landingscreen
#import tools
#import loginpopup
#import homeMenu
#import footer
reload(landingscreen)
#reload(tools)
#reload(loginpopup)
#reload(homeMenu)
#reload(footer)
reload(Resources)


webbrowser.open('http://nemo.com', new=2)
# Go to https://listman.pythonanywhere.com/
click(Resources.FireFox.newTab)
click(Resources.FireFox.addressBar)

type('https://listman.pythonanywhere.com/' + Key.ENTER)
sleep(1)
testLandingScreen()
sleep(1)
#testLoginPopup()
sleep(1)
#testHomeMenu()
sleep(1)
#testFooter()