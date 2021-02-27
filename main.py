import pyautogui
import time
### YOU MUST INSTALL opencv-python https://pypi.org/project/opencv-python/
time.sleep(2)
right1 = (1475, 485)
right2 = (1475, 635)
right3 = (1475, 785)
left1 = (260, 485)
left2 = (260, 635)
left3 = (260, 785)
# Un comment this to get a box that shows the coordinates of your mouse.
# Use this to see where to place the towers
#pyautogui.mouseInfo()
pyautogui.PAUSE = 0.1

class Tower:
    def __init__(self, xCord, yCord, hotkey, restartMap, targeting=0, farms=None):
        self.xCord = xCord
        self.yCord = yCord
        self.coords = (self.xCord, self.yCord)
        if xCord >= 835:
            self.upgradeSide = "left"
        else:
            self.upgradeSide = "right"
        self.hotkey = hotkey
        self.targeting = targeting
        self.restartMap = restartMap
        self.farms = farms


    def p(self, path=None, quantity=None, path2=None, quantity2=None, coop=None):
        placing = 1
        while placing:
            checkForLevelUp(self.restartMap, self.farms)
            time.sleep(.25)
            pyautogui.moveTo(self.xCord, self.yCord)
            pyautogui.press(self.hotkey)
            pyautogui.click()
            if coop == None:
                time.sleep(.05)
            else:
                time.sleep(.5)
            pyautogui.click()
            time.sleep(.25)
            if self.upgradeSide == "left":
                # 63, 29 (255, 255, 255)
                # 63, 32 ( 255, 84, 0
                if not pyautogui.pixelMatchesColor(256, 44, (254, 190, 0), tolerance=20):
                    placing = 0
            elif self.upgradeSide == "right":
                if not pyautogui.pixelMatchesColor(1629, 40, (254, 254, 254), tolerance=5):
                    placing = 0
        for i in range(self.targeting):
            pyautogui.press("tab")
        if path!=None:
            afterPlacing = 1
            self.u(path, quantity, path2, quantity2, afterPlacing)
        else:
            pyautogui.click(1635, 0)
            time.sleep(.05)

    def u(self, path, quantity, path2=None, quantity2=None, afterPlacing=None, temple=None):
        if self.upgradeSide == "left":
            if path == 1:
                buttonCoords = (260, 485)
            elif path == 2:
                buttonCoords = (260, 635)
            elif path == 3:
                buttonCoords = (260, 785)

            if path2 == 1:
                buttonCoords2 = (260, 485)
            elif path2 == 2:
                buttonCoords2 = (260, 635)
            elif path2 == 3:
                buttonCoords2 = (260, 785)
        elif self.upgradeSide == "right":
            if path == 1:
                buttonCoords = (1475, 485)
            elif path == 2:
                buttonCoords = (1475, 635)
            elif path == 3:
                buttonCoords = (1475, 785)

            if path2 == 1:
                buttonCoords2 = (1475, 485)
            elif path2 == 2:
                buttonCoords2 = (1475, 635)
            elif path2 == 3:
                buttonCoords2 = (1475, 785)

        checkForLevelUp(self.restartMap, self.farms)
        if afterPlacing == None:
            pyautogui.click(1635, 0)
            time.sleep(.05)
            pyautogui.click(self.xCord, self.yCord)

        count = 0
        while count < quantity:
            checkForLevelUp(self.restartMap, self.farms, self.coords)
            if pyautogui.pixelMatchesColor(buttonCoords[0], buttonCoords[1], (80, 213, 0), tolerance=10):
                if path == 1:
                    pyautogui.press(",")
                elif path == 2:
                    pyautogui.press(".")
                elif path == 3:
                    pyautogui.press("/")
                count += 1

        count2 = 0
        if path2!=None:
            while count2 < quantity2:
                checkForLevelUp(self.restartMap, self.farms, self.coords)
                if pyautogui.pixelMatchesColor(buttonCoords2[0], buttonCoords2[1], (84, 222, 0), tolerance=20):
                    if path2 == 1:
                        pyautogui.press(",")
                    elif path2 == 2:
                        pyautogui.press(".")
                    elif path2 == 3:
                        pyautogui.press("/")
                    count2 += 1
        if temple == None:
            pyautogui.click(1635, 0)
            time.sleep(.05)
        else:
            time.sleep(.5)
            pyautogui.click(1133, 730)
    def s(self):
        pyautogui.click(1635, 0)
        time.sleep(.05)
        pyautogui.click(self.xCord, self.yCord)
        time.sleep(.05)
        pyautogui.press('backspace')
# Enter the coordinates of the towers that you want to place

def checkForDeath(restartMap):
    if pyautogui.pixelMatchesColor(1006, 860, (255, 194, 0)):
        pyautogui.click(1006, 860)
        time.sleep(.5)
        pyautogui.click(1046, 723)
        restartMap()

