from visual import *       

scene.range = 20
scene.width = 600
scene.height = 600

ceiling = box(pos=vector(0,19,0),width = 0.1,height=1, length =39, color=color.red)
leftbox1 = box(pos=vector(-19,-10,0),width = 0.1,height=17, length = 1, color=color.red)
leftbox2 = box(pos=vector(-19,10,0),width = 0.1,height=17, length = 1, color=color.red)
right = box(pos=vector(19,0,0),width = 0.1,height=5, length=1, color=color.red)
floor = box(pos=vector(0,-19,0),width = 0.1,height=1, length=39, color=color.red)

ball = sphere(pos=(0,0,0), radius=1, color=color.blue)
ball.velocity = 1*vector(5,8,0)
COR = 1

dt = 0.01

while 1:
    rate(100)
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

    if ball.pos.x > 17.5 and (right.pos.y-0.5) < ball.pos.y < (right.pos.y + 0.5):
        ball.velocity.x = (-1)*ball.velocity.x
    elif ball.pos.x < -17.5:
        ball.velocity.x = -1*ball.velocity.x
    elif  ball.pos.y > 17.5:
        ball.velocity.y = (-1)*ball.velocity.y
    elif ball.pos.y < -17.5:
        ball.velocity.y = (-1)*ball.velocity.y

    print ball.velocity
        
        
