from sikuli import *
import tools
reload(tools)

def testLandingScreen() :
    # Hover the cursor over the Home text , catchphrase and user icon
    wait(Resources.CatchPhraseImages.home,3)
    homeTest     = hover(Resources.Banner.homeIcon)
    screenshot('C:\Dev\TESTS\Screenshot')
    homePhrase   = hover(Resources.CatchPhraseImages.home)
    screenshot('C:\Dev\TESTS\Screenshot')
    userIcon     = hover(Resources.Banner.userIcon)
    screenshot('C:\Dev\TESTS\Screenshot') 

    
    # Check the central image: the image bottom should match the screen bottom
    bottomRight = Region(1499,890,405,186)
    homeheightCheck = bottomRight.exists("1588327659663.png") is not None
    print("correct height for central image: ",homeheightCheck)
    sleep(1)

    
    #check the mainscreen menus
    accountImage = Resources.Home.accountLink
    account = exists(accountImage) is not None
    print('account menu found: ', account )
    if account:
        hover(accountImage)
    
    sleep(1) 
    rankingImage = Resources.Home.rankingLink
    ranking = exists(rankingImage) is not None
    print('ranking menu found: ', ranking )
    if ranking:
        hover(rankingImage)
    
    sleep(1)   
    aboutImage = Resources.Home.aboutLink
    about = exists(aboutImage) is not None
    print('about menu found: ', about )
    if about:
        hover(aboutImage)
    
    sleep(1)
    advisedImage =Resources.Home.advisedLink
    advised = exists(advisedImage) is not None
    print('advised menu found: ', advised )
    if advised:
        hover(advisedImage)
    
    sleep(1) 
    RateItImage = Resources.Home.rateItLink
    RateIt = exists(RateItImage) is not None
    print('RateIt menu found: ', RateIt )
    if RateIt:
        hover(RateItImage)

    sleep(1)
    wheel(Button.WHEEL_DOWN,3) # todo add region image
    footerRegion = Region(0,809,1903,271)
    footerText = footerRegion.text() 

    print('checking footers')
    menusToFind =['Contact' , 'Other rankings' ,  'Donate' , 'Where to read mangas' , 'Feedback' , 'Where to watch animes' ]
    errors = []
    for menuName in menusToFind:
        if menuName in footerText:
            print(menuName + ' found')
        else:
           errors.append(menuName) 
    
    if len(errors) > 0:
        print('------ footer errors ------')
        for error in errors:
            print(error + ' not found')
        print(footerText)
        