# import the necessary packages
import numpy as np
import argparse
import cv2

from HandClasses import *

import pygame as game

from App import *
from VerletPhysics import *
from Fits import *
from Camera import *
# define the list of boundaries
lowerblue = np.array([75, 79, 107])
higherblue = np.array([103,151,155])

loweryellow = np.array([29,58,146])
higheryellow = np.array([74,115,240])

lowerpurple = np.array([110,35,150])
higherpurple = np.array([159,147,218])

lowergreen = np.array([47,41,135])
highergreen = np.array([80,156,255])

lowernewgreen = np.array([59,48,163])
highernewgreen = np.array([94,176,255])

todaylowgreen = np.array([55,237,67])
todayhighgreen = np.array([107,255,227])

todaylowgreen = np.array([64,163,88])
todayhighgreen = np.array([107,255,249])

#lowernewgreen = np.array([57,41,231])
#highernewgreen = np.array([93,140,255])



class DemoRope(App):
    #
    world    = World(Vector(640.0, 480.0), Vector(0, 0), 4)
    #
    grabbed  = None
    radius   = 15
    strength = 0.05
    #camera selection
    cameraString = 'WebCam'
    #
    def Initialize(self):
        #
        rope = self.world.AddComposite()
        #self.cap = cv2.VideoCapture(0)
        self.hand1 = HandClassOneColor([[]])

        mat = Material(1.0,1.0,1.0)
        rope.AddParticles(
            self.world.AddParticle(20.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(40.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(60.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(80.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(100.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(120.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(140.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(160.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(180.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(200.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(220.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(240.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(260.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(280.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(300.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(320.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(340.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(360.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(380.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(400.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(420.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(440.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(460.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(480.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(500.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(520.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(540.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(560.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(580.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(600.0,self.world.hsize.y,Material(1.0,0.0,1.0)),
            self.world.AddParticle(620.0,self.world.hsize.y,Material(1.0,0.0,1.0))
        )
        
        rope.AddConstraints(
            self.world.AddConstraint(rope.particles[0], rope.particles[1], 1.0),
            self.world.AddConstraint(rope.particles[1], rope.particles[2], 1.0),
            self.world.AddConstraint(rope.particles[2], rope.particles[3], 1.0),
            self.world.AddConstraint(rope.particles[3], rope.particles[4], 1.0),
            self.world.AddConstraint(rope.particles[4], rope.particles[5], 1.0),
            self.world.AddConstraint(rope.particles[5], rope.particles[6], 1.0),
            self.world.AddConstraint(rope.particles[6], rope.particles[7], 1.0),
            self.world.AddConstraint(rope.particles[7], rope.particles[8], 1.0),
            self.world.AddConstraint(rope.particles[8], rope.particles[9], 1.0),
            self.world.AddConstraint(rope.particles[9], rope.particles[10], 1.0),
            self.world.AddConstraint(rope.particles[10], rope.particles[11], 1.0),
            self.world.AddConstraint(rope.particles[11], rope.particles[12], 1.0),
            self.world.AddConstraint(rope.particles[12], rope.particles[13], 1.0),
            self.world.AddConstraint(rope.particles[13], rope.particles[14], 1.0),
            self.world.AddConstraint(rope.particles[14], rope.particles[15], 1.0),
            self.world.AddConstraint(rope.particles[15], rope.particles[16], 1.0),
            self.world.AddConstraint(rope.particles[16], rope.particles[17], 1.0),
            self.world.AddConstraint(rope.particles[17], rope.particles[18], 1.0),
            self.world.AddConstraint(rope.particles[18], rope.particles[19], 1.0),
            self.world.AddConstraint(rope.particles[19], rope.particles[20], 1.0),
            self.world.AddConstraint(rope.particles[20], rope.particles[21], 1.0),
            self.world.AddConstraint(rope.particles[21], rope.particles[22], 1.0),
            self.world.AddConstraint(rope.particles[22], rope.particles[23], 1.0),
            self.world.AddConstraint(rope.particles[23], rope.particles[24], 1.0),
            self.world.AddConstraint(rope.particles[24], rope.particles[25], 1.0),
            self.world.AddConstraint(rope.particles[25], rope.particles[26], 1.0),
            self.world.AddConstraint(rope.particles[26], rope.particles[27], 1.0),
            self.world.AddConstraint(rope.particles[27], rope.particles[28], 1.0),
            self.world.AddConstraint(rope.particles[28], rope.particles[29], 1.0),
            self.world.AddConstraint(rope.particles[29], rope.particles[30], 1.0)
        )

        rope.particles[0].material.mass = 0.0
        rope.particles[-1].material.mass = 0.0
        self.camera = Camera(self.cameraString)
        #rope.particles[9].ApplyForce(Vector(400.0, -900.0))


    #
    def Update(self):
        #
        if self.hand1.numberofFingers == 3 and self.hand1.state=='Closed':
            if self.grabbed == None:
                closest = self.ClosestPoint()
                if closest[1] < self.radius:
                    self.grabbed = closest[0]
                #print('here')
            if self.grabbed != None:
                mouse    = Vector(self.hand1.centerTriangle[0],self.hand1.centerTriangle[1])
                force = (mouse - self.grabbed.position) * self.strength
                self.grabbed.ApplyImpulse(force)
                #print('here2')        
                self.world.Simulate()
        elif game.mouse.get_pressed()[0]:
            if self.grabbed == None:
                closest = self.ClosestPoint()
                if closest[1] < self.radius:
                    print("here")
                    self.grabbed = closest[0]
            if self.grabbed != None:
                mouse = Vector(game.mouse.get_pos()[0], game.mouse.get_pos()[1])
                force = (mouse - self.grabbed.position) * self.strength
                self.grabbed.ApplyImpulse(force)
            self.world.Simulate()
        else:
            if self.grabbed != None:
                self.world.SimulateWorldStop() 
                self.grabbed = None
            #print('here3')

        success, image = self.camera.getFrame()

        if not success:
            print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        else:
            inputimage = cv2.flip(image.copy(),1)
            # Flip the image horizontally for a later selfie-view display, and convert
            # the BGR image to RGB.
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image_rgb = image.copy()
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            #results = hands.process(image)

            # Draw the hand annotations on the image.
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            frame_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            image_height, image_width, _ = image.shape
            maskgreen = MaskClass(frame_HSV.copy(),todaylowgreen,todayhighgreen)
            maskgreen.process()
            #cv2.imshow('green',maskgreen.tagged)
            
            fullcenters = []
            fullcenters.append(maskgreen.centers)
            #fullcenters.append(maskyellow.centers)
            self.hand1 = HandClassOneColor(fullcenters)
            #print(len(fullcenters[0]))
            font = cv2.FONT_HERSHEY_PLAIN
            if self.hand1.numberofFingers == 3:
                #print(str(self.hand1.area) + ' ' +str(self.hand1.state))
                cv2.putText(inputimage, 'Hand'+ str(self.hand1.state), (image_width-200,25), font, 2, (120,120,0), 3)
                #print(self.hand1.centerTriangle)
            else: 
                cv2.putText(inputimage, 'Not Right Hand', (image_width-300,25), font, 2, (120,120,0), 3)  

            masksum = maskgreen.tagged
            #
            self.cv_inputimage = inputimage
            self.cv_masksumimage = masksum
            self.cv_greenfiltered = maskgreen.tagged
            
            cv2.imshow('input-image',self.cv_inputimage)
            bin = cv2.waitKey(5)
            
            cv2.imshow('gree-filter',self.cv_greenfiltered)
        if game.key.get_pressed()[game.K_ESCAPE]:
            self.Exit()


    #
    def Render(self):
        #
        self.screen.fill((24, 24, 24))
        for c in self.world.constraints:
            pos1 = (int(c.node1.position.x), int(c.node1.position.y))
            pos2 = (int(c.node2.position.x), int(c.node2.position.y))
            game.draw.line(self.screen, (255, 255, 0), pos1, pos2, 4)
        game.draw.line(self.screen, (130, 130, 130), (self.world.hsize.x,20), (self.world.hsize.x,460), 3)
        game.draw.line(self.screen, (130, 130, 130), (20,self.world.hsize.y), (620,self.world.hsize.y), 3)
        y = []
        x = []
        for p in self.world.particles:
            pos = (int(p.position.x), int(p.position.y))
            x.append(p.position.x-self.world.hsize.x)
            y.append(p.position.y*-1+self.world.hsize.y)
            game.draw.circle(self.screen, (255, 255, 255), pos, 8, 0)
        #print("x="+str(x))
        #print("y="+str(y))
        tempfit = CurveFit(x,y,2)
        dists = []
        if self.grabbed != None:
            pos = (int(self.grabbed.position.x), int(self.grabbed.position.y))
            #game.draw.circle(self.screen, (255, 0, 255), pos, 8, 0)
            for c in self.world.constraints:
                pos1 = (int(c.node1.position.x), int(c.node1.position.y))
                pos2 = (int(c.node2.position.x), int(c.node2.position.y))
                dist = math.sqrt((pos[0] - pos1[0])**2 + (pos[1] - pos1[1])**2)
                if(dist<35):
                    c.stiff = 0.001
                #else:
                #    c.stiff = 0.5
                #c.stiff = 0.5 + (dist*0.5)/700
                #c.stiff = 0.1
                #dists.append(dist)
            #norm = [float(i)/max(dists) for i in dists]
            #print(norm)
            #iter = 0
            #for c in self.world.constraints:
                #c.stiff = norm[iter]+0.001
                #iter+=1
                #game.draw.line(self.screen, (int(dist)%255, 0, 0), pos1, pos2, 4)

                #game.draw.line(self.screen, (255, 255, 0), pos1, pos2, 4)

        # define the RGB value for white,
        #  green, blue colour .
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        # create a font object.
        # 1st parameter is the font file
        # which is present in pygame.
        # 2nd parameter is size of the font
        font = game.font.Font('freesansbold.ttf', 15)
        
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render(tempfit.function, True, green, blue)
        #game.draw.arc(self.screen, (255,0,0), tempfit.ellipserect,  tempfit.startangle, tempfit.endangle,3)
        
        for l in range(len(tempfit.x_parabolic)-1):
            pos1 = (int(tempfit.x_parabolic[l]), int(tempfit.y_parabolic[l]))
            pos2 = (int(tempfit.x_parabolic[l+1]), int(tempfit.y_parabolic[l+1]))
            game.draw.line(self.screen, (255, 0, 0), pos1, pos2, 3)
            #game.draw.circle(self.screen, (255, 0, 0), pos1, 1, 0)


        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()

        # set the center of the rectangular object.
        textRect.center = (500, 20)

        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        self.screen.blit(text, textRect)

        if self.hand1.numberofFingers == 3 and self.hand1.state=='Closed':
            game.draw.circle(self.screen, (0, 255, 0), self.hand1.centerTriangle, 8, 0)
        elif self.hand1.numberofFingers == 3 and self.hand1.state=='Open':
            game.draw.circle(self.screen, (255, 0, 0), self.hand1.centerTriangle, 8, 0)
        game.display.update()

    #
    def ClosestPoint(self):
        if game.mouse.get_pressed()[0]:
            mouse    = Vector(game.mouse.get_pos()[0], game.mouse.get_pos()[1])
        else:
            mouse    = Vector(self.hand1.centerTriangle[0],self.hand1.centerTriangle[1])
        closest  = None
        distance = float('inf')
        for particle in self.world.particles:
            d = mouse.distance(particle.position)
            if d < distance:
                closest  = particle
                distance = d
        
        return (closest, distance)

if __name__ == "__main__":
    print ("Starting...")
    app = DemoRope("Swinging Rope", 640, 480, 30)
    app.Run()

    #if bin & 0xFF == ord('q'):
    #    print('exit')
    #elif bin & 0xFF ==ord('s'):
    #    print('save')

    #self.cap.release()
    # loop over the boundaries
    print ("Ending...")