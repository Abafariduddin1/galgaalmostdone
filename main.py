import pgzrun

WIDTH=700
HEIGHT=700

bees = []
bulle = []

ship=Actor("plane.png")
ship.pos=350,600



point=75
ypoint=10
for o in range(8):
    for i in range(4):
        bee = Actor("bee.png")
        bees.append(bee)
        bees[-1].x=100+50*o
        bees[-1].y=80+50*i

    


def draw():
    screen.clear()
    screen.fill("blue")
    ship.draw()
    for i in bees:
        i.draw()
    for i in bulle:
        i.draw()    
    screen.draw.text(str(score),(20,20),color="black", scolor="grey" )    
    
def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor("idk.png")
        bullet.x=ship.x
        bullet.y=ship.y-50
        bulle.append(bullet)
        sounds.eep.play()
score = 0          
numb=3
def update():
     global numb
     global score
     global bees 
     if keyboard.a:
        ship.x -= 5 
     if keyboard.d:
        ship.x += 5 
     if bees[-1].x>700:
         numb=-3
     if bees[0].x<0:
         numb=3           
     for i in bees:
         i.y=i.y+1
         i.x=i.x+numb
         if i.colliderect(ship):
             sounds.game.play()
     if ship.x<=-40:
         ship.x=730
     if ship.x>=740:
         ship.x=-30    
     for i in bulle:
         i.y=i.y-10
     for bee in bees:
         for bullet in bulle:
             if bee.colliderect(bullet):
                 bees.remove(bee)
                 bulle.remove(bullet)
                 score=score+1
                     
        
               

    







pgzrun.go()