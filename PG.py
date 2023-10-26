#Practical-1 Write a python program to perform translation operation on rectangle by taking initial coordinates from user.
from tkinter import *
root=Tk()
C=Canvas(root,bg="black",height=700,width=700)
tx=int(input("Enter the translate value:"))
x0=int(input("Enter the coordinate x0:"))
y0=int(input("Enter the coordinate y0:"))
x1=int(input("Enter the coordinate x1:"))
y1=int(input("Enter the coordinate y1:"))
x2=int(input("Enter the coordinate x2:"))
y2=int(input("Enter the coordinate y2:"))
x3=int(input("Enter the coordinate x3:"))
y3=int(input("Enter the coordinate y3:"))
rectangle=C.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3,x0,y0,fill="white")
rectangle1=C.create_polygon(x0+tx,y0+tx,x1+tx,y1+tx,x2+tx,y2+tx,x3+tx,y3+tx,x0+tx,y0+tx,fill="white")
C.create_text(300, 50, text="Vinay Srinivas Eligeti/TCS2324012", fill="white", font=('Helvetica 18 bold'))
C.pack()
mainloop() 

#Practical-2 Write a python program to perform scaling operation on triangle by taking initial coordinates from user.
from tkinter import *
root=Tk()
C=Canvas(root,bg="black",height=700,width=700)
sx=int(input("Enter the scale value:"))
x0=int(input("Enter the coordinate x0:"))
y0=int(input("Enter the coordinate y0:"))
x1=int(input("Enter the coordinate x1:"))
y1=int(input("Enter the coordinate y1:"))
x2=int(input("Enter the coordinate x2:"))
y2=int(input("Enter the coordinate y2:"))
rectangle=C.create_polygon(x0,y0,x1,y1,x2,y2,x0,y0,fill="white")
rectangle1=C.create_polygon(x0*sx,y0*sx,x1*sx,y1*sx,x2*sx,y2*sx,x0*sx,y0*sx,fill="white")
C.create_text(300, 50, text="Vinay Srinivas Eligeti/TCS2324012", fill="white", font=('Helvetica 18 bold'))
C.pack()
mainloop()

#Practical-3 Write a python program to perform reflection operation on polygon by taking initial coordinates from user.
from tkinter import *
root=Tk()
C=Canvas(root,bg="black",height=700,width=700)
tx=int(input("Enter the translate value:"))
x0=int(input("Enter the coordinate x0:"))
y0=int(input("Enter the coordinate y0:"))
x1=int(input("Enter the coordinate x1:"))
y1=int(input("Enter the coordinate y1:"))
x2=int(input("Enter the coordinate x2:"))
y2=int(input("Enter the coordinate y2:"))
rectangle=C.create_polygon(x0,y0,x1,y1,x2,y2,x0,y0,fill="white")
rectangle1=C.create_polygon(x0*2,y0+y0+tx*2,x1+tx,y1+tx,x2+tx,y2+tx,x0*2,y0+y0+tx*2,fill="white")
C.create_text(300, 50, text="Vinay Srinivas Eligeti/TCS2324012", fill="white", font=('Helvetica 18 bold'))
C.pack()
mainloop()

#Practical-4 Write a python program to rotate right angle triangle by 45 degree by taking initial coordinates from user.
import math
from tkinter import *
root=Tk()
C=Canvas(root,bg="black",height=700,width=700)
angle=int(input("Enter the angle value:"))
angle_rad=math.radians(angle)
x0=int(input("Enter the coordinate x0:"))
y0=int(input("Enter the coordinate y0:"))
x1=int(input("Enter the coordinate x1:"))
y1=int(input("Enter the coordinate y1:"))
x2=int(input("Enter the coordinate x2:"))
y2=int(input("Enter the coordinate y2:"))
rectangle=C.create_polygon(x0,y0,x1,y1,x2,y2,x0,y0,fill="white")
x00=(x0*math.cos(angle_rad)-y0*math.sin(angle_rad))*-1
y00=x0*math.sin(angle_rad)+y0*math.cos(angle_rad)
x01=(x1*math.cos(angle_rad)-y1*math.sin(angle_rad))*-1
y01=x1*math.sin(angle_rad)+y1*math.cos(angle_rad)
x02=(x2*math.cos(angle_rad)-y2*math.sin(angle_rad))*-1
y02=x2*math.sin(angle_rad)+y2*math.cos(angle_rad)
rectangle1=C.create_polygon(x00,y00,x01,y01,x02,y02,x00,y00,fill="white")
C.create_text(300, 50, text="Vinay Srinivas Eligeti/TCS2324012", fill="white", font=('Helvetica 18 bold'))
C.pack()
mainloop()