def checkForLevelUp(restartMap, farms=None, coords=None):
    if farms != None:
        for i in range(len(farms)):
            pyautogui.moveTo(farms[i][0], farms[i][1])
            time.sleep(.02)
    if pyautogui.pixelMatchesColor(970, 500, (0, 202, 222), tolerance=10):
        pyautogui.moveTo(875, 493)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.press("space")
        time.sleep(1)
        pyautogui.click(coords)
    checkForDeath(restartMap)

def checkForGameEnd(restartMap, farms=None, round100=None):
    checkForLevelUp(restartMap, farms)
    if round100 < 4:
        if pyautogui.pixelMatchesColor(880, 900, (110, 231, 0), tolerance=20):
            pyautogui.click(880, 900)
            time.sleep(1)
            pyautogui.click(1116, 882)
            time.sleep(1)
            if round100 == 3:
                pyautogui.click()
                time.sleep(1)
                pyautogui.press("space")
                time.sleep(1)
            if round100 !=3:
                pyautogui.click(1596, 38)
                time.sleep(2.5)
                pyautogui.click(1596, 38)
                time.sleep(1)
                pyautogui.click(1065, 859)
                time.sleep(1)
                pyautogui.click(1140, 720)
                time.sleep(1)
            return 1
    if round100 == 1:
        if pyautogui.pixelMatchesColor(933, 811, (156, 255, 0), tolerance=10):
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.click(880, 900)
            time.sleep(1)
            pyautogui.click(1116, 882)
            time.sleep(1)
            pyautogui.click(1596, 38)
            time.sleep(2.5)
            pyautogui.click(1596, 38)
            time.sleep(1)
            pyautogui.click(1065, 859)
            time.sleep(1)
            pyautogui.click(1140, 720)
            time.sleep(1)
            return 1

    if round100 == 2:
        if pyautogui.pixelMatchesColor(933, 811, (156, 255, 0), tolerance=10):
            pyautogui.click()
            time.sleep(1)
            pyautogui.click(880, 900)
            time.sleep(1)
            pyautogui.click(1116, 882)
            time.sleep(1)
            pyautogui.press("space")
            return 1
    if round100 == 4:
        if pyautogui.pixelMatchesColor(999, 891, (255, 255, 255), tolerance=10):
            pyautogui.click(999, 891)
            time.sleep(2)
            pyautogui.click(1000, 800)
            time.sleep(1)
            pyautogui.click(1110, 700)
            time.sleep(1)
            pyautogui.press("space")
    if round100 == 5:
        if pyautogui.pixelMatchesColor(880, 900, (110, 231, 0), tolerance=20):
            pyautogui.click(880, 900)
            time.sleep(1)
            pyautogui.click(800, 850)
            time.sleep(1)
            collectionEvent()
        pass

### USE QUINCY
def darkCastle():
    dart = Tower(1461, 572, 'q', darkCastle, 3)
    hero = Tower(1017, 446, 'u', darkCastle)
    boat = Tower(1264, 423, 'c', darkCastle)
    alch = Tower(1455, 446, 'f', darkCastle)
    sub1 = Tower(1327, 694, 'x', darkCastle)
    sub2 = Tower(1218, 691, 'x', darkCastle)

    while 1:
        time.sleep(1)
        waitingForEnd = 1
        checkForLevelUp(darkCastle)
        pyautogui.press("space")
        pyautogui.press("space")
        hero.p()
        dart.p(2, 2, 3, 3)
        boat.p(2, 2, 1, 3)
        alch.p(1, 4, 3, 1)
        dart.u(3, 2)
        sub1.p(3, 4)
        sub2.p(1, 2, 3, 4)
        while waitingForEnd:
            if checkForGameEnd(darkCastle) == 1:
                waitingForEnd = 0

def mapOne():
    waitingForEnd = 1

    hero = Tower(485, 468, 'u', mapOne)
    alch = Tower(659, 258, 'f', mapOne)
    boat = Tower(563, 396, 'c', mapOne)
    wizard = Tower(392, 601, 'a', mapOne)
    time.sleep(10)
    pyautogui.press("space")
    time.sleep(.5)
    pyautogui.press("space")

    checkForLevelUp(mapOne, None)
    hero.p()
    boat.p(2, 2, 1, 3)
    alch.p(1, 4, 2, 2)
    wizard.p(3, 2, 1, 3)
    while waitingForEnd:
        checkForLevelUp(mapOne, None)
        if pyautogui.pixelMatchesColor(954, 745, (113, 232, 0), tolerance=20):
            pyautogui.click(954, 745)
            time.sleep(7)
            pyautogui.click(1734, 929)
            waitingForEnd = 0
