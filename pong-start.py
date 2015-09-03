from visual import *

def collisionBalls(sphere1, sphere2):
    dist = mag(sphere1.pos - sphere2.pos)
    if(dist < (sphere1.radius + sphere2.radius)):
        return True
    else:
        return False


scene.range=5
scene.autoscale = False

ball1 = sphere(pos = (-5,3,0), radius = 0.2, color = color.magenta)
ball2 = sphere(pos = (-5,1,0), radius = 0.2, color = color.cyan)
ball3 = sphere(pos = (-5,-1,0), radius = 0.2, color = color.yellow)
ball4 = sphere(pos = (-5,-3,0), radius = 0.2, color = color.orange)

shooter = box(pos = (-4.5,-4.5,0), height = 0.1, width = 0.3, length= 0.5)

ball1.v = 0.5*vector(1,0,0)
ball2.v = 1*vector(1,0,0)
ball3.v = 1.5*vector(1,0,0)
ball4.v = 2*vector(1,0,0)

ballList = [ball1, ball2, ball3, ball4]
bulletList = []

shots = 0
t=0
dt = 0.01
while 1 :
    shooter.v = vector(0,0,0)
    rate(500)
    for thisball in ballList:
        thisball.pos += thisball.v*dt

        if thisball.pos.x > 5:
            thisball.v = -1*thisball.v
        elif thisball.pos.x < -5:
            thisball.v = -1*thisball.v
            
    if scene.kb.keys:
        k = scene.kb.getkey()
        if k == "right":
            shooter.v = 20*vector(1,0,0)
        elif k == "left":
            shooter.v = 20*vector(-1,0,0)
        elif ((k == "up") and (shooter.pos.y < 5)):
            shooter.v = 20*vector(0,1,0)
        elif ((k == "down") and (shooter.pos.y > -5)):
            shooter.v = 20*vector(0,-1,0)
        elif k == " ":
            if shots < 11:
                bullet = sphere(pos = shooter.pos, radius = 0.1, color=color.white) #Make a bullet to shoot the balls
                bullet.v = 3*vector(0,1,0)
                bulletList.append(bullet)
                shots += 1
            else:
                print 'Press R' #Replenish the shots
        elif k == "r":
            print 'Replenish the balls'
            shots = 0
        else:
            shooter.v = vector(0,0,0)
            
        shooter.pos += shooter.v*dt

    for indx,thisbullet in enumerate(bulletList):
        thisbullet.pos += thisbullet.v*dt

        for thisball in ballList:
            if collisionBalls(thisball, thisbullet):
                thisball.visible = False
                ballList.remove(thisball)
                print 'deleted ball'
                
        
        if(thisbullet.pos.y > 10):
            thisbullet.visible = False
            bulletList.remove(thisbullet)
            print 'deleted bullet '+ str(indx)

    if not ballList:
        exit()
    t = t +dt