#Practical-5 Write a python program to perform shearing on rectangle in positive direction of x-axis by taking initial coordinates from user.
from tkinter import *
root=Tk()
C=Canvas(root,bg="black",height=700,width=700)
shx=int(input("Enter the translate value:"))
x0=int(input("Enter the coordinate x0:"))
y0=int(input("Enter the coordinate y0:"))
x1=int(input("Enter the coordinate x1:"))
y1=int(input("Enter the coordinate y1:"))
x2=int(input("Enter the coordinate x2:"))
y2=int(input("Enter the coordinate y2:"))
x3=int(input("Enter the coordinate x3:"))
y3=int(input("Enter the coordinate y3:"))
rectangle=C.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3,x0,y0,fill="white")
rectangle1=C.create_polygon(x0+shx,y0,x1,y1,x2,y2,x3+shx,y3,x0+shx,y0,fill="blue")
C.create_text(300, 50, text="Vinay Srinivas Eligeti/TCS2324012", fill="white", font=('Helvetica 18 bold'))
C.pack()
mainloop()

#Practical-6 Write a python program to create below shape and perform reflection about parallel to y-axis, followed by translation and scaling operation on it.
from tkinter import *
root=Tk()
C=Canvas(root,bg="black",height=700,width=700)
x0,y0,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6=150,120,65,200,150,280,150,245,250,245,250,155,150,155
arrow=C.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x0,y0,fill="white")
reflection=C.create_polygon(x0,y0+200,x1,y1+200,x2,y2+200,x3,y3+200,x4,y4+200,x5,y5+200,x6,y6+200,x0,y0+200,fill="green")
tx=200
translate=C.create_polygon(x0+tx,y0,x1+tx,y1,x2+tx,y2,x3+tx,y3,x4+tx,y4,x5+tx,y5,x6+tx,y6,x0+tx,y0,fill="white")
s=2
t=160
scale=C.create_polygon(x0*s+t,y0*s,x1*s+t,y1*s,x2*s+t,y2*s,x3*s+t,y3*s,x4*s+t,y4*s,x5*s+t,y5*s,x6*s+t,y6*s,x0*s+t,y0*s,fill="red")
C.create_text(300, 50, text="Vinay Srinivas Eligeti/TCS2324012", fill="white", font=('Helvetica 18 bold'))
C.pack()
mainloop()

#Practical-7 Aim: Implement space invader game in python using pygame module.
import pygame
import random
import math
from pygame import mixer
# initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
# caption
pygame.display.set_caption("pyplay")
# toseticon
icon1 = pygame.image.load("ufo.png")
pygame.display.set_icon(icon1)
# drawplayer
playerimg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

#bullet
bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"
score_value=0

#adding font for displaying score
font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10
#adding font for displaying game over
over_font=pygame.font.Font("freesansbold.ttf",70)

def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
# enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_Change=[]
enemyY_Change=[]
no_of_enemies=6

for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 800-64))
    enemyY.append(random.randint(50, 150))
    enemyX_Change.append(3)
    enemyY_Change.append(40)
    
# background image
Background_img=pygame.image.load('background.png')
 
mixer.music.load("background.wav")
mixer.music.play(-1)

#collision function
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False
    
#bullet function
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
    