def mapTwo():
    waitingForEnd = 1
    hero = Tower(907, 633, 'u', mapTwo)
    boat = Tower(796, 584, 'c', mapTwo)
    wizard = Tower(819, 757, 'a', mapTwo)
    alch = Tower(695, 737, 'f', mapTwo)

    time.sleep(10)
    pyautogui.press("space")
    time.sleep(.5)
    pyautogui.press("space")
    checkForLevelUp(mapTwo, None)

    hero.p()
    boat.p(2, 2, 1, 3)
    alch.p(1, 4, 2, 2)
    wizard.p(3, 2, 1, 4)
    boat.u(1, 2)


    while waitingForEnd:
        checkForLevelUp(mapTwo, None)
        if pyautogui.pixelMatchesColor(954, 745, (113, 232, 0), tolerance=20):
            pyautogui.click(954, 745)
            time.sleep(7)
            pyautogui.click(1734, 929)
            waitingForEnd = 0
def mapThree():
    waitingForEnd = 1
    wizard = Tower(448, 616, 'a', mapThree)
    hero = Tower(449, 515, 'u', mapThree)
    village = Tower(310, 753, 'k', mapThree)
    alch = Tower(441, 789, 'f', mapThree)
    bomb = Tower(322, 561, 'e', mapThree)
    bomb2 = Tower(172, 636, 'e', mapThree)

    time.sleep(10)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press("space")
    time.sleep(.5)
    pyautogui.press("space")
    checkForLevelUp(mapThree, None)
    hero.p()
    wizard.p(1, 4, 2, 2)
    alch.p(1, 4, 2, 2)
    village.p(1, 3, 2, 2)
    bomb.p(1, 4, 2, 2)
    bomb2.p(3, 2, 2, 1)

    while waitingForEnd:
        checkForLevelUp(mapThree, None)
        if pyautogui.pixelMatchesColor(954, 745, (113, 232, 0), tolerance=20):
            time.sleep(5)
            pyautogui.click(954, 745)
            time.sleep(5)
            pyautogui.click(954, 838)
            time.sleep(5)
            pyautogui.click(954, 838)
            time.sleep(5)
            waitingForEnd = 0

def odyssey():
    while 1:
        map2 = 1
        map3 = 1
        pyautogui.click(1760, 950)
        time.sleep(.5)
        pyautogui.click(1760, 950)
        time.sleep(.5)
        pyautogui.click(1760, 950)
        mapOne()
        while map2:
            if pyautogui.pixelMatchesColor(76, 37, (255, 95, 0), tolerance=10):
                map2 = 0
                mapTwo()
        while map3:
            if pyautogui.pixelMatchesColor(76, 37, (255, 95, 0), tolerance=10):
                map3 = 0
                mapThree()

