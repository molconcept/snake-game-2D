import math
import random
import time
import winsound
import turtle

#Creating delay variable
delay=0.1

#Creating variable for score,reached score and scoresum 
score=0
reached_score=0
score_sum=0

#Creating life variable
life=5

#Creating level variable
level=1

#Creating game state variable
game_state='start'

#Creating variable diff
diff='easy'

#Creating variabl to control life spawn
hl='not_taken'

#setup screen
wn=turtle.Screen()
wn.title('Snake & The Apple by ASR')
wn.setup(600,600)
wn.tracer(0)

# TURTLES BLOCK

#Creating snake head
head=turtle.Turtle()
head.speed(0)
head.penup()
head.color('black')
head.shape('square')
head.goto(0,0)
head.direction='stop'

segments=[]              #Taking list to add segments to form snake body 

#Creating food of snake
food=turtle.Turtle()
food.speed(0)
food.penup()
turtle.register_shape('Apple.gif')
food.shape('Apple.gif')
food.goto(0,180)

#Creating obstacles for snake
ob=turtle.Turtle()
ob.speed(0)
turtle.register_shape('Stone.gif')
ob.shape('Stone.gif')
ob.penup()
ob.goto(-1000,1000)

ob1=turtle.Turtle()
ob1.speed(0)
turtle.register_shape('Stone.gif')
ob1.shape('Stone.gif')
ob1.penup()
ob1.goto(-1000,1000)

ob2=turtle.Turtle()
ob2.speed(0)
turtle.register_shape('Stone.gif')
ob2.shape('Stone.gif')
ob2.penup()
ob2.goto(-1000,1000)

ob3=turtle.Turtle()
ob3.speed(0)
turtle.register_shape('Stone.gif')
ob3.shape('Stone.gif')
ob3.penup()
ob3.goto(-1000,1000)

ob4=turtle.Turtle()
ob4.speed(0)
turtle.register_shape('Stone.gif')
ob4.shape('Stone.gif')
ob4.penup()
ob4.goto(-1000,1000)

ob5=turtle.Turtle()
ob5.speed(0)
turtle.register_shape('Stone.gif')
ob5.shape('Stone.gif')
ob5.penup()
ob5.goto(-1000,1000)

#Creating turtle to display score & life
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)

#Creating turtle to display level
lev=turtle.Turtle()
lev.speed(0)
lev.color('white')
lev.penup()
lev.goto(0,-290)
lev.hideturtle()

#Creating turtle to display score at the end
lend=turtle.Turtle()
lend.speed(0)
lend.color('black')
lend.penup()
lend.goto(0,-1)
lend.hideturtle()

#Creating turtle to display quit message
qut=turtle.Turtle()
qut.penup()
wn.addshape('Pause_pop.gif')
qut.shape('Pause_pop.gif')
qut.hideturtle()

#Creating turtle to display current mode
cm=turtle.Turtle()
cm.penup()
cm.hideturtle()

#Creating life turtle
hrt=turtle.Turtle()
hrt.speed(0)
hrt.penup()
hrt.goto(-4000,6000)
turtle.register_shape('Heart.gif')
hrt.shape('Heart.gif')
hrt.hideturtle()
    
# FUNCTIONS BLOCK

#Creating function to change any turtle shape then display and hide it in required time
def simg(x,tim,cui):
    tur=x
    wn.addshape(cui)
    tur.shape(cui)
    tur.showturtle()
    wn.update()
    time.sleep(tim)
    tur.hideturtle()

# Creating function to display game screen
def start_game():
    global game_state
    if game_state=='start' or game_state=='back':
        play_sfx('startbg1.wav')
        game_state = "rungame"

#Creating function to display control , rules & difficulty of game on screen
def con_screen():
    global game_state
    if game_state=='start' or game_state=='back':
        play_sfx('onbuttonselect.wav')
        game_state='aboutcon'

