import pgzrun

WIDTH = 700
HEIGHT = 700
TITLE = "car game"

bake = Actor("bake" , (350 , 350))
start = Actor("start" , (350 , 350))

rood = Actor("rood" , (350 , 350))
tank = Actor("tank" , (-50 , 430))
car = Actor("car" , (750 , 150))
motor = Actor("motor" , (350 , 600))
game_over = Actor("game_over" , (100 , 100))
agin = Actor("agin" , (400 , 400))

speed_motor = 0
score = 0
gameOver = False
gameStart = True


def update():
    global gameOver , score , speed_motor , gameStart
    if gameStart:        
        if gameOver == False:
                tank.x += 4
                car.x -= 4
        if tank.x >= 750 and car.x >=-750:
                tank.x = -50
                car.x = 750

        motor.y -= speed_motor
        if motor.y <= -50:
            motor.y = 750
            score += 1

        if motor.colliderect(tank):
            speed_motor = 0
            gameOver = True

        elif motor.colliderect(car):
            speed_motor = 0
            gameOver = True



    if keyboard.w:
        motor.y -= 7.5
    elif keyboard.s:
        motor.y += 3
    elif keyboard.d:
        motor.x += 3
    elif keyboard.a:
        motor.x -= 3

def draw():
    
    if not gameStart:
        print("game start",gameStart,"gameOver",gameOver) 
        start.pos = -100,-200
        bake.pos = -500,-700 

    if gameStart:
        print("game start",gameStart,"gameOver",gameOver) 
        
        rood.draw() 
        tank.draw()
        car.draw()
        motor.draw()
        bake.draw()
        start.draw() 
        screen.draw.text(f"score : {score}" , color = "black" , topleft = (50 , 50) , fontsize = 50)    
    if not gameStart:
        print("game start",gameStart,"gameOver",gameOver)
        gameOver == True
        screen.fill("red")
        game_over.draw()
        agin.draw()
        screen.draw.text(f"{score}" , color = "black" , topleft = (85 , 210) , fontsize =100)
        
def on_mouse_down(pos,button):
    global gameStart,gameOver
    if start.collidepoint(pos) and button == mouse.LEFT:
        print("yes")
        gameStart = False

    if agin.collidepoint(pos) and button == mouse.LEFT:
        print("no")
        gameStart = False

 

pgzrun.go()