### USE QUINCY
def darkCastleImpoppable():
    farms = [(731, 736), (898, 734), (731, 880), (900, 875)]

    # 726, 437
    hero = Tower(726, 437, 'u', darkCastleImpoppable, 0, farms)
    dart1 = Tower(550, 615, 'q', darkCastleImpoppable, 0, farms)
    dart2 = Tower(260, 248, 'q', darkCastleImpoppable, 0, farms)

    farm1 = Tower(731, 736, 'h', darkCastleImpoppable, 0, farms)
    farm2 = Tower(898, 734, 'h', darkCastleImpoppable, 0, farms)
    farm3 = Tower(731, 880, 'h', darkCastleImpoppable, 0, farms)
    farm4 = Tower(900, 875, 'h', darkCastleImpoppable, 0, farms)

    sub1 = Tower(1209, 430, 'x', darkCastleImpoppable, 0,  farms)
    sub2 = Tower(1324, 405, 'x', darkCastleImpoppable, 0, farms)
    alch1 = Tower(1313, 280, 'f', darkCastleImpoppable, 0, farms)
    alch2 = Tower(1451, 666, 'f', darkCastleImpoppable, 0, farms)
    alch3 = Tower(672, 168, 'f', darkCastleImpoppable, 0, farms)
    wizard1 = Tower(846, 444, 'a', darkCastleImpoppable, 0, farms)
    wizard2 = Tower(572, 477, 'a', darkCastleImpoppable, 0, farms)
    dartling1 = Tower(1454, 569, 'm', darkCastleImpoppable, 0, farms)
    glue1 = Tower(542, 402, 'y', darkCastleImpoppable,  0, farms)
    glue2 = Tower(488, 309, 'y', darkCastleImpoppable, 3, farms)
    village1 = Tower(723, 341, 'k', darkCastleImpoppable, 0, farms)
    spike1 = Tower(1570, 552, 'j', darkCastleImpoppable, 0, farms)
    heli1 = Tower(842, 213, 'b', darkCastleImpoppable, 0, farms)
    sniper1 = Tower(977, 357, 'z', darkCastleImpoppable, 3, farms)
    sniper2 = Tower(870, 328, 'z', darkCastleImpoppable, 3, farms)

    while 1:
        time.sleep(1)
        waitingForEnd = 1
        checkForLevelUp(darkCastleImpoppable)
        hero.p()
        dart1.p()
        pyautogui.press("space")
        pyautogui.press("space")
        farm1.p()
        sub1.p(3, 1)
        farm1.u(1, 1)
        sub1.u(1, 2)
        farm1.u(1, 1)
        sub1.u(3, 1)
        farm2.p(1, 2)
        alch1.p(1, 2)
        farm3.p(1, 2)
        alch1.u(1, 1)
        farm4.p(1, 2)

        pyautogui.moveTo(814, 808)
        time.sleep(8)
        # Breaking trees
        pyautogui.click(210, 186)
        time.sleep(.25)
        pyautogui.click(457, 189)
        time.sleep(.25)

        dart2.p(3, 2)
        sub1.u(3, 1)
        farm4.u(3, 3)
        farm2.u(1, 1)
        farm3.u(1, 1)
        wizard1.p(1, 2, 3, 4)
        dartling1.p()
        # Locking the dart in place
        pyautogui.click(1454, 569)
        pyautogui.moveTo(754, 550)
        time.sleep(.5)
        pyautogui.press("tab")
        pyautogui.click(1635, 0)
        time.sleep(.05)
        dartling1.u(1, 2, 2, 3)
        alch2.p(1, 3)
        farm2.u(1, 1)
        alch2.u(1, 1, 3, 1)
        farm2.u(2, 2)
        farm1.u(1, 1)
        sub2.p(1, 2, 3, 3)
        sub1.u(3, 1)
        glue1.p(1, 2, 2, 3)
        farm1.u(1, 1, 2, 2)
        sub2.u(3, 2)
        farm3.u(1, 1, 2, 2)
        village1.p(1, 2, 2, 3)
        wizard1.u(3, 1)
        spike1.p(1, 2, 3, 5)
        heli1.p(1, 4, 3, 2)
        alch3.p(1, 4, 2, 2)
        heli1.u(1, 1)
        glue2.p(2, 2, 3, 3)
        sniper1.p(1, 4, 3, 2)
        farm1.s()
        farm2.s()
        farm3.s()
        farm4.s()
        wizard2.p(1, 5, 3, 2)
        sniper2.p(1, 4, 3, 2)

        while waitingForEnd:
            if checkForGameEnd(darkCastleImpoppable, farms, 1) == 1:
                waitingForEnd = 0

