# Hiba Hamad, hhamad
# Project Name: Bloon Battles

import math
import pygame
from sys import exit 

#initiallizing pygame
pygame.init()

#initiallizing screen display, setting color to pink
screen = pygame.display.set_mode((890,735))
screen.fill('Pink')

#naming display screen, also name of the game, 'Bloon Battles'
pygame.display.set_caption('Bloon Battles')

#initiallizing clock
clock = pygame.time.Clock()

#loading map and game bar images
test_surface = pygame.image.load('graphics/map-11.png').convert_alpha()
game_bar = pygame.image.load('graphics/game-bar2.png').convert_alpha()

#loading balloon and popped balloon images
b = pygame.image.load('graphics/balloon.png').convert_alpha()
pop = pygame.image.load('graphics/popped-balloon.png').convert_alpha()

#setting initial health to 20
healthBar = 20

# Displays a balloon
# When put in while loop, balloon moves to the end of the map
class Balloons:
    def __init__(self,b,x):

        #initiallizing variables
        self.x = x
        self.y = 85
        self.balloon = b

    ## ROUND 1
    #displays inputted balloon on screen + makes into rectangle
    #moves balloon at a slow speed when in main loop
    def round1(self):

        self.rect = self.balloon.get_rect(topleft=(self.x,self.y))
        screen.blit(self.balloon,self.rect)

        if self.x<495:
            self.x += 1
            
        if self.x>=494 and self.y<265:
            self.y += 1
        
        if self.y>=264 and self.x<640:
            self.x += 1
            
        if self.x>=639 and self.y<800:
            self.y += 1

    ## ROUND 2
    #displays inputted balloon on screen + makes into rectangle
    #moves balloon at a medium speed when in main loop
    def round2(self):

        self.rect = self.balloon.get_rect(topleft=(self.x,self.y))
        screen.blit(self.balloon,self.rect)
        
        if self.x<495:
            self.x += 1.5
            
        if self.x>=494 and self.y<265:
            self.y += 1.5
        
        if self.y>=264 and self.x<640:
            self.x += 1.5
            
        if self.x>=639 and self.y<800:
            self.y += 1.5

    #returns true if balloon is passing the map border,
    #otherwise, returns false
    def checkPassing(self):

        if self.rect.top>735:
            return True
        
        return False

    #returns true if balloon is colliding with given item,
    #otherwise, returns false
    def isColliding(self,item):

        if self.rect.colliderect(item):
            return True

        return False

    #returns current center position of balloon
    def balloonPos(self):

        return (self.rect.centerx,self.rect.centery)

    ## ROUND 1 Balloons
    ## Contains 15 balloons 
    def round1Balloons(self):
        
        self.dB1 = Balloons(b,100)
        self.dB2 = Balloons(b,60)
        self.dB3 = Balloons(b,20)
        self.dB4 = Balloons(b,-20)
        self.dB5 = Balloons(b,-60)
        self.dB6 = Balloons(b,-100)
        self.dB7 = Balloons(b,-140)
        self.dB8 = Balloons(b,-180)
        self.dB9 = Balloons(b,-220)
        self.dB10 = Balloons(b,-260)
        self.dB11 = Balloons(b,-300)
        self.dB12 = Balloons(b,-340)
        self.dB13 = Balloons(b,-380)
        self.dB14 = Balloons(b,-420)
        self.dB15 = Balloons(b,-460)
            
        return [
        self.dB1,self.dB2,self.dB3,self.dB4,
        self.dB5,self.dB6,self.dB7,self.dB8,
        self.dB9,self.dB10,self.dB11,self.dB12,
        self.dB13,self.dB14,self.dB15]

    ## ROUND 1 Balloons
    ## Contains 20 balloons 
    def round2Balloons(self):

        self.dB1 = Balloons(b,100)
        self.dB2 = Balloons(b,60)
        self.dB3 = Balloons(b,20)
        self.dB4 = Balloons(b,-20)
        self.dB5 = Balloons(b,-60)
        self.dB6 = Balloons(b,-100)
        self.dB7 = Balloons(b,-140)
        self.dB8 = Balloons(b,-180)
        self.dB9 = Balloons(b,-220)
        self.dB10 = Balloons(b,-260)
        self.dB11 = Balloons(b,-300)
        self.dB12 = Balloons(b,-340)
        self.dB13 = Balloons(b,-380)
        self.dB14 = Balloons(b,-420)
        self.dB15 = Balloons(b,-460)
        self.dB16 = Balloons(b,-500)
        self.dB17 = Balloons(b,-540)
        self.dB18 = Balloons(b,-580)
        self.dB19 = Balloons(b,-620)
        self.dB20 = Balloons(b,-660)
        self.dB21 = Balloons(b,-700)
        self.dB22 = Balloons(b,-740)
        self.dB23 = Balloons(b,-780)
        self.dB24 = Balloons(b,-820)
        self.dB25 = Balloons(b,-860)
            
        return [
        self.dB1,self.dB2,self.dB3,self.dB4,
        self.dB5,self.dB6,self.dB7,self.dB8,
        self.dB9,self.dB10,self.dB11,self.dB12,
        self.dB13,self.dB14,self.dB15,self.dB16,
        self.dB17,self.dB18,self.dB19,self.dB20,
        self.dB21,self.dB22,self.dB23]
        
