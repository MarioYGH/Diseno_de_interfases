import random
import numpy as np
import cv2 as cv

width = 900
height = 600
n_objects = 10
ground_level = height - 250

#colours
green, pink, brown, black, yellow = (40,185,40), (255,192,203),(30,65,155), (0,0,0), (0,215,215)

#blank image
bg = np.zeros((height,width,3), dtype=np.uint8)

#draw background
cv.rectangle(bg,(width,0),(0,ground_level),(255,225,95),-1)
cv.rectangle(bg,(width,ground_level),(0,height),green,-1)

class Cow:
    def __init__(self,image, location):
        self.img = image
        self.loc = location
        self.ht = np.random.randint(300,400)
        self.scale = np.random.choice(np.linspace(0.5,1.5,num=8),1)
        self.b_radius = 50
        self.s_radius = 25
        
    def draw(self, reverse=1):
        #body color
        body_color = [(30,65,155),(255,255,255),(60,95,185)]
        body_spots = [(255,192,203),(0,0,0),(60,95,185)]
        
        elector = np.random.random_integers(0,2)
        
        #feet
        cv.line(self.img, (int(self.loc-30*self.scale),int(self.ht+150*self.scale)), (int(self.loc-30*self.scale),int(self.ht+100*self.scale)),body_color[elector],int(10*self.scale))
        cv.line(self.img, (int(self.loc-30*self.scale),int(self.ht+150*self.scale)), (int(self.loc-30*self.scale),int(self.ht+150*self.scale)),black,int(10*self.scale))
        cv.line(self.img, (int(self.loc-15*self.scale),int(self.ht+150*self.scale)), (int(self.loc-15*self.scale),int(self.ht+100*self.scale)),body_color[elector],int(10*self.scale))
        cv.line(self.img, (int(self.loc-15*self.scale),int(self.ht+150*self.scale)), (int(self.loc-15*self.scale),int(self.ht+150*self.scale)),black,int(10*self.scale))
        cv.line(self.img, (int(self.loc+30*self.scale),int(self.ht+150*self.scale)), (int(self.loc+30*self.scale),int(self.ht+100*self.scale)),body_color[elector],int(10*self.scale))
        cv.line(self.img, (int(self.loc+30*self.scale),int(self.ht+150*self.scale)), (int(self.loc+30*self.scale),int(self.ht+150*self.scale)),black,int(10*self.scale))
        cv.line(self.img, (int(self.loc+15*self.scale),int(self.ht+150*self.scale)), (int(self.loc+15*self.scale),int(self.ht+100*self.scale)),body_color[elector],int(10*self.scale))
        cv.line(self.img, (int(self.loc+15*self.scale),int(self.ht+150*self.scale)), (int(self.loc+15*self.scale),int(self.ht+150*self.scale)),black,int(10*self.scale))
        
        #body
        cv.circle(self.img, (self.loc,int(self.ht+120*self.scale)) , int(self.s_radius/2*self.scale), pink, -1)
        cv.ellipse(self.img,(self.loc,int(self.ht+100*self.scale)),(int(self.b_radius*self.scale),int(self.s_radius*self.scale)),0,0,360,body_color[elector],-1)
        
        if reverse == 1:
            #spots
            cv.circle(self.img, (self.loc,int(self.ht+95*self.scale)) , int(self.s_radius/3*self.scale), body_spots[elector], -1)
            cv.circle(self.img, (int(self.loc+20*self.scale),int(self.ht+110*self.scale)) , int(self.s_radius/3*self.scale), body_spots[elector], -1)
            
            #head
                #collar
            cv.ellipse(self.img,(int(self.loc-35*self.scale),int(self.ht+95*self.scale)),(int(self.b_radius/2*self.scale),int(self.s_radius/1.5*self.scale)),0,0,360,black,-1)
            cv.line(self.img, (int(self.loc-40*self.scale),int(self.ht+90*self.scale)), (int(self.loc-40*self.scale),int(self.ht+110*self.scale)),yellow,5)
                #ears
            cv.ellipse(self.img,(int(self.loc-20*self.scale),int(self.ht+75*self.scale)),(int(self.b_radius/3*self.scale),int(self.s_radius/3*self.scale)),30,0,360,black,-1)
            cv.ellipse(self.img,(int(self.loc-20*self.scale),int(self.ht+75*self.scale)),(int(self.b_radius/4.5*self.scale),int(self.s_radius/4.5*self.scale)),30,0,360,pink,-1)
            cv.ellipse(self.img,(int(self.loc-60*self.scale),int(self.ht+75*self.scale)),(int(self.b_radius/3*self.scale),int(self.s_radius/3*self.scale)),150,0,360,black,-1)
            cv.ellipse(self.img,(int(self.loc-60*self.scale),int(self.ht+75*self.scale)),(int(self.b_radius/4.5*self.scale),int(self.s_radius/4.5*self.scale)),150,0,360,pink,-1)
                #head shape
            cv.ellipse(self.img,(int(self.loc-40*self.scale),int(self.ht+90*self.scale)),(int(self.b_radius/2*self.scale),int(self.s_radius/1.5*self.scale)),0,0,360,body_color[elector],-1)
            cv.ellipse(self.img,(int(self.loc-40*self.scale),int(self.ht+75*self.scale)),(int(self.b_radius/2.5*self.scale),int(self.s_radius/2*self.scale)),0,0,360,body_color[elector],-1)
                #eyes and nose
            cv.ellipse(self.img,(int(self.loc-40*self.scale),int(self.ht+90*self.scale)),(int(self.b_radius/3.5*self.scale),int(self.s_radius/3*self.scale)),0,0,360,pink,-1) 
            cv.circle(self.img, (int(self.loc-35*self.scale),int(self.ht+90*self.scale)) , int(self.s_radius/10*self.scale), black, -1)
            cv.circle(self.img, (int(self.loc-45*self.scale),int(self.ht+90*self.scale)) , int(self.s_radius/10*self.scale), black, -1)
            cv.circle(self.img, (int(self.loc-35*self.scale),int(self.ht+75*self.scale)) , int(self.s_radius/9*self.scale), black, -1)
            cv.circle(self.img, (int(self.loc-45*self.scale),int(self.ht+75*self.scale)) , int(self.s_radius/9*self.scale), black, -1)
            
            #tail
            cv.line(self.img, (int(self.loc+40*self.scale),int(self.ht+90*self.scale)), (int(self.loc+60*self.scale),int(self.ht+110*self.scale)),body_color[elector],5)
            cv.circle(self.img, (int(self.loc+60*self.scale),int(self.ht+110*self.scale)) , int(self.s_radius/5*self.scale), (0,0,0), -1)
            
        else:
            #spots
            cv.circle(self.img, (self.loc,int(self.ht+95*self.scale)) , int(self.s_radius/3*self.scale), body_spots[elector], -1)
            cv.circle(self.img, (int(self.loc-20*self.scale),int(self.ht+110*self.scale)) , int(self.s_radius/3*self.scale), body_spots[elector], -1)
            
            #head
                #collar
            cv.ellipse(self.img,(int(self.loc+35*self.scale),int(self.ht+95*self.scale)),(int(self.b_radius/2*self.scale),int(self.s_radius/1.5*self.scale)),0,0,360,black,-1)
            cv.line(self.img, (int(self.loc+40*self.scale),int(self.ht+90*self.scale)), (int(self.loc+40*self.scale),int(self.ht+110*self.scale)),yellow,5)
                #ears
            cv.ellipse(self.img,(int(self.loc+20*self.scale),int(self.ht+75*self.scale)),(int(self.b_radius/3*self.scale),int(self.s_radius/3*self.scale)),30,0,360,black,-1)
            cv.ellipse(self.img,(int(self.loc+20*self.scale),int(self.ht+75*self.scale)),(int(self.b_radius/4.5*self.scale),int(self.s_radius/4.5*self.scale)),30,0,360,pink,-1)
            cv.ellipse(self.img,(int(self.loc+60*self.scale),int(self.ht+75*self.scale)),(int(self.b_radius/3*self.scale),int(self.s_radius/3*self.scale)),150,0,360,black,-1)
            cv.ellipse(self.img,(int(self.loc+60*self.scale),int(self.ht+75*self.scale)),(int(self.b_radius/4.5*self.scale),int(self.s_radius/4.5*self.scale)),150,0,360,pink,-1)
                #head shape
            cv.ellipse(self.img,(int(self.loc+40*self.scale),int(self.ht+90*self.scale)),(int(self.b_radius/2*self.scale),int(self.s_radius/1.5*self.scale)),0,0,360,body_color[elector],-1)
            cv.ellipse(self.img,(int(self.loc+40*self.scale),int(self.ht+75*self.scale)),(int(self.b_radius/2.5*self.scale),int(self.s_radius/2*self.scale)),0,0,360,body_color[elector],-1)
                #eyes and nose
            cv.ellipse(self.img,(int(self.loc+40*self.scale),int(self.ht+90*self.scale)),(int(self.b_radius/3.5*self.scale),int(self.s_radius/3*self.scale)),0,0,360,pink,-1) 
            cv.circle(self.img, (int(self.loc+35*self.scale),int(self.ht+90*self.scale)) , int(self.s_radius/10*self.scale), black, -1)
            cv.circle(self.img, (int(self.loc+45*self.scale),int(self.ht+90*self.scale)) , int(self.s_radius/10*self.scale), black, -1)
            cv.circle(self.img, (int(self.loc+35*self.scale),int(self.ht+75*self.scale)) , int(self.s_radius/9*self.scale), black, -1)
            cv.circle(self.img, (int(self.loc+45*self.scale),int(self.ht+75*self.scale)) , int(self.s_radius/9*self.scale), black, -1)
            
            #tail
            cv.line(self.img, (int(self.loc-40*self.scale),int(self.ht+90*self.scale)), (int(self.loc-60*self.scale),int(self.ht+110*self.scale)),body_color[elector],5)
            cv.circle(self.img, (int(self.loc-60*self.scale),int(self.ht+110*self.scale)) , int(self.s_radius/5*self.scale), (0,0,0), -1)
            
        return self.img
    