### WIP USE OBYN
def lateGameCubizm():

    hero = Tower(588, 484, 'u', lateGameCubizm)
    dart1 = Tower(660, 530, 'q', lateGameCubizm)

    farm1 = Tower(838, 1009, 'h', lateGameCubizm)
    farm2 = Tower(639, 1010, 'h', lateGameCubizm)
    farm3 = Tower(476, 1009, 'h', lateGameCubizm)
    farm4 = Tower(307, 1011, 'h', lateGameCubizm)
    farm5 = Tower(142, 1011, 'h', lateGameCubizm)
    farm6 = Tower(674, 869, 'h', lateGameCubizm)
    farm7 = Tower(509, 868, 'h', lateGameCubizm)
    farm8 = Tower(342, 868, 'h', lateGameCubizm)
    farm9 = Tower(180, 870, 'h', lateGameCubizm)
    farm10 = Tower(267, 727, 'h', lateGameCubizm)
    farm11 = Tower(187, 586, 'h', lateGameCubizm)
    farm12 = Tower(253, 432, 'h', lateGameCubizm)
    farm13 = Tower(435, 629, 'h', lateGameCubizm)
    farm14 = Tower(913, 828, 'h', lateGameCubizm)
    farm15 = Tower(1076, 834, 'h', lateGameCubizm)
    farm16 = Tower(1077, 693, 'h', lateGameCubizm)
    farm17 = Tower(1245, 621, 'h', lateGameCubizm)
    farm18 = Tower(1116, 480, 'h', lateGameCubizm)
    farm19 = Tower(953, 454, 'h', lateGameCubizm)
    farm20 = Tower(788, 503, 'h', lateGameCubizm)
    farm21 = Tower(1408, 591, 'h', lateGameCubizm)
    farm22 = Tower(1562, 450, 'h', lateGameCubizm)
    farm23 = Tower(1397, 450, 'h', lateGameCubizm)
    farm24 = Tower(1563, 309, 'h', lateGameCubizm)
    farm25 = Tower(1397, 309, 'h', lateGameCubizm)
    farm26 = Tower(1563, 167, 'h', lateGameCubizm)
    farm27 = Tower(1401, 167, 'h', lateGameCubizm)
    farm28 = Tower(1238, 67, 'h', lateGameCubizm)
    farm29 = Tower(1234, 211, 'h', lateGameCubizm)
    farm30 = Tower(1071, 158, 'h', lateGameCubizm)
    farm31 = Tower(770, 68, 'h', lateGameCubizm)
    farm32 = Tower(608, 67, 'h', lateGameCubizm)
    farm33 = Tower(446, 69, 'h', lateGameCubizm)
    farm34 = Tower(233, 69, 'h', lateGameCubizm)
    farm35 = Tower(231, 210, 'h', lateGameCubizm)
    farm36 = Tower(437, 210, 'h', lateGameCubizm)
    farm37 = Tower(602, 210, 'h', lateGameCubizm)
    farm38 = Tower(603, 351, 'h', lateGameCubizm)

    sub1 = Tower(792, 341, 'x', lateGameCubizm)
    alch1 = Tower(730, 245, 'f', lateGameCubizm)
    alch2 = Tower(839, 450, 'f', lateGameCubizm)
    boat1 = Tower(982, 304, 'c', lateGameCubizm)

    cannon1 = Tower(757, 451, 'e', lateGameCubizm)
    cannon2 = Tower(847, 470, 'e', lateGameCubizm)
    tack1 = Tower(488, 421, 'r', lateGameCubizm)
    glue1 = Tower(412, 378, 'y', lateGameCubizm)
    sniper1 = Tower(732, 665, 'z', lateGameCubizm)
    wizard1 = Tower(936, 609, 'a', lateGameCubizm)
    wizard2 = Tower(577, 725, 'a', lateGameCubizm)
    engineer1 = Tower(804, 557, 'l', lateGameCubizm)
    engineer2 = Tower(493, 972, 'l', lateGameCubizm)
    village1 = Tower(616, 385, 'k', lateGameCubizm)
    super1 = Tower(697, 531, 's', lateGameCubizm)
    super2 = Tower(1154, 197, 's', lateGameCubizm)
    super3 = Tower(1330, 188, 's', lateGameCubizm)
    super4 = Tower(708, 698, 's', lateGameCubizm)
    ice1 = Tower(474, 568, 't', lateGameCubizm)
    dartling1 = Tower(860, 637, 'm', lateGameCubizm)

    while 1:
        time.sleep(1)
        waitingForEnd = 1
        checkForLevelUp(lateGameCubizm)
        hero.p()
        dart1.p()
        pyautogui.press("space")
        pyautogui.press("space")
        farm1.p(1,2,3,3)
        farm2.p(1, 2, 3, 3)
        farm3.p(1, 2, 3, 3)
        dart1.u(3,3, 2, 2)
        farm4.p(1,2,3,3)
        farm5.p(1, 2, 3, 3)
        farm6.p(1, 2, 3, 3)
        farm7.p(1, 2, 3, 3)
        farm8.p(1, 2, 3, 3)
        farm9.p(1, 2, 3, 3)
        sub1.p(1, 2,3, 3)
        farm10.p(1, 2, 3, 3)
        farm11.p(1, 2, 3, 3)
        farm12.p(1, 2)

        while waitingForEnd:
            if checkForGameEnd(lateGameCubizm, None, 3) == 1:
                waitingForEnd = 0
        farm12.u(3, 3)

        farm13.p(1, 2, 3, 3)
        farm14.p(1, 2, 3, 3)
        farm15.p(1, 2, 3, 3)
        farm16.p(1, 2, 3, 3)
        farm17.p(1, 2, 3, 3)
        farm18.p(1, 2, 3, 3)
        farm19.p(1, 2, 3, 3)
        farm20.p(1, 2, 3, 3) ####
        farm21.p(1, 2, 3, 3)
        farm22.p(1, 2, 3, 3)
        farm23.p(1, 2, 3, 3)
        farm24.p(1, 2, 3, 3)
        farm25.p(1, 2, 3, 3)
        alch1.p(1, 4, 3, 1)
        farm26.p(1,2,3,3)
        farm27.p(1,2,3,3)
        farm28.p(1,2,3,3)
        farm29.p(1,2,3,3)
        farm30.p(1,2,3,3)
        farm31.p(1,2,3,3)
        farm32.p(1,2,3,3)
        farm33.p(1,2,3,3)
        farm34.p(1,2,3,3)
        farm35.p(1,2,3,3)
        farm36.p(1,2,3,3)
        farm37.p(1,2,3,3)
        farm38.p(1,2,3,3)
        sub1.u(3, 2)
        farm1.u(3, 2)
        boat1.p(2, 2, 3, 5)
        farm20.s()
        dart1.s()
        super1.p(1, 3)
        cannon1.p(1, 5, 3, 2)
        tack1.p(2, 4, 3, 2)
        wizard1.p(2, 5)
        engineer1.p(3, 5)
        super1.u(1, 1, None, None, None, 1)
        ### Upgrading to temple
        # pyautogui.click(697, 531)
        # time.sleep(.5)
        # pyautogui.press("'")
        # time.sleep(.5)
        # pyautogui.click(1133, 730)

        village1.p(2, 3, 1, 2)

        ### add detection for round 100, then sell everything and continue into freeplay
        waitingForEnd = 1
        while waitingForEnd:
            if checkForGameEnd(lateGameCubizm, None, 2) == 1:
                waitingForEnd = 0

        farm1.s()
        farm2.s()
        farm3.s()
        farm4.s()
        farm5.s()
        farm6.s()
        farm7.s()
        farm8.s()
        farm9.s()
        farm10.s()
        farm11.s()
        farm12.s()
        farm13.s()
        farm14.s()
        farm15.s()
        farm16.s()
        farm17.s()
        farm18.s()
        farm19.s()
        farm20.s()
        farm21.s()
        farm22.s()
        farm23.s()
        farm24.s()
        farm25.s()
        farm26.s()
        farm27.s()
        farm28.s()
        farm29.s()
        farm30.s()
        farm31.s()
        farm32.s()
        farm33.s()
        farm34.s()
        farm35.s()
        farm36.s()
        farm37.s()
        farm38.s()

        super2.p(1, 2, 2, 5)
        super3.p(1, 2, 3, 5)
        cannon2.p(1, 5, 2, 2)
        ice1.p(1, 5, 3, 2)
        dartling1.p(1, 5, 3, 2)
        super4.p(1, 2, 3, 4)
        wizard2.p(1, 4)
        engineer2.p(2, 5)
        super1.u(1, 1, None, None, None, 1)
        ### Upgrading to Max temple
        # pyautogui.click(697, 531)
        # time.sleep(.5)
        # pyautogui.press("'")
        # time.sleep(.5)
        # pyautogui.click(1133, 730)

        ice1.p(1, 5, 3, 2)
        village1.p(1, 2, 2, 5)
        alch2.p(1, 5, 3, 1)
        glue1.p(2, 2, 3, 5)

        ## Round 200 insta
        waitingForEnd = 1
        while waitingForEnd:
            if checkForGameEnd(lateGameCubizm, None, 2) == 1:
                waitingForEnd = 0

        waitingForEnd = 1
        while waitingForEnd:
            if checkForGameEnd(lateGameCubizm, None, 1) == 1:
                waitingForEnd = 0