# player function
def player (x, y):
    screen.blit(playerimg, (x, y))

# enemy function
def enemy (x, y, i):
    screen.blit(enemyImg[i], (x, y))

# gamewindow
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(Background_img,(0,0))
    #   playerX -= 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=800-64:
        playerX=800-64
    
    # bullet movement
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
    bulletX+=playerX_change
        
    # enemy movement
    for i in range(no_of_enemies):
        #Game Over
        if enemyY[i]>400:
            for j in range(no_of_enemies):
                enemyY[i]=2000
            game_over_text()
            break
            
        enemyX[i] += enemyX_Change[i]
        if enemyX[i]<=0:
            enemyX_Change[i]=3
            enemyY[i] += enemyY_Change[i]
        elif enemyX[i] >= 800-64:
            enemyX_Change[i] = -3
            enemyY[i] += enemyY_Change[i]
#         elif enemyY[i]<=0:
#             enemyY[i] += enemyY_Change[i]
#         elif enemyY[i]>=200:
#             enemyY[i] = 0

        # check collision 
        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound=mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY=480
            bullet_state="ready"
            score_value+=1
            
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i], enemyY[i], i)
    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()

#Practical-8 Aim: Implement Snake game in python using pygame module.
import pygame
import time
import random
 
snake_speed = 15
 
# Window size
window_x = 1020
window_y = 600
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption("Vinay Srinivas Eligeti TCS2324012")
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
 
# initial score
score = 0
 
# displaying Score function
def show_score(choice, color, font, size):
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)
 
# game over function
def game_over():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
 
 
# Main Function
while True:
     
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    # displaying score continuously
    show_score(1, white, 'times new roman', 20)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)

#Practical-9 Aim: Implement 2D UFO game using unity.

CameraController.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    public GameObject player;
    private Vector3 offset;
    // Start is called before the first frame update
    void Start()
    {
        offset = transform.position - player.transform.position;
    }

    // Update is called once per frame
    void LateUpdate()
    {
        transform.position = player.transform.position + offset;
    }
}


PlayerController.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class PlayerController : MonoBehaviour
{
    public Text winText;
    public Text countText;
    public int count = 0;
    private Rigidbody2D rbd; 
    public float speed;
    void Start()
    {
        rbd = GetComponent<Rigidbody2D>();
    }
    
    void FixedUpdate()
    {
        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");
        Vector2 movement = new Vector2(moveHorizontal, moveVertical);
        rbd.AddForce(movement*speed);
    }
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.tag == "PickUp")
        {
            other.gameObject.SetActive(false);
            count++;
            SetCountText();
        }
    }
    void SetCountText()
    {
        countText.text = "Score: "+count.ToString();
        if (count == 8)
        {
            winText.text = "You Win!!";
        }
    }
}

Rotator.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotator : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.Rotate(new Vector3(0, 0, 45) * Time.deltaTime);
    }
}

#Practical-10 Aim: Implement 3D roll ball game using unity.

CameraController.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    private Vector3 offset;
    public GameObject player;
    // Start is called before the first frame update
    void Start()
    {
        offset = transform.position - player.transform.position;
    }

    // Update is called once per frame
    void LateUpdate()
    {
        transform.position = player.transform.position + offset;
    }
}


PlayerController.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour
{
    public Text winText;
    public Text countText;
    public int count = 0;
    private Rigidbody rb;
    public float speed;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        count = 0;
        winText.text = " ";
        SetCountText();
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");
        Vector3 movement = new Vector3(moveHorizontal, 0.0f, moveVertical);
        rb.AddForce(movement * speed);
    }
    void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("PickUp"))
        {
            other.gameObject.SetActive(false);
            count = count + 1;
            SetCountText();
        }
    }
    void SetCountText()
    {
        countText.text = "Score " + count.ToString();
        if (count == 8)
        {
            winText.text = "You Win!!";
        }
    }
}


Rotator.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotator : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.Rotate(new Vector3(15, 30, 45) * Time.deltaTime);
    }
}