#contains a list of instances (and additional empty list for iteration)
#each instance is a list of instances for the incoming balloons each round
allRounds = [Balloons(b,0).round1Balloons(),Balloons(b,0).round2Balloons()]
                   
#Displays spikes on screen
#User can move spikes (only once) to the balloon path in the map
#Each bundle of spikes pops 6 balloons
class AllSpikes:
    #initiallizes all variables, loads spikes images,
    #calls functions to display spikes on screen
    def __init__(self):
    
        self.count = 0
        self.spikesDamage = 0
        currentX = 0
        currentY = 0
        self.moving = False
        
        self.spikesImg1 = pygame.image.load('graphics/spikes1.png').convert_alpha()
        self.spikesImg1 = pygame.transform.scale(self.spikesImg1,(60,60))
        
        self.spikesImg2 = pygame.image.load('graphics/spikes2.png').convert_alpha()
        self.spikesImg2 = pygame.transform.scale(self.spikesImg2,(60,60))
        
        self.spikesImg3 = pygame.image.load('graphics/spikes3.png').convert_alpha()
        self.spikesImg3 = pygame.transform.scale(self.spikesImg3,(60,60))

        self.moving = False
        self.placed = False
        self.spikesCord = (80,480)

        self.assignSpikes()
        self.displaySpikes()

    #displays spikes images on screen
    def displaySpikes(self):
        
        #updates image of spikes displayed on screen
        #spikes appear to be less for every two balloons popped
        if self.spikesDamage==0 or self.spikesDamage==1:
            self.item = self.spikesImg1
            self.itemR = self.item.get_rect(center=self.spikesCord)
        if self.spikesDamage==2 or self.spikesDamage==3:
            self.item = self.spikesImg2
            self.itemR = self.item.get_rect(center=self.spikesCord)
        if self.spikesDamage>=4:
            self.item = self.spikesImg3
            self.itemR = self.item.get_rect(center=self.spikesCord)

        #displays spikes on screen if they are still active
        #spikes are active if they've popped less than 6 balloons
        if self.spikesDamage!=6:
            screen.blit(self.item,self.itemR)

        #when current spikes are no longer active,
        #next spikes are displayed on screen
        #if player used all spikes (total 3), spikes disappear
        if self.spikesDamage==6 and self.count!=2:
            self.placed = False
            self.spikesCord = (80,495)
            self.spikesDamage=0
            self.count+=1

    #returns true is balloon is colliding with spikes
    #otherwise returns false
    def popBalloon(self,balloon):
        global displayBalloon1
        
        if balloon.isColliding(self.itemR) and (
            self.spikesDamage<6 and self.moving) == False:
            self.spikesDamage += 1
            return True

        return False

    #assign currents spikes bundle to screen
    def assignSpikes(self):

        #saving values for each spikes bundles
        self.spikes_select1 = self.spikesImg1
        self.spikes_select_rect1 = self.spikes_select1.get_rect(center=
                                                                self.spikesCord)
        self.spikes_select2 = self.spikesImg1
        self.spikes_select_rect2 = self.spikes_select2.get_rect(center=
                                                                self.spikesCord)
        self.spikes_select3 = self.spikesImg1
        self.spikes_select_rect3 = self.spikes_select3.get_rect(center=
                                                                self.spikesCord)
        
        #updates current spikes displayed on screen
        if self.count==0:
            self.item,self.itemR = (self.spikes_select1,self.spikes_select_rect1)
            
        if self.count==1:
            self.item,self.itemR = (self.spikes_select2,self.spikes_select_rect2)
            
        if self.count==2:
            self.item,self.itemR = (self.spikes_select3,self.spikes_select_rect3)

    # source: https://pygame.readthedocs.io/en/latest/3_image/image.html
    #moves an image, which user holds mouse button on, alongside cursor 
    def moveSpikes(self,event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.itemR.collidepoint(event.pos):
                self.moving = True
                
        elif event.type == pygame.MOUSEBUTTONUP:
            self.moving = False
            self.placed = True

        elif event.type == pygame.MOUSEMOTION:
            if self.moving==True and self.placed==False:
                self.spikesCord = event.pos

#Displays character, Bibbo, on screen
#User can drag Bibbo on screen
#Bibbo shoots feather darts to pop balloons
class Bibbo(pygame.sprite.Sprite):

    def __init__(self):

        #initiallizing sprite class
        super().__init__()

        #loading Bibbo image, creating rect for image
        self.default_bird = pygame.image.load('graphics/bibbo.png').convert_alpha()
        self.default_bird = pygame.transform.rotate(self.default_bird, 180)
        self.rect = self.default_bird.get_rect(center=(600,250))

        #top left of bibbo's range
        self.rangeStr = (self.rect.left-100,self.rect.top-100)
        #bottom right of bibbo's range
        self.rangeFin = (self.rect.right+100,self.rect.bottom+100)
        #middle of bibbo's range
        self.rangeMid = ((self.rangeStr[0]+self.rangeFin[0])/2,
                         (self.rangeStr[1]+self.rangeFin[1])/2)
        

        #bibbo's initial angle rotation is 0
        self.angle = 0

        #initiallizing variables for angle of player
        self.quad = None
        self.angleTaken = False

        #initiallizing variable for shooting status of bibbo
        self.canShoot = True

        #initiallizing variables for tracking time
        self.currentTime = 0
        self.dartTime = 0
        self.counting = True

    #if given balloon is colliding with bibbo's range,
    #gets angle bibbo needs to rotate at to face the balloon,
    #also calls function to shoot at balloon
    def getAngleCallShoot(self,balloon):

        #saving current balloon's center position
        self.balloonPos = balloon.balloonPos()

        #checks if balloon is colliding with bibbo's range
        if self.balloonPos[0]>self.rangeStr[0] and self.balloonPos[0]<self.rangeFin[0]:
            if self.balloonPos[1]>self.rangeStr[1] and (
                self.balloonPos[1]<self.rangeFin[1]):
                #calculating angle using arc tangent 
                self.diffX = self.rangeMid[0]-self.balloonPos[0]
                self.diffY = self.rangeMid[1]-self.balloonPos[1]
                if self.diffY==0:
                    self.angleTemp = 0
                else: self.angleTemp = abs(math.degrees(math.atan(
                                                self.diffX/self.diffY)))
                #calls functions to change angle according to..
                #quadrant of the balloon collision
                self.checkQuad()
                #if shooting is valid,
                #calls function to shoot a dart at the balloon,
                #saves dart to a group
                if self.canShoot == True:
                    self.dartAngle = self.angle
                    dart_group.add(bibboIns.createDart(balloon,
                            self.dartAngle,self.balloonPos[0],self.balloonPos[1]))

    #changes the angle depending on which quadrant...
    #..the balloon is colliding with bibbo's range
    def checkQuad(self):

        quad00 = self.rangeStr
        quad01 = ((self.rangeStr[0]+self.rangeFin[0])//2,self.rangeStr[1])
        quad02 = (self.rangeFin[0],self.rangeStr[1])

        quad10 = (self.rangeStr[0],(self.rangeStr[1]+self.rangeFin[1])//2)
        quad11 = ((self.rangeStr[0]+self.rangeFin[0])//2,
                  (self.rangeStr[1]+self.rangeFin[1])//2)
        quad12 = (self.rangeFin[0],(self.rangeStr[1]+self.rangeFin[1])//2)

        quad20 = (self.rangeStr[0],self.rangeFin[1])
        quad21 = ((self.rangeStr[0]+self.rangeFin[0])//2,self.rangeFin[1])
        quad22 = self.rangeFin

        #hold balloon's center position
        x = self.balloonPos[0]
        y = self.balloonPos[1]

        if y>quad00[1] and y<quad10[1]:
            #quad 1
            if x>quad01[0] and x<quad02[0]:
                self.quad = 1
                self.angle = -self.angleTemp

            #quad 2
            elif x>quad00[0] and x<quad01[0]:
                self.quad = 2
                self.angle = self.angleTemp

        elif y>quad10[1] and y<quad20[1]:

            #quad 3
            if x>quad00[0] and x<quad01[0]:
                self.quad = 3
                self.angle = 180 - self.angleTemp

            #quad 4
            elif x>quad01[0] and x<quad02[0]:
                self.quad = 4
                self.angle = 180 + self.angleTemp

    # source: https://www.youtube.com/watch?v=_TU6BEyBieE
    #diplays image of bibbo on screen
    #and rotates according to balloon collisions
    def blitRotate(self):

        self.img = pygame.transform.rotate(self.default_bird,self.angle)
                
        screen.blit(self.img,(self.rect.centerx-int(self.img.get_width()/2),
                              self.rect.centery-int(self.img.get_height()/2)))

    #creates a dart that shoots at given balloon at given angle
    def createDart(self,balloon,angle,balloonX,balloonY):

        self.canShoot = False

        return Darts(angle,self.quad,balloon,self.rangeMid[0],self.rangeMid[1],
                        balloonX,balloonY)

    #restricts bibbo to only shoot one dart per second
    def updateDartTime(self):

        self.currentTime = pygame.time.get_ticks()

        if self.canShoot == False and self.counting == True:
            self.counting = False
            self.dartTime = pygame.time.get_ticks()

        elif self.currentTime - self.dartTime > 1000:
            self.counting = True
            self.canShoot = True

#Creates a dart that shoots at given balloon
#Dart pops balloons at collision
class Darts(pygame.sprite.Sprite):
    def __init__(self,angle,quad,balloon,x1,y1,x2,y2):
        
        #initiallizing sprite class
        super().__init__()

        #loading images and change angle according to direction of balloon
        self.feather_dart = pygame.image.load('graphics/feather.png').convert_alpha()
        self.feather_dart = pygame.transform.rotate(self.feather_dart, 180)
        self.image = pygame.transform.rotate(self.feather_dart, angle)

        #initiallizing variables that hold dart and balloon position
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        #initiallizing variables for dart angle and position
        self.quad = quad
        self.m = angle/90

        #initializing variable to track number of balloons dart pops
        self.numPopped = 0

        #making a rect of the dart
        self.rect = self.image.get_rect(center=(self.x1,self.y1))

    #updates position of dart
    def update(self):
        
        if self.quad == 1:
            self.rect.x += 5*self.m
            self.rect.y -= 5
        if self.quad == 2:
            self.rect.x -= 5*self.m
            self.rect.y -= 5
        if self.quad == 3:
            self.rect.x -= 5*self.m
            self.rect.y += 5
        if self.quad == 4:
            self.rect.x += 5*self.m
            self.rect.y += 5

        #kills dart if it passes the map borders
        if self.rect.x>1000 or self.rect.y>1000:
            self.kill()

    #kills dart if it has popped 2 balloons
    #returns True if balloon collides with dart
    #otherwise returns False
    def popBalloon(self,balloon):

        if balloon.isColliding(self.rect) and self.numPopped<2:
            self.numPopped += 1
            return True

        if self.numPopped >= 2:
            self.kill()

        return False

#displays balloons of each round
#returns current round number and instance in a tuple
def displayBalloonRounds(currentTime):

    currentRound = (0,None)

    #displays round 1 balloons
    if currentTime>2 and currentTime<25:
        currentRound = (1,allRounds[0])
        for balloon in currentRound[1]:
            balloon.round1()

    #displays round 2 balloons
    if currentTime>=25:
        currentRound = (2,allRounds[1])
        for balloon in currentRound[1]:
            balloon.round2()

    return currentRound


#creates instance of the allSpikes class
spikesIns = AllSpikes()

#creates instance of Bibbo class
bibboIns = Bibbo()

#creates a player group for Bibbo instance
playerGroup = pygame.sprite.Group()
playerGroup.add(bibboIns)

#creates dart group
dart_group = pygame.sprite.Group()


# displays everything on game window
def drawPlayWindow():    
    global healthBar
    
    screen.blit(test_surface,(0,0)) #displays map

    currentTime = pygame.time.get_ticks()//1000 #tracks time in seconds

    #gets current round number and
    #list of instances of balloons in current round
    roundIns = displayBalloonRounds(currentTime)
    roundNum = roundIns[0]
    currentRound = roundIns[1]
        
    screen.blit(game_bar,(0,0)) #displays game bar on left

    spikesIns.assignSpikes() #updates spikes bundle
    spikesIns.displaySpikes() #updates spikes bundle image

    dart_group.draw(screen) #displays darts
    dart_group.update() #updates darts' positions

    #updates frequency at which bibbo can shoot darts
    bibboIns.updateDartTime() 
    bibboIns.blitRotate() #rotates bibbo to face balloons

    #checks if rounds started
    #calls functions to pop balloons or not
    if currentRound != None:

        for balloon in currentRound:
            bibboIns.getAngleCallShoot(balloon)
            
            if spikesIns.popBalloon(balloon):
                if balloon in currentRound:
                    currentRound.remove(balloon)
                    screen.blit(pop,balloon)
                    
            for dart in dart_group:
                if dart.popBalloon(balloon):
                    if balloon in currentRound:
                        currentRound.remove(balloon)
                        screen.blit(pop,balloon)

        for balloon in currentRound:
            #removes balloon from current round if it passes map border
            #also decreases health by one
            if balloon.checkPassing():
                if balloon in currentRound:
                    currentRound.remove(balloon)
                    healthBar -= 1 

    display_healthBar = (pygame.font.Font(None,30)).render(
        'HEALTH: '+ str(healthBar), False, 'white')

    display_roundNum = (pygame.font.Font(None,30)).render(
        'ROUND: '+ str(roundNum), False, 'white')

    #displays current health of player
    screen.blit(display_healthBar,(20,55))
    #displays current round number
    screen.blit(display_roundNum,(20,30))

#displays GAME OVER window
def gameOverWind():

    screen.blit(test_surface,(0,0)) #display map

    #displays words 'GAME OVER'
    screen.blit((pygame.font.Font(None,150)).render('GAME OVER',
                                                    False, 'red'),(200,300))

    #displays words 'click to start over'
    screen.blit((pygame.font.Font(None,50)).render('click to start over',
                                                    False, 'red'),(400,400))
    
#stores main loop of game
def main():
    global healthBar

    #infinite while loop 
    while True:
        #checking all events
        for event in pygame.event.get():

            #if players quits game, exit program
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #if player clicks on screen in game over window,
            #health is restored
            if event.type == pygame.MOUSEBUTTONDOWN and healthBar == 0:
                healthBar = 20

            #calls function to move spikes
            spikesIns.moveSpikes(event)

        #if player hasn't ran out of health, display game window
        if healthBar > 0:
            drawPlayWindow()

        #if player ran out of health, display game over window
        else:
            gameOverWind()

        #updates display every loop        
        pygame.display.update()
        clock.tick(60) #makes while loop run 60 times per second

#calling main loop
main()







    