### USE QUINCY
def hedgeCoopABR():
    hero = Tower(448, 519, 'u', hedgeCoopABR)
    dart = Tower(321, 508, 'q', hedgeCoopABR)
    alch = Tower(330, 641, 'f', hedgeCoopABR)
    tack = Tower(186, 550, 'r', hedgeCoopABR)
    ninja = Tower(446, 613, 'd', hedgeCoopABR)
    village = Tower(303, 415, 'k', hedgeCoopABR)
    while 1:
        time.sleep(1)
        waitingForEnd = 1
        checkForLevelUp(hedgeCoopABR)
        pyautogui.press("space")
        time.sleep(1)
        pyautogui.press("space")
        hero.p(None, None, None, None, 1)
        dart.p(2, 1, 3, 2, 1)
        ninja.p(1, 3, 3, 1, 1)
        alch.p(1, 4, 2, 2, 1)
        ninja.u(1, 1)
        dart.u(2, 1, 3, 3)
        village.p(1, 3, 2, 2, 1)
        tack.p(1, 2, 3, 5, 1)
        ### GO into freeplay
        while waitingForEnd:
            if checkForGameEnd(lateGameCubizm, None, 3) == 1:
                waitingForEnd = 0
        alch.u(1, 1,)
        ninja.u(1, 1)
        waitingForEnd = 1
        while waitingForEnd:
            if checkForGameEnd(hedgeCoopABR, None, 4) == 4:
                waitingForEnd = 0
def infernalEasy():
    dart = Tower(470, 274, 'q', infernalEasy)
    hero = Tower(836, 697, 'u', infernalEasy)
    sniper = Tower(1577, 534, 'z', infernalEasy)
    sub1 = Tower(1150, 232, 'x', infernalEasy)
    sub2 = Tower(1246, 223, 'x', infernalEasy)

    while 1:
        time.sleep(2)
        waitingForEnd = 1
        checkForLevelUp(darkCastle)
        pyautogui.press("space")
        pyautogui.press("space")
        hero.p()
        dart.p()
        sub1.p(1, 2, 3, 3)
        sub2.p(1, 2, 3, 3)
        sniper.p(1, 2, 3, 4)
        while waitingForEnd:
            if checkForGameEnd(infernalEasy, None, 5) == 1:
                waitingForEnd = 0