def rule_screen():
    global game_state
    if game_state=='start' or game_state=='back':
        play_sfx('onbuttonselect.wav')
        game_state='aboutrule'                       

def diff_screen():
    global game_state
    if game_state=='start' or game_state=='back':
        play_sfx('onbuttonselect.wav')
        game_state='selectdiff'                  

#Creating function to select difficulty mode of the game
def choose_easy():
    global diff
    if game_state=='selectdiff':
        play_sfx('onmodeselect.wav')
        simg(cm,0.7,'e_con.gif')
        diff='easy'

def choose_medium():
    global diff
    if game_state=='selectdiff':
        play_sfx('onmodeselect.wav')
        simg(cm,0.7,'m_con.gif')
        diff='medium'

def choose_hard():
    global diff
    if game_state=='selectdiff':
        play_sfx('onmodeselect.wav')
        simg(cm,0.7,'h_con.gif')
        diff='hard'    

def mode_info() :
    global game_state
    if game_state=='selectdiff' :
        play_sfx('onbuttonselect_v2.wav')
        game_state='modeinfo'
        
#Function for playing sound
def play_sfx(x):
    winsound.PlaySound(x,winsound.SND_ASYNC)

#Moving snake
def go_up():
    if head.direction!='down':
        head.direction='up'

def go_down():
    if head.direction!='up':
        head.direction='down'

def go_left():
    if head.direction!='right':
        head.direction='left'    

def go_right():
    if head.direction!='left':
        head.direction='right'

def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)

    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)

    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)

    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)

#Making function to bring snake at x=0,y=0(origin)
def reset_snake():
    time.sleep(1)
    head.goto(0,0)
    head.direction='stop'

    #Reset score
    global score
    score=0
    pen.clear()
    pen.write('Score : {}    Reachedscore : {}    Life : {} '.format(score,reached_score,life),False,align='center',font=('Arial',20,'bold'))

    #Reset delay
    global delay
    delay=0.1

    #Hiding the segments at collision
    for i in segments:
        i.goto(1000,1000)
        i.hideturtle()

    #Removing the segments from the list
    segments.clear()

#Creating function to add bonus score after completing the level
def bonus_score():
    global reached_score
    reached_score+=5
    pen.clear()
    pen.write('Score : {}    Reachedscore : {}    Life : {} '.format(score,reached_score,life),False,align='center',font=('Arial',20,'bold'))

#Creating function to return back to start screen
rb=''    
def return_b():
    global game_state
    if game_state=='aboutcon' or game_state=='aboutrule' or game_state=='selectdiff' or game_state=='modeinfo':
        play_sfx('onreturn.wav')
        game_state='back'

#Creating function to restart the game
def reset_game():
    global reached_score
    global score_sum
    global life
    global level
    global game_state
    if game_state=='loser' or game_state=='winner':
        play_sfx('restartgamebg.wav')
        reset_snake()
        reached_score=0
        score_sum=0
        level=1
        life=5
        hl='not_taken'
        game_state='rungame'
        pen.clear()
        lev.clear()
        lend.clear()

#Creating function to hide or show on screen turtles
def grup(ue):
    if ue=='hide':
        head.hideturtle()
        food.hideturtle()
        hrt.hideturtle()
        if len(segments)!=0:
            for pi in segments:
                pi.hideturtle()
        ob.hideturtle()
        ob1.hideturtle()
        ob2.hideturtle()
        ob3.hideturtle()
        ob4.hideturtle()
        ob5.hideturtle()

    elif ue=='show':
        head.showturtle()
        food.showturtle()
        hrt.showturtle()
        if len(segments)!=0:
            for pi in segments:
                pi.showturtle()
        ob.showturtle()
        ob1.showturtle()
        ob2.showturtle()
        ob3.showturtle()
        ob4.showturtle()
        ob5.showturtle()        
        
#Creating function to pause the game
pause=False
def controlpause():
    global pause
    if game_state == "rungame":
        if pause==False:
            play_sfx('pause.wav')
            pause=True
            qut.showturtle()
            grup('hide')
            
