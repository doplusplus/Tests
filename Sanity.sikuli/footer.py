from sikuli import *

def testFooterMenu(link,picture,name):
    click(link)
    ppOK = exists(picture) is not None
    print(name + 'still needs implementation' if ppOK else name + 'FAILED' )
    click("1588260170327.png")   
    

def testFooter():
    type(Key.PAGE_DOWN)
    sleep(3)
    testFooterMenu("1588259685875.png","1588260088936.png",'contacts')
    testFooterMenu("1588259705221.png","1588260218332.png",'donate')
    testFooterMenu("1588259720729.png","1588260257384.png",'feedback')
    testFooterMenu("1588259728797.png","1588260280178.png",'others')
    testFooterMenu("1588259735502.png","1588260311779.png",'where to read')
    testFooterMenu("1588259743618.png","1588260336515.png",'where to watch')