def quadEasy():
    dart = Tower(1271, 526, 'q', quadEasy)
    hero = Tower(716, 796, 'u', quadEasy)
    sniper = Tower(1300, 900, 'z', quadEasy)
    alch = Tower(1455, 446, 'f', quadEasy)
    sub1 = Tower(750, 490, 'x', quadEasy)
    sub2 = Tower(850, 490, 'x', quadEasy)

    while 1:
        time.sleep(2)
        waitingForEnd = 1
        checkForLevelUp(darkCastle)
        pyautogui.press("space")
        pyautogui.press("space")
        hero.p()
        dart.p()
        sub1.p(1, 2, 3, 3)
        sniper.p(1, 2, 3, 4)
        sub2.p(1, 2, 3, 3)
        while waitingForEnd:
            if checkForGameEnd(quadEasy, None, 5) == 1:
                waitingForEnd = 0
def darkCastleEasy():
    dart = Tower(575, 485, 'q', darkCastleEasy)
    hero = Tower(734, 437, 'u', darkCastleEasy)
    sniper = Tower(1000, 200, 'z', darkCastleEasy)
    alch = Tower(1455, 446, 'f', darkCastleEasy)
    sub1 = Tower(1094, 429, 'x', darkCastleEasy)
    sub2 = Tower(1229, 424, 'x', darkCastleEasy)

    while 1:
        time.sleep(2)
        waitingForEnd = 1
        checkForLevelUp(darkCastle)
        pyautogui.press("space")
        pyautogui.press("space")
        hero.p()
        dart.p()
        sub1.p(1, 2, 3, 3)
        sniper.p(1, 2, 3, 4)
        sub2.p(1, 2, 3, 3)
        while waitingForEnd:
            if checkForGameEnd(darkCastleEasy, None, 5) == 1:
                waitingForEnd = 0
def workshopEasy():
    dart = Tower(906, 490, 'q', workshopEasy)
    hero = Tower(1006, 488, 'u', workshopEasy)
    heli = Tower(500, 470, 'b', workshopEasy)
    alch = Tower(665, 474, 'f', workshopEasy)
    ninja = Tower(1187, 418, 'd', workshopEasy)
    alch2 = Tower(1189, 327, 'f', workshopEasy)
    spike = Tower(1599, 650, 'j', workshopEasy)
    while 1:
        time.sleep(2)
        waitingForEnd = 1
        checkForLevelUp(darkCastle)
        pyautogui.press("space")
        pyautogui.press("space")
        hero.p()
        dart.p()
        heli.p(1, 3, 2, 2)
        alch.p(1, 4, 3, 1)
        ninja.p(1, 4, 3, 2)
        alch2.p(1, 3)
        spike.p(2, 1, 3, 1)
        while waitingForEnd:
            if checkForGameEnd(workshopEasy, None, 5) == 1:
                waitingForEnd = 0
def muddypuddlesEasy():
    dart = Tower(1128, 837, 'q', muddypuddlesEasy)
    hero = Tower(584, 339, 'u', muddypuddlesEasy)
    sniper = Tower(698, 27, 'z', muddypuddlesEasy)
    sub1 = Tower(1202, 456, 'x', muddypuddlesEasy)
    sub2 = Tower(701, 733, 'x', muddypuddlesEasy)

    while 1:
        time.sleep(2)
        waitingForEnd = 1
        checkForLevelUp(darkCastle)
        pyautogui.press("space")
        pyautogui.press("space")
        hero.p()
        dart.p(3, 2)
        sub1.p(1, 2, 3, 3)
        sub2.p(1, 2, 3, 3)
        sniper.p(1, 2, 3, 4)
        while waitingForEnd:
            if checkForGameEnd(infernalEasy, None, 5) == 1:
                waitingForEnd = 0
def ravineEasy():
    dart = Tower(283, 668, 'q', ravineEasy)
    hero = Tower(739, 809, 'u', ravineEasy)
    heli = Tower(683, 149, 'b', ravineEasy)
    alch = Tower(851, 209, 'f', ravineEasy)
    ninja = Tower(380, 719, 'd', ravineEasy)
    alch2 = Tower(478, 770, 'f', ravineEasy)

    while 1:
        time.sleep(2)
        waitingForEnd = 1
        checkForLevelUp(darkCastle)
        pyautogui.press("space")
        pyautogui.press("space")
        hero.p()
        dart.p()
        heli.p(1, 3, 2, 2)
        alch.p(1, 4, 3, 1)
        ninja.p(1, 4, 3, 2)
        alch2.p(1, 3)
        while waitingForEnd:
            if checkForGameEnd(infernalEasy, None, 5) == 1:
                waitingForEnd = 0