#Playing music on end        
def lose_play():
    global life
    global game_state
    if game_state=='lose':
        play_sfx('gameexitbg.wav')
        wn.bgpic('loseend.gif')
        life=-1
        game_state='loser'
        

def win_play():
    global game_state
    global reached_score
    if game_state=='win':
        reached_score=-10
        play_sfx('gameclearbg.wav')
        game_state='winner'

#Creating function to exit game
key=''
def exit_game():
    global key
    if game_state=='loser' or game_state=='winner':
        key='quit'

#To quit while the game is on run or continue it
def y_press():
    if game_state=='rungame' and pause==True:
        global key
        qut.hideturtle()
        grup('show')
        key='quit'

def n_press():
    global pause
    if game_state=='rungame' and pause==True:
        play_sfx(f'{apd}/onbuttonselect_v2.wav')
        qut.hideturtle()
        grup('show')
        pause=False

#Creating function to speed up the snake
def velocity():
    global delay
    if game_state=='rungame' and delay>0.05:
        play_sfx('onboost.wav')
        delay-=0.03

#Cheat_Test
'''def cheat():
    ink=int(input('Enter No : '))
    global reached_score
    reached_score=ink

def cheat_2():
    ink2=int(input('Enter No : '))
    global score
    score=ink2'''

#Creating keyboard bindings    
turtle.listen()
turtle.onkeypress(go_up,'Up')       #Movement controls map
turtle.onkeypress(go_down,'Down')
turtle.onkeypress(go_left,'Left')
turtle.onkeypress(go_right,'Right')

turtle.onkeypress(start_game,'s')   #Start screen controls map
turtle.onkeypress(rule_screen,'x')
turtle.onkeypress(con_screen,'c')
turtle.onkeypress(diff_screen,'m')
turtle.onkeypress(mode_info,'i')
turtle.onkeypress(choose_easy,'j')
turtle.onkeypress(choose_medium,'k')
turtle.onkeypress(choose_hard,'l')
turtle.onkeypress(return_b,'r')

turtle.onkeypress(lose_play,'q')    #End game controls map
turtle.onkeypress(win_play,'z')
turtle.onkeypress(reset_game,'p')

turtle.onkeypress(controlpause,'Escape') #Pause game control map
turtle.onkeypress(y_press,'y')
turtle.onkeypress(n_press,'n')

turtle.onkeypress(exit_game,'F1')  #Quit game control map

turtle.onkeypress(velocity,'a') #Speed control map

'''turtle.onkeypress(cheat,',')
turtle.onkeypress(cheat_2,'.')'''

