import pgzrun
from random import randint

HEIGHT = 500
WIDTH = 1200
w,h =WIDTH,HEIGHT

music.play('remix')
p = Actor('ironman',(w//2,h//2))
e = Actor ('alien',(w//2,h//200))
c = Actor ('coin',(w//2,h-100))
score = 0
game_state = 0

def draw():
    if game_state == 0:

      screen.fill('black')
      p.draw()
      e.draw()
      c.draw()
      screen.draw.text(f'Score: {score}',(10,10),color ='white')

    elif game_state == 1:
        screen.draw.text(f'game over',(w//2, h//2),color = 'white')
    
    elif game_state == 2 :
        screen.draw.text(f'you win',(w//2, h//2),color = 'green')

def player_update():
    if p.x > w :
        p.x = 0
    elif p.y > h:
        p.y = 0 
    if keyboard.left:
        p.x -= 5
    elif keyboard.right:
        p.x += 5
    elif keyboard.up:
        p.y -= 5
    elif keyboard.down:
        p.y += 5
    

def enemy_update():
    if c.x > e.x:
        e.x += 1
    if c.x < e.x:
        e.x -= 1
    if c.y > e.y:
        e.y += 1
    if c.y < e.y:
        e.y -= 1
    if e.colliderect (p):
        
        p.x = w//2
        p.y = h//2

def score_update():
    global score
    if p.colliderect (c):
        score += 10
        c.x = randint(0,w)
        c.y = randint(0,h)
        
    if e.colliderect (c):
        score -= 10
        c.x = randint(0,w)
        c.y = randint(0,h)
    if score < -50:
        game_state = 1 # game over
    if score >= 50:
        game_state = 2 # game win
    
def update():
    enemy_update()
    player_update()
    score_update()
 
pgzrun.go()