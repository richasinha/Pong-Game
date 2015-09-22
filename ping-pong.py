from visual import *

class HitCounter():
    def __init__(self,position=(0,0), score=0):
        self.counter = label(pos=position, color=color.red, text=str(score))
        self.score = score
    def scoring(self):
        self.score=self.score+1
        self.counter.text = str(self.score)
        print (self.score)

scene.range = 20
scene.width = 600
scene.height = 600

ceiling = box(pos=vector(0,19,0),width = 0.1,height=1, length =39, color=color.white)
leftbox = box(pos=vector(-19,0,0),width = 0.1,height=39, length = 1, color=color.white)
right = box(pos=vector(19,0,0),width = 0.1,height=5, length=1, color=color.red)
floor = box(pos=vector(0,-19,0),width = 0.1,height=1, length=39, color=color.white)

ball = sphere(pos=(0,0,0), radius=1, color=color.blue)
ball.velocity = 20*vector(5,8,0)
COR = 1
end = 0
points = 0
score = HitCounter()

dt = 0.001

while 1:
    rate(60)
    ball.pos += ball.velocity*dt
    mouse = scene.mouse.pos

    if(mouse.y-right.height/2 > floor.y + floor.height/2 and mouse.y + right.height/2 < ceiling.pos.y-ceiling.height/2) :
        right.y = mouse.y
    else:
        #place right at centre of mouse is outside the walls
        if(mouse.y-right.height/2 <floor.y + floor.height/2):
            right.pos = (18,0,0)
        elif(mouse.y + right.height/2 > ceiling.y - floor.height/2):
            right.pos =(18 ,0 ,0)

    if ball.pos.x > 17.5:
        if(right.pos.y - 1) < ball.pos.y < (right.pos.y + 1):
            score.scoring()
            ball.velocity.x = (-1)*ball.velocity.x
            rate(1)
        else:
            print ball.pos
            print right.pos
            points = score.score
            end = 1
    elif ball.pos.x < -17.5:
        ball.velocity.x = -1*ball.velocity.x
    elif  ball.pos.y > 17.5:
        ball.velocity.y = (-1)*ball.velocity.y
    elif ball.pos.y < -17.5:
        ball.velocity.y = (-1)*ball.velocity.y

    if end == 1:
        ball.pos += ball.velocity*dt
        ball.visible = False
        del ball
        del score
        endGame = label(pos=vector(0,0,0),text='Game Over', height=30, border=6, font = 'sans' )
        sleep(3)
        exit()    
        