# Main Game Loop
while True:
    #To pause the screen
    if not pause:
        # Update the screen
        wn.update()

        #Controlling speed of screen
        time.sleep(delay)

        #Display rule ,control screen and difficulty mode screen
        if game_state=='aboutrule':
            wn.bgpic("ruleshow.gif")
            head.hideturtle()
            food.hideturtle()
            pen.clear()
            lev.clear()

        if game_state=='aboutcon':
            wn.bgpic("controlshow.gif")
            head.hideturtle()
            food.hideturtle()
            pen.clear()
            lev.clear()

        if game_state=='selectdiff':
            wn.bgpic("modeshow.gif")
            head.hideturtle()
            food.hideturtle()
            pen.clear()
            lev.clear()

        if game_state=='modeinfo':
            wn.bgpic("modeinfobg.gif")
            head.hideturtle()
            food.hideturtle()
            pen.clear()
            lev.clear()

        #Displaying gameover screen when life becomes zero
        if life == 0:
            wn.bgpic("losepop.gif")
            game_state='lose'
            head.hideturtle()
            food.hideturtle()
            pen.clear()
            lev.clear()
            #Clearing obstacles from screen
            ob.goto(-1000,1000)
            ob1.goto(-1000,1000)
            ob2.goto(-1000,1000)
            ob3.goto(-1000,1000)
            ob4.goto(-1000,1000)
            ob5.goto(-1000,1000)

        #Displaying result when lost
        if game_state=='loser':
           wn.bgpic('loseend.gif')
           lend.clear()
           lend.write('Total score : {}'.format(score_sum),False,align='center',font=('Arial',25,'bold'))
            
        #Displaying game end screen when score becomes 300 
        if reached_score == 300:
            #To display right screen on clearing the game
            life=1
            wn.bgpic("winpop.gif")
            game_state='win'
            head.hideturtle()
            food.hideturtle()
            pen.clear()
            lev.clear()
            #Clearing obstacles from screen
            ob.goto(-1000,1000)
            ob1.goto(-1000,1000)
            ob2.goto(-1000,1000)
            ob3.goto(-1000,1000)
            ob4.goto(-1000,1000)
            ob5.goto(-1000,1000)

        #Displaying result when win
        if game_state=='winner':
            wn.bgpic('winend.gif')
            lend.clear()
            lend.write('Total score : {}'.format(score_sum),False,align='center',font=('Arial',25,'bold'))

        #Display start screen 
        if game_state == "start" or game_state=='back':
            wn.bgpic("Startback.gif")
            head.hideturtle()
            food.hideturtle()
            pen.clear()
            lev.clear()

        #Run the main game code    
        if game_state == "rungame" and reached_score<30:
            wn.bgpic('Bg1x.gif')
            head.showturtle()
            food.showturtle()
            lend.clear()
            pen.write('Score : {}    Reachedscore : {}    Life : {} '.format(score,reached_score,life),False,align='center',font=('Arial',20,'bold'))
            lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))

        #Creating & Running levels for game
        if reached_score==30:
            level=2
            lev.clear()
            lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
            wn.bgpic('Bg2x.gif')
            if diff=='hard':
                ob.goto(0,180)
                ob1.goto(0,-180)
            reset_snake()
            
            #Adding bonus for completing the level in reached_score
            bonus_score()

        if reached_score==60:
            level=3
            lev.clear()
            lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
            wn.bgpic('Bg3x.gif')
            if diff=='hard':
                ob.goto(-180,0)
                ob1.goto(180,0)
            reset_snake()

            #Adding bonus for completing the level in reached_score
            bonus_score()

        if reached_score==90:
            level=4
            lev.clear()
            lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
            wn.bgpic('Bg4x.gif')
            if diff=='hard':
                ob.goto(180,180)
                ob1.goto(-180,-180)
            reset_snake()

            #Adding bonus for completing the level in reached_score
            bonus_score()

        if reached_score==120:
            level=5
            lev.clear()
            lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
            wn.bgpic('Bg5x.gif')
            if diff=='hard':
                ob.goto(-180,180)
                ob1.goto(180,-180)
            reset_snake()

            #Adding bonus for completing the level in reached_score
            bonus_score()

        if reached_score==150:
            level=6
            lev.clear()
            lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
            wn.bgpic('Bg6x.gif')
            if diff=='medium':
                ob.goto(0,180)
                ob1.goto(0,-180)
            if diff=='hard':
                ob.goto(-180,-180)
                ob1.goto(180,-180)
                ob2.goto(0,180)
            reset_snake()

            #Adding bonus for completing the level in reached_score
            bonus_score()

            #Adding bonus life for completing 5 levels for easy mode
            if diff=='easy':
                life+=2
                pen.clear()
                pen.write('Score : {}    Reachedscore : {}    Life : {} '.format(score,reached_score,life),False,align='center',font=('Arial',20,'bold'))

        if reached_score==180:
            level=7
            lev.clear()
            lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
            wn.bgpic('Bg7x.gif')
            if diff=='medium':
                ob.goto(-180,0)
                ob1.goto(180,0)
            if diff=='hard':
                ob.goto(0,180)
                ob1.goto(0,-180)
                ob2.goto(-180,0)
                ob3.goto(180,0)
            reset_snake()

            #Adding bonus for completing the level in reached_score
            bonus_score()

            #Spawning life for medium mode
            if diff=='medium':
                hrt.goto(210,0)
                hrt.showturtle()
            
        if reached_score==210:
            level=8
            lev.clear()
            lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
            wn.bgpic('Bg8x.gif')
            if diff=='medium':
                ob.goto(-180,-180)
                ob1.goto(180,-180)
                ob2.goto(0,180)
            if diff=='hard':
                ob.goto(180,180)
                ob1.goto(-180,-180)
                ob2.goto(-180,180)
                ob3.goto(180,-180)
            reset_snake()

            #Adding bonus for completing the level in reached_score
            bonus_score()

            #Spawning life for medium mode
            if diff=='medium':
                hrt.goto(0,210)
                hrt.showturtle()

            #If player doesn't takes the life
            if diff=='hard':    
                hrt.hideturtle()
                hrt.goto(-4000,6000)    
                
        if reached_score==240:
            level=9
            lev.clear()
            lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
            wn.bgpic('Bg9x.gif')
            if diff=='medium':
                ob.goto(0,180)
                ob1.goto(0,-180)
                ob2.goto(-180,0)
                ob3.goto(180,0)
            if diff=='hard':
                ob.goto(180,180)
                ob1.goto(-180,-180)
                ob2.goto(-180,180)
                ob3.goto(180,-180)
                ob4.goto(180,0)
                ob5.goto(-180,0)
            reset_snake()

            #Adding bonus for completing the level in reached_score
            bonus_score()

            #If player doesn't takes the life
            hrt.hideturtle()
            hrt.goto(-4000,6000)
                    
        if reached_score==270:
            level=10
            lev.clear()
            lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
            wn.bgpic('Bg10x.gif')
            if diff=='medium':
                ob.goto(180,180)
                ob1.goto(-180,-180)
                ob2.goto(-180,180)
                ob3.goto(180,-180)
            if diff=='hard':
                ob.goto(180,180)
                ob1.goto(-180,-180)
                ob2.goto(-180,180)
                ob3.goto(180,-180)
                ob4.goto(0,180)
                ob5.goto(0,-180)
            reset_snake()

            #Adding bonus for completing the level in reached_score
            bonus_score()

            #If player doesn't takes the life
            hrt.hideturtle()
            hrt.goto(-4000,6000)

        #Spawning life for hard mode
        if diff=='hard' and level==7 and hl=='not_taken':
            if score==160:
                hrt.goto(0,210)
                hrt.showturtle()
                hl='1_taken'

        elif diff=='hard' and level==9 and hl=='1_taken':
            if score==220:
                hrt.goto(210,0)
                hrt.showturtle()
                hl='all_taken'

        #Checking for collision between boundary and snake
        if head.xcor()>240 or head.xcor()<-240 or head.ycor()>240 or head.ycor()<-240:
            play_sfx('borderhit.wav')
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'

            #Hiding the segments at collision
            for i in segments:
                i.goto(1000,1000)
                i.hideturtle()

            #Removing the segments from the list
            segments.clear()

            #Reset score at collision
            score=0

            #Reset life
            life-=1

            pen.clear()
            pen.write('Score : {}    Reachedscore : {}    Life : {} '.format(score,reached_score,life),False,align='center',font=('Arial',20,'bold'))


            #Reset delay
            delay=0.1

        #Checking for collision between snake head and it's segments
        for i in segments:
            if head.distance(i)<20:
                if reached_score!=300:
                    play_sfx('bodyhit.wav')
                time.sleep(1)
                head.goto(0,0)
                head.direction='stop'

                #Hiding the segments at collision
                for i in segments:
                    i.goto(1000,1000)
                    i.hideturtle()

                #Removing the segments from the list
                segments.clear()

                #Reset score at collision
                score=0

                #Reset life
                life-=1

                pen.clear()
                pen.write('Score : {}    Reachedscore : {}    Life : {} '.format(score,reached_score,life),False,align='center',font=('Arial',20,'bold'))

                #Reset delay
                delay=0.1

        #Check for collision between snake and heart
        if head.distance(hrt)<30:
            play_sfx('lifebg.wav')
            life+=1
            pen.clear()
            pen.write('Score : {}    Reachedscore : {}    Life : {} '.format(score,reached_score,life),False,align='center',font=('Arial',20,'bold'))
            hrt.goto(-4000,6000)
            hrt.hideturtle()
            
        #Check for collision between snake and obstacle
        if head.distance(ob)<40 or head.distance(ob1)<40 or head.distance(ob2)<40 or head.distance(ob3)<40 or head.distance(ob4)<40 or head.distance(ob5)<40:
            play_sfx('obhit.wav')
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'

            #Hiding the segments at collision
            for i in segments:
                i.goto(1000,1000)
                i.hideturtle()

            #Removing the segments from the list
            segments.clear()

            #Reset life
            life-=1

            #Reset score at collision
            score=0

            pen.clear()
            pen.write('Score : {}    Reachedscore : {}    Life : {} '.format(score,reached_score,life),False,align='center',font=('Arial',20,'bold'))

            #Reset delay
            delay=0.1

        #Check for spawning of food above the obstacle
        if ob.distance(food)<20 or ob1.distance(food)<20 or ob2.distance(food)<20 or ob3.distance(food)<20 or ob4.distance(food)<20 or ob5.distance(food)<20:
            p=random.choice([-160,-200,0,160,200])
            q=random.choice([-160,-200,0,160,200])
            food.hideturtle()
            food.goto(p,q)
            food.showturtle()

        #Check for spawning of Heart above the obstacle
        if hrt.distance(food)<20 :
            p=random.choice([-160,-200,0,160,200])
            q=random.choice([-160,-200,0,160,200])
            food.hideturtle()
            food.goto(p,q)
            food.showturtle()  
            
         
        #Check for collision of snake and food
        if head.distance(food)<28:
            x=random.randint(-240,240)
            y=random.randint(-240,240)
            food.goto(x,y)

            play_sfx('appleeat.wav')

            #Appending new segment in the list at collision with food
            new_segment=turtle.Turtle()
            new_segment.speed(0)
            new_segment.color('grey')
            new_segment.shape('square')
            new_segment.penup()
            segments.append(new_segment)

            #Increasing score on collision
            if diff=='easy':
                score+=30

            if diff=='medium':
                score+=15

            if diff=='hard':
                score+=10
            score_sum+=score

            if score>reached_score:
                reached_score=score
            pen.clear()
            pen.write('Score : {}    Reachedscore : {}    Life : {} '.format(score,reached_score,life),False,align='center',font=('Arial',20,'bold'))

            #Reducing delay to increase speed                                                               # To make the game more challenging we are increasing
                                                                                                                                  # the speed when the snake's head collides with the 
                                                                                                                                  # food by reducing the delay(variable)
            if diff=='easy':
                delay-=0.001

            if diff=='medium':
                delay-=0.002

            if diff=='hard':
                delay-=0.003
            

        #Moving segments in reverse order
        for index in range(len(segments) -1,0,-1):
            x=segments[index-1].xcor()
            y=segments[index-1].ycor()
            segments[index].goto(x,y)

        #Adding first segment of the list to snake head
        if len(segments)>0:
            x=head.xcor()
            y=head.ycor()
            segments[0].goto(x,y)

        #Moving snake only when game starts
        if game_state=='rungame':
            move()

        #Breaking loop on key press to quit game
        if key=='quit':
            play_sfx('quitbg.wav')
            time.sleep(1)
            break
    else:
        wn.update()
        #When screen is paused
        if key=='quit':
            play_sfx('quitbg.wav')
            time.sleep(1)
            break
    
turtle.bye()