def ouchEasy():
    dart = Tower(1018, 666, 'q', ouchEasy)
    hero = Tower(671, 417, 'u', ouchEasy)
    sniper = Tower(1400, 1000, 'z', ouchEasy)
    sub1 = Tower(720, 605, 'x', ouchEasy)
    sub2 = Tower(954, 470, 'x', ouchEasy)

    while 1:
        time.sleep(2)
        waitingForEnd = 1
        checkForLevelUp(darkCastle)
        pyautogui.press("space")
        pyautogui.press("space")
        hero.p()
        dart.p(3, 2)
        sub1.p(1, 2, 3, 3)
        sniper.p(1, 2, 3, 3)
        sub2.p(1, 2, 3, 3)
        while waitingForEnd:
            if checkForGameEnd(infernalEasy, None, 5) == 1:
                waitingForEnd = 0
def floodedvalleyEasy():

    boat1 = Tower(994, 204, 'c', floodedvalleyEasy)
    boat2 = Tower(1031, 722, 'c', floodedvalleyEasy)
    sub1 = Tower(1029, 929, 'x', floodedvalleyEasy)
    sub2 = Tower(1105, 349, 'x', floodedvalleyEasy)

    while 1:
        time.sleep(2)
        waitingForEnd = 1
        checkForLevelUp(darkCastle)
        pyautogui.press("space")
        pyautogui.press("space")
        sub1.p(1, 2, 3, 3)
        boat1.p(2, 2, 3, 2)
        sub2.p(1, 2, 3, 3)
        boat2.p(2, 2, 3, 2)
        while waitingForEnd:
            if checkForGameEnd(infernalEasy, None, 5) == 1:
                waitingForEnd = 0
def bloodypuddlesEasy():
    dart = Tower(375, 623, 'q', bloodypuddlesEasy)
    hero = Tower(1109, 510, 'u', bloodypuddlesEasy)
    sniper = Tower(724, 25, 'z', bloodypuddlesEasy)
    sub1 = Tower(645, 724, 'x', bloodypuddlesEasy)
    sub2 = Tower(1173, 189, 'x', bloodypuddlesEasy)

    while 1:
        time.sleep(2)
        waitingForEnd = 1
        checkForLevelUp(darkCastle)
        pyautogui.press("space")
        pyautogui.press("space")
        hero.p()
        dart.p(3, 2)
        sub1.p(1, 2, 3, 3)
        sub2.p(1, 2, 3, 3)
        sniper.p(1, 2, 3, 4)
        while waitingForEnd:
            if checkForGameEnd(infernalEasy, None, 5) == 1:
                waitingForEnd = 0

# Coords, (x, y), then page number
expertMapBonuses = {(689, 290, 0): ravineEasy, (1112, 290, 0): floodedvalleyEasy, (1536, 290, 0): infernalEasy,
                    (688, 603, 0): bloodypuddlesEasy, (1112, 603, 0): workshopEasy, (1536, 603, 0): quadEasy,
                    (689, 290, 1): darkCastleEasy, (1112, 290, 1): muddypuddlesEasy, (1536, 290, 1): ouchEasy}


def collectionEvent():
    time.sleep(1)

    if pyautogui.pixelMatchesColor(950, 652, (114, 232, 0), tolerance=10):
        pyautogui.click(950, 652)
        time.sleep(1)
        pyautogui.click(821, 534)
        time.sleep(.7)
        pyautogui.click()
        pyautogui.click(1105, 538)
        time.sleep(.7)
        pyautogui.click()
        time.sleep(.7)
        pyautogui.click()
        time.sleep(2)
        pyautogui.click(100, 25)
    # Clicks the play button
    time.sleep(1)
    pyautogui.click(837, 933)
    time.sleep(1)
    # Clicks onto the expert button
    pyautogui.click(1340, 969)
    try:
        time.sleep(.5)
        # Finds bonus reward button
        x, y = pyautogui.locateCenterOnScreen('bonusReward.png', confidence=0.8)
        print(x, y, "COORDS")
    except TypeError:
        pyautogui.click(1340, 969)
        time.sleep(.5)
        x, y = pyautogui.locateCenterOnScreen('bonusReward.png', confidence=0.8)
    # Check for which page you are on
    if pyautogui.pixelMatchesColor(1089, 753, (64, 159, 255), tolerance=10):
        pageNumber = 0
    else:
        pageNumber = 1
    time.sleep(.5)
    # Clicks onto the map with bonus reward
    pyautogui.click(x, y)
    time.sleep(.5)
    # Clicks onto easy button
    pyautogui.click(631, 417)
    time.sleep(.5)
    # Press the "easy" button
    pyautogui.click(630, 579)
    # Check for overwrite save
    if y == 289:
        y = 290
    time.sleep(.5)
    if pyautogui.pixelMatchesColor(1194, 723, (99, 219, 0), tolerance=10):
        pyautogui.click(1194, 723)
    expertMapBonuses[(x, y, pageNumber)]()

#darkCastle()
#darkCastleImpoppable()
#lateGameCubizm()
#hedgeCoopABR()
collectionEvent()