class Chicken:
    def __init__(self,image, location):
        self.img = image
        self.loc = location
        self.ht = np.random.randint(300,400)
        self.scale = np.random.choice(np.linspace(0.5,1.5,num=8),1)
        self.b_radius = 50
        self.s_radius = 25
        
    def draw(self, reverse = 1):
        body_color = [(30,65,155),(255,255,255),(60,95,185)]
        elector = np.random.random_integers(0,2)
        
        #body and legs
        cv.circle(self.img, (self.loc,int(self.ht+120*self.scale)) , int(self.s_radius/2*self.scale), body_color[elector], -1)
        cv.line(self.img, (int(self.loc-5*self.scale),int(self.ht+140*self.scale)), (int(self.loc-5*self.scale),int(self.ht+120*self.scale)),body_color[elector],int(4*self.scale))
        cv.line(self.img, (int(self.loc-5*self.scale),int(self.ht+140*self.scale)), (int(self.loc-5*self.scale),int(self.ht+140*self.scale)),yellow,int(4*self.scale))
        cv.line(self.img, (int(self.loc+5*self.scale),int(self.ht+140*self.scale)), (int(self.loc+5*self.scale),int(self.ht+120*self.scale)),body_color[elector],int(4*self.scale))
        cv.line(self.img, (int(self.loc+5*self.scale),int(self.ht+140*self.scale)), (int(self.loc+5*self.scale),int(self.ht+140*self.scale)),yellow,int(4*self.scale))
        
        if reverse == 1:
            #tail
            cv.line(self.img, (int(self.loc-self.s_radius/2*self.scale),int(self.ht+130*self.scale)), (int(self.loc-5*self.scale),int(self.ht+120*self.scale)),body_color[elector],int(4*self.scale))
            cv.line(self.img, (int(self.loc-self.s_radius/2*self.scale),int(self.ht+130*self.scale)), (int(self.loc+5*self.scale),int(self.ht+120*self.scale)),body_color[elector],int(4*self.scale))
            
            #head
                #head shape
            cv.line(self.img, (int(self.loc+5*self.scale),int(self.ht+120*self.scale)), (int(self.loc+5*self.scale),int(self.ht+100*self.scale)),body_color[elector],int(7*self.scale))
            cv.circle(self.img, (int(self.loc+7*self.scale),int(self.ht+100*self.scale)) , int(self.s_radius/3*self.scale), body_color[elector], -1)
                #beak and eye
            cv.line(self.img, (int(self.loc+(7+self.s_radius/7)*self.scale),int(self.ht+100*self.scale)), (int(self.loc+(7+self.s_radius/3)*self.scale),int(self.ht+102*self.scale)),yellow,int(4*self.scale))
            cv.line(self.img, (int(self.loc+(7+self.s_radius/7)*self.scale),int(self.ht+104*self.scale)), (int(self.loc+(7+self.s_radius/3)*self.scale),int(self.ht+102*self.scale)),yellow,int(4*self.scale))
            cv.circle(self.img, (int(self.loc+5*self.scale),int(self.ht+100*self.scale)) , int(self.s_radius/20*self.scale), black, -1)
                #headress
            cv.line(self.img, (int(self.loc+7*self.scale),int(self.ht+(100-self.s_radius/4)*self.scale)), (int(self.loc+(7+self.s_radius/5)*self.scale),int(self.ht+(97-self.s_radius/4)*self.scale)),(0,0,255),int(4*self.scale))
            cv.line(self.img, (int(self.loc+7*self.scale),int(self.ht+(100-self.s_radius/4)*self.scale)), (int(self.loc+(7-self.s_radius/5)*self.scale),int(self.ht+(97-self.s_radius/4)*self.scale)),(0,0,255),int(4*self.scale))
            cv.line(self.img, (int(self.loc+7*self.scale),int(self.ht+(100-self.s_radius/4)*self.scale)), (int(self.loc+7*self.scale),int(self.ht+(97-self.s_radius/4)*self.scale)),(0,0,255),int(4*self.scale))
        else:
            #tail
            cv.line(self.img, (int(self.loc+self.s_radius/2*self.scale),int(self.ht+130*self.scale)), (int(self.loc-5*self.scale),int(self.ht+120*self.scale)),body_color[elector],int(4*self.scale))
            cv.line(self.img, (int(self.loc+self.s_radius/2*self.scale),int(self.ht+130*self.scale)), (int(self.loc+5*self.scale),int(self.ht+120*self.scale)),body_color[elector],int(4*self.scale))
            
            #head
                #head shape
            cv.line(self.img, (int(self.loc-5*self.scale),int(self.ht+120*self.scale)), (int(self.loc-5*self.scale),int(self.ht+100*self.scale)),body_color[elector],int(7*self.scale))
            cv.circle(self.img, (int(self.loc-7*self.scale),int(self.ht+100*self.scale)) , int(self.s_radius/3*self.scale), body_color[elector], -1)
                #beak and eye
            cv.line(self.img, (int(self.loc-(7+self.s_radius/7)*self.scale),int(self.ht+100*self.scale)), (int(self.loc-(7+self.s_radius/3)*self.scale),int(self.ht+102*self.scale)),yellow,int(4*self.scale))
            cv.line(self.img, (int(self.loc-(7+self.s_radius/7)*self.scale),int(self.ht+104*self.scale)), (int(self.loc-(7+self.s_radius/3)*self.scale),int(self.ht+102*self.scale)),yellow,int(4*self.scale))
            cv.circle(self.img, (int(self.loc-5*self.scale),int(self.ht+100*self.scale)) , int(self.s_radius/20*self.scale), black, -1)
                #headress
            cv.line(self.img, (int(self.loc-7*self.scale),int(self.ht+(100-self.s_radius/4)*self.scale)), (int(self.loc-(7+self.s_radius/5)*self.scale),int(self.ht+(97-self.s_radius/4)*self.scale)),(0,0,255),int(4*self.scale))
            cv.line(self.img, (int(self.loc-7*self.scale),int(self.ht+(100-self.s_radius/4)*self.scale)), (int(self.loc-(7-self.s_radius/5)*self.scale),int(self.ht+(97-self.s_radius/4)*self.scale)),(0,0,255),int(4*self.scale))
            cv.line(self.img, (int(self.loc-7*self.scale),int(self.ht+(100-self.s_radius/4)*self.scale)), (int(self.loc-7*self.scale),int(self.ht+(97-self.s_radius/4)*self.scale)),(0,0,255),int(4*self.scale))

        return self.img
    
for i in range(0,30):
    electors = np.random.random_integers(0,1)
    if electors == 1:       
        img = Cow(bg,np.random.randint(40,840)).draw(reverse=np.random.randint(0,2))
    else:
        img = Chicken(bg,np.random.randint(40,840)).draw(reverse=np.random.randint(0,2))

img = Chicken(bg,60).draw(reverse=np.random.randint(0,2))
cv.imshow('granja', img)

#display image
cv.waitKey(0)
cv.destroyAllWindows()