import random
import pygame
import math
pygame.init()
size = (1000,600)
screen = pygame.display.set_mode(size)
fps = 35
clock = pygame.time.Clock()
color = pygame.color.THECOLORS
pygame.display.set_caption("Naruto's Adventure")
icon = pygame.image.load('naruto_icon.png')
pygame.display.set_icon(icon)
#phases
phase = preview = 'preview'
phase_menu ="menu"
phase_game ='game'
phase_options ='options'
phase_help ='help'
phase_quit ='quit'
phase_skin = 'skin choose'
phase = preview

#menu variables
str1=pygame.font.SysFont ('Monotype Corsiva', 70,True) 
menu_bckgr = pygame.image.load('menu/Menu.jpg')
click_sound = pygame.mixer.Sound('sound/selected.mp3')
helpach = open('menu/helpach.txt', 'r')
hshrift = pygame.font.SysFont('Comic Sans', 50)
text_help= helpach.read()
option_str = pygame.font.SysFont ('ALGERIAN', 60)
option_str1 = pygame.font.SysFont ('ALGERIAN', 45)
zagolovok = pygame.font.SysFont ('ALGERIAN', 80)
plus =pygame.image.load('menu/plus.png')
minus = pygame.image.load('menu/minus.png')
plus = pygame.transform.scale(plus,(119,100))
minus = pygame.transform.scale(minus,(100,105))
sound_off = pygame.image.load('menu/off.png')
sound_on = pygame.image.load('menu/on.png')
sound_off = pygame.transform.scale(sound_off,(180,120))
sound_on = pygame.transform.scale(sound_on,(180,120))
volume = 0.4
pause_button = pygame.image.load('menu/pause_button.png')
pause_button = pygame.transform.scale(pause_button,(70,70))
class Stars:
    def __init__(self):
        self.x= random.randint(0, 1000) 
        self.y= 0
    def move(self):
        pygame.draw.circle(screen, color['orangered4'], (self.x, self.y), 3)
        self.y+=3

list_of_stars=[]
list_of_items=[
    [100,100,'Play',color["orange2"],1],
    [100,200,'Options',color['orange2'],2],
    [100,300,'Help',color['orange2'],3],
    [100,400,'Quit',color['orange2'],4]
]
numb_item = 0

def Sure():
    global done
    sure = False
    subscreen = pygame.Surface((500,300))
    ans = pygame.font.SysFont('Segoe Script',50,True)
    quest = pygame.font.SysFont('Segoe Script',30,True,True)
    answers=[
        [100,180,'YES',color['black'],1],
        [300,180,'NO',color['black'],2]
    ]
    answer = 0
    question = quest.render('Are you sure to quit?',True,color['darkgreen'],color['palegreen4'])
    while not sure:
        screen.blit(subscreen,(250,150))
        subscreen.blit(pygame.transform.scale(pygame.image.load('menu/subscreen.jpeg'),(500,300)),(0,0))
        subscreen.blit(question,(50,120))
        mouse = pygame.mouse.get_pos()
        for i in answers:
            if i[0]<=mouse[0]-250<=i[0]+80 and i[1]<=mouse[1]-150<=i[1]+60:
                answer = i[4]
            if answer == i[4]:
                subscreen.blit(ans.render(i[2],True,i[3],color['blueviolet']),(i[0],i[1]))
            else:
                subscreen.blit(ans.render(i[2],True,i[3]),(i[0],i[1]))
                answer = 0
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN and i.button == pygame.BUTTON_LEFT:
                if 100<=i.pos[0]-250<=180 and 180<=i.pos[1]-150<=240:
                    click_sound.play()
                    done = True
                    sure = True
                if 300<=i.pos[0]-250<=380 and 180<=i.pos[1]-150<=240:
                    click_sound.play()
                    sure = True    
        pygame.display.flip()
        clock.tick(35)

def Pause():
    global phase, phase_menu, phase_game,click_sound
    pause = False
    pause_screen = pygame.Surface((800,500))
    pause_bg = pygame.image.load('menu/pause.jpg')
    pause_bg = pygame.transform.scale(pause_bg,(800,500))
    choices = [
        [200,150,'Continue',color['black'],1],
        [200,200,'Main Menu',color['black'],2],
        [200,250,'Quit',color['black'],3]
    ]
    choice_str = pygame.font.SysFont('Arial',40,True)
    choice = 0
    while not pause:
        screen.blit(pause_screen,(100,50))
        pause_screen.blit(pause_bg,(0,0))
        mouse = pygame.mouse.get_pos()
        for i in choices:
            if i[0]<=mouse[0]-100<=i[0]+200 and i[1]<=mouse[1]-50<=i[1]+30:
                choice = i[-1]
            if choice == i[-1]:
                pause_screen.blit(choice_str.render(i[2],True,i[3],color['darkgoldenrod4']),(i[0],i[1]))
            else:
                pause_screen.blit(choice_str.render(i[2],True,i[3]),(i[0],i[1]))
                choice = 0
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
                click_sound.play()
                pause = True
            if i.type == pygame.MOUSEBUTTONDOWN and i.button == pygame.BUTTON_LEFT:
                if 250<=i.pos[0]<=250+200 and 200<=i.pos[1]<=200+70:
                    click_sound.play()
                    pause= True
                if 250<=i.pos[0]<=250+200 and 250<=i.pos[1]<=250+70:
                    click_sound.play()
                    pause= True
                    phase= phase_menu
                if choice == 3:
                    click_sound.play()
                    pause = True
                    Sure()
        pygame.display.flip()
        clock.tick(35)
def Loading(the_phase):
    global phase
    left_eye_y, right_eye_y= -140,600
    eye_velocity = 5
    right_eye = pygame.transform.scale(pygame.image.load('right_eye.png'),(250,140))
    left_eye = pygame.transform.scale(pygame.image.load('left_eye.png'),(250,140))
    load = False
    load_count = 0
    load_screen = pygame.Surface(size)
    while not load:
        screen.blit(load_screen,(0,0))
        load_screen.fill(color['black'])
        load_screen.blit(right_eye,(600, right_eye_y))
        load_screen.blit(left_eye,(150, left_eye_y))
        if left_eye_y==right_eye_y:
            eye_velocity=0
            load_count+=1
            if load_count==50:
                phase = the_phase
                load = True
        else:
            right_eye_y -= eye_velocity
            left_eye_y += eye_velocity
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                load = True
                done = True
        pygame.display.flip()
        clock.tick(35)

#for elite action
E_move = 0
elite_count = 0
def Preview():
    global E_move,elite_count
    shrift = pygame.font.SysFont('Times New Roman',100,True)
    E = shrift.render('E',True,color['red3'])
    Ǝ = shrift.render('Ǝ',True,color['red3'])
    sego = pygame.font.SysFont('Segoe UI Black',40,True,True)
    bracket = pygame.font.SysFont('Calibri',80,True)
    screen.fill(color['black'])
    if 30<elite_count:
        screen.blit(shrift.render('    I     ',True,color['red3']),(380,250))
    if 10+30<elite_count<30+30:
        screen.blit(bracket.render('][',True,color['red3']),(475,268))
    if 30+30<elite_count<70+30:
        screen.blit(shrift.render('    Ξ    ',True,color['red3']),(365,250))
    if 70+30<elite_count<=110+30:
        screen.blit(E,(460+E_move,250))
        screen.blit(Ǝ,(460-E_move,250))
        E_move+=3
        if elite_count==110+30:
            E_move=0
    if 100+30<elite_count<130+30:
        screen.blit(shrift.render(' L I T  ',True,color['red3']),(365,250))
    if 120+30<elite_count:
        screen.blit(shrift.render('Ξ L I T Ξ ',True,color['red3']),(300,250))
        screen.blit(shrift.render('I',True,color['red3']),(310-E_move,250))
        screen.blit(shrift.render('I',True,color['red3']),(650+E_move,250))
        if 140+30>=elite_count:
            E_move+=1
    if 180+30<elite_count:
        screen.blit(sego.render('PRODUCTION',True,color['red3']),(340,370))
    elite_count+=1

# Music and sounds
pygame.mixer.music.load('musics/preview.mpeg')
music_up = False
def music(a):
    global music_up,phase_menu,level1,skin_life,boss_life
    music_dict = {
        phase_menu : 'musics/menusong.mpeg',
        phase_game : 'musics/level.mpeg',
        skin_life : 'musics/game_over.mpeg',
        boss_life : 'musics/win.mpeg'
    }
    pygame.mixer.music.load(music_dict[a])
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

bonus_sound = pygame.mixer.Sound('sound/bonus.mpeg')
jump_sound = pygame.mixer.Sound('sound/jumping.mpeg')
shoot_sound = pygame.mixer.Sound('sound/shoot.mpeg')
shoot_collide = pygame.mixer.Sound('sound/shot_collide.mpeg')


def Titles():
    global phase,phase_menu
    logo_y=620
    logo_velocity=2
    end = open('end.txt', 'r')
    endshrift = pygame.font.SysFont('Broadway', 40)
    text_end = end.read() 
    logo_ph = pygame.image.load('logo.png')
    logo_ph = pygame.transform.scale(logo_ph,(400,200))
    end_y = 800
    title_screen = pygame.Surface(size)
    pygame.mixer.music.load('musics/aura1.mp3')
    pygame.mixer.music.play()
    while phase!=phase_menu:
        screen.blit(title_screen,(0,0))
        title_screen.fill(color['black'])
        title_screen.blit(logo_ph, (300,logo_y))
        logo_y-=logo_velocity
        if logo_y==-600:
            logo_velocity=0
            music(phase_menu)
            phase = phase_menu
        a=0
        for i in text_end.split('\n'):  
            title_screen.blit(endshrift.render(i, True, color['red4']), (300,end_y+a))
            a+=50
        end_y-=logo_velocity
        pygame.display.flip()
        clock.tick(20)
# Skin variables

x=240
y=0
dy = -5
dx = 0
x_speed = 10
y_speed = -28
gravity = 2.5
jump_is_allowed = False
camera_x = 0
camera_y = 0
life_count = 3
skin_life = 3
chosen = 'sasuke'
left = False
right = False
count_anim = 0
 #attacking
right_attack = False
left_attack = False
attack_anim = 0
 #skin get hurt
damage_anim = 0
damage = False

# life hearts photo's
full_heart = pygame.image.load('full heart.png')

# maps variables
block_size = 35
bg = pygame.image.load("fons/foon2.png")
bg1 = pygame.image.load("fons/foon.png")
bg2 = pygame.image.load("fons/fon.jpg")
fon = pygame.image.load("fon4.png")
bg = pygame.transform.scale(bg, size)
bg1 = pygame.transform.scale(bg1, size)
bg2 = pygame.transform.scale(bg2, size)
cloud = pygame.image.load("level1/c.png")
block1 = pygame.image.load("level1/b.png")
block2 = pygame.image.load("level2/2.png")
block3 = pygame.image.load("level2/3.png")
block = pygame.image.load("level2/6.png")
block5 = pygame.image.load("level2/13.png")
block6 = pygame.image.load("level2/14.png")
block8 = pygame.image.load("level2/5.png")
block7 = pygame.image.load("level2/7.png")
block7c = pygame.image.load("level2/7c.png")
block9 = pygame.image.load("level2/8.png")
block10 = pygame.image.load("level2/10.png")
block11 = pygame.image.load("level2/e.png")
block12 = pygame.image.load("level2/q.png")
block13 = pygame.image.load("level2/r.png")
block14 = pygame.image.load("level2/t.png")
block15 = pygame.image.load("level2/y.png")
block16 = pygame.image.load("level1/g.png")
block17 = pygame.image.load("level1/h.png")
block18 = pygame.image.load("level1/m.png")
block19 = pygame.image.load("level1/d.png")
block20 = pygame.image.load("level1/i.png")
block21 = pygame.image.load("level1/j.png")
block22 = pygame.image.load("level1/f.png")
block23 = pygame.image.load("level3/1.jpg")
block24 = pygame.image.load("level3/2.jpg")
block25 = pygame.image.load("level3/3.jpg")
block26 = pygame.image.load("level3/4.png")
block27 = pygame.image.load("level3/5.png")
block28 = pygame.image.load("level3/6.png")
block29 = pygame.image.load("level3/7.jpg")
block30 = pygame.image.load("level3/8.jpg")
block31 = pygame.image.load("level3/9.jpg")
block32 = pygame.image.load("level3/10.jpg")
block33 = pygame.image.load("level3/11.jpg")
fon = pygame.transform.scale(fon, (1000,300))
level = pygame.transform.scale(pygame.image.load("level.png"),(block_size+20,block_size+20))
cloud = pygame.transform.scale(cloud, (block_size+40,block_size+50))
block1 = pygame.transform.scale(block1, (block_size,block_size))
block2 = pygame.transform.scale(block2, (block_size,block_size))
block3 = pygame.transform.scale(block3, (block_size,block_size))
block = pygame.transform.scale(block, (block_size,block_size))
block5 = pygame.transform.scale(block5, (block_size,block_size))
block6 = pygame.transform.scale(block6, (block_size,block_size))
block7 = pygame.transform.scale(block7, (block_size,block_size))
block7c = pygame.transform.scale(block7c, (block_size,block_size))
block8 = pygame.transform.scale(block8, (block_size,block_size))
block9 = pygame.transform.scale(block9, (block_size,block_size))
block10 = pygame.transform.scale(block10, (block_size,block_size))
block11 = pygame.transform.scale(block11, (block_size,block_size))
block12 = pygame.transform.scale(block12, (block_size,block_size))
block13 = pygame.transform.scale(block13, (block_size,block_size))
block14 = pygame.transform.scale(block14, (block_size,block_size))
block15 = pygame.transform.scale(block15, (block_size,block_size))
block16 = pygame.transform.scale(block16, (block_size,block_size))
block17 = pygame.transform.scale(block17, (block_size,block_size))
block18 = pygame.transform.scale(block18, (block_size,block_size))
block19 = pygame.transform.scale(block19, (block_size,block_size))
block20 = pygame.transform.scale(block20, (block_size,block_size))
block21 = pygame.transform.scale(block21, (block_size,block_size))
block22 = pygame.transform.scale(block22, (block_size,block_size))
block23 = pygame.transform.scale(block23, (block_size,block_size))
block24 = pygame.transform.scale(block24, (block_size,block_size))
block25 = pygame.transform.scale(block25, (block_size,block_size))
block26 = pygame.transform.scale(block26, (block_size,block_size))
block27 = pygame.transform.scale(block27, (block_size,block_size))
block28 = pygame.transform.scale(block28, (block_size,block_size))
block29 = pygame.transform.scale(block29, (block_size,block_size))
block30 = pygame.transform.scale(block30, (block_size,block_size))
block31 = pygame.transform.scale(block31, (block_size,block_size))
block32 = pygame.transform.scale(block32, (block_size,block_size))
block33 = pygame.transform.scale(block33, (block_size,block_size))
level1=[
    "           c                 c        c             c               c                     c                          c       c           c                         ", 
    "                                                                c         c                                                        ",
    "     c                 c                  c        c        c         c                     c        c      c            c                   " ,
    "                 c              c                                         c        c    c                         c                    c                         " ,
    "           c                                                                                          c    c                    c c c                     c                 " ,
    "                                                                                                                                                                         " ,
    "                                                   P                                                        P                                                    " ,
    "                                                  ghh                                                      ghh                                                               GPPP " ,
    "                                                              HPP                  ghhh                                                                    P               bbbbbbb" ,
    "            HP                        HP                   ghhhhhhhh                          HP                              ghhhhh                      ghh              mmmmmmm",
    "          ghhhhhhh                  ghhhhhhh              gm          gh     HP             ghhhhhhh                                                                       mmmmmmm    ",
    "                                              gh      gh                   ghhhhhhhh                                                            ghh                        mmmmmmm        ",
    "                    gh                                                                                                                                                     mmmmmmm          ",
    "                         dbbi               H                   P      H               H  P                  L                     HP                   P       H         Pmmmmmmm       ",
    "                        dfmmji           dbbbbbbbbi     dbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbi       dbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbmmmmmmmm",
    "bbbbbbbbbbbbbbbbbbbbbbbbfmmmmjbbbbbbbbbbbfmmmmmmmmjbbbbbfmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmj       fmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",
    "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm       mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",
    "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm       mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",
    "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm       mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",
    "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm       mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",
    "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm       mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",
    ]
level2=[
    "66666666666666666666q       t66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666",
    "66666666666666666666q       t66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666",
    "66666666666666666666q       neeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeey66666666666",
    "66666666666666666666q                                                                                                                                           t66666666666",
    "66666666666666666666q                                                                                                                                           t66666666666",
    "66666666666666666666q                                                                                                                                           t66666666666",
    "66666666666666666666q                                                                                             kP                                            t66666666666",
    "66666666666666666666q                                                                                      s2222222222222223                                    t66666666666",
    "66666666666666666666q                                                      GP                                                       k P                         t66666666666",
    "66666666666666666666q                                                 s222222222223             GPP                             s2222222223                     t66666666666",
    "66666666666666666666q                                                                        s222222223                                                         t66666666666",
    "66666666666666666666q                          G          s223                                                                                     s23          t66666666666",
    "66666666666666666666q                       s222222223           k             s222222223                              82222227                                 t66666666666",
    "66666666666666666666q                                                                                                  t666666q                                 t66666666666",
    "66666666666666666666q                   k                            G                      GP                         t66666697              l                Pt66666666666",
    "66666666666666666666q       k        82222227           8222222222222222222222222222222222222222222222227  k P    82222w666666692222222222222227        82222222w66666666666",
    "6666666666666666666692222222222222222w666666922222222222w666666666666666666666666666666666666666666666669222222222w6666666666666666666666666666q        t6666666666666666666",
    "66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666q        t6666666666666666666",
    "66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666q        t6666666666666666666",
    "66aaaaa6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666q        t6666666666666666666",
    "66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666q        t6666666666666666666",
    ]

level3=[
    "zzzD       EEEEEEEEEEEEEEEEEEEzzzzzz",
    "zzzD                          Fzzzzz",
    "zzzD                          Fzzzzz",
    "zzzD                          Fzzzzz",
    "zzzD                          Fzzzzz",
    "zzzD                          Fzzzzz",
    "zzzD                k         Fzzzzz",
    "zzzD                          Fzzzzz",
    "zzzD        k                 Fzzzzz",
    "zzzD         ou               Fzzzzz",
    "zzzD                         xzzzzzz",
    "zzzD    ouu           xuuuuuuzzzzzzz",
    "zzzD             ou   Fzzzzzzzzzzzzz",
    "zzzD                  Fzzzzzzzzzzzzz",
    "zzzzA  P     P     P xzzzzzzzzzzzzzz",
    "zzzzzuuuuuuuuuuuuuuuuzzzzzzzzzzzzzzz",
    "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
    "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
    "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
    ]
# bots
#BATS
class AirBots:
    def __init__(self,x,y):
        self.y = y-25
        self.x = x
        self.list = [i for i in range(self.x,self.x+152)] #координаты х по которым оно будет двигаться вперед
        self.reverse = self.list[::-1] # и обратно
        self.left = random.choice([True,False])
        self.c = 0
        self.count = random.randint(0,fps)
        self.rights = [pygame.transform.scale(pygame.image.load('bots img/bat_right_3.png'),(50,50)),
                       pygame.transform.scale(pygame.image.load('bots img/bat_right_2.png'),(50,50)),
                       pygame.transform.scale(pygame.image.load('bots img/bat_right_1.png'),(50,50))
                      ]
        self.lefts = [pygame.transform.scale(pygame.image.load('bots img/bat_left_3.png'),(50,50)),
                      pygame.transform.scale(pygame.image.load('bots img/bat_left_2.png'),(50,50)),
                      pygame.transform.scale(pygame.image.load('bots img/bat_left_1.png'),(50,50))
                      ]
        self.life = 1
        self.turn = []
        self.turns = []
        self.width = 50
        self.height = 50
    def move(self):
        if self.c>=150:
            self.left = not self.left
            self.c = 0
        self.count %=12
        if self.left:
            self.turn = self.list
            self.turns = self.rights
        else:
            self.turn = self.reverse
            self.turns = self.lefts
        screen.blit(self.turns[self.count//4],(self.turn[self.c]+camera_x,self.y+camera_y))
        pygame.draw.line(screen,color['red'],(self.turn[self.c] + camera_x,self.y),(self.turn[self.c] + 50 + camera_x,self.y),5)
        pygame.draw.line(screen,color['lightgreen'],(self.turn[self.c] + camera_x,self.y),(self.turn[self.c] + 50*self.life + camera_x,self.y),5)
        pygame.draw.rect(screen,color['white'],(self.turn[self.c] + camera_x,self.y-3,50,6),1)
        self.count+=1
        self.c += 3

#BEARS AND BOARS
class EarthBots:
    def __init__(self,x,y,animal):
        self.y = y
        self.list = [i for i in range(x,x+181)]
        self.reverse = self.list[::-1]
        self.c = 0
        self.animal = animal
        self.count = random.randint(0,fps)
        self.left = random.choice([True,False])
        self.life = 2
        self.turn = []
        self.turns = [] 
    def move(self):
        if self.animal == 'bear':
            self.width,self.height = 93,75
        else:
            self.width,self.height = 58,35
        self.rights = [
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_left_1.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_left_2.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_left_3.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_left_1.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_left_2.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_left_3.png'),(self.width,self.height))
        ]
        self.lefts = [
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_right_1.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_right_2.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_right_3.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_right_1.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_right_2.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_right_3.png'),(self.width,self.height))
        ]
        self.count%=24
        if self.c>=180:
            self.left = not self.left
            self.c = 0
        if self.left:
            self.turn = self.list
            self.turns = self.rights
        else:
            self.turn = self.reverse
            self.turns = self.lefts
        screen.blit(self.turns[self.count//4],(self.turn[self.c]+camera_x,self.y))
        pygame.draw.line(screen,color['red'],(self.turn[self.c] + camera_x,self.y),(self.turn[self.c] + self.width + camera_x,self.y),5)
        pygame.draw.line(screen,color['lightgreen'],(self.turn[self.c] + camera_x,self.y),(self.turn[self.c] + self.width*(self.life/2) + camera_x,self.y),5)
        pygame.draw.rect(screen,color['white'],(self.turn[self.c] + camera_x,self.y-3,self.width ,6),1)
        self.c+=4
        self.count+=1
        
#SURIKENS
class Shoot:
    def __init__(self,x,y,host='boss',look=-1,vel=0,angle=0):
        self.x = x
        self.y = y
        self.look = look
        self.host = host
        self.vel = vel
        self.angle = angle
    def move(self):
        suriken = pygame.transform.scale(pygame.image.load('bots img/shuriken.png'),(40,30))
        if self.host == 'boss':
            if self.vel==0:
                screen.blit(suriken,(self.x+camera_x,self.y))
            else:
                screen.blit(pygame.transform.rotate(suriken,self.angle),(self.x,self.y))
                self.y += self.vel
            self.x -= 20
        else:
            if self.look==-1:
                screen.blit(suriken,(self.x+camera_x,self.y))
            if self.look==1:
                screen.blit(pygame.transform.rotate(suriken,180),(self.x+camera_x,self.y))
            self.x+=(20*self.look)

#Scroll Papers
class Papers:
    def __init__(self,x,y):
        self.y = y-15
        self.x = x
        self.list = [i for i in range(self.y,self.y+16)]
        self.reverse=self.list[::-1]
        self.up = random.choice([True,False])
        self.c = 0                    
    def move(self):
        paper = pygame.transform.rotozoom(pygame.image.load('scroll_paper.png'),60,0.1)
        if self.c>=15:
            self.c=0
            self.up = not self.up
        self.c+=1
        if self.up:
            screen.blit(paper,(self.x+camera_x,self.list[self.c]+camera_y))
        else:
            screen.blit(paper,(self.x+camera_x,self.reverse[self.c]+camera_y))

class Meat:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        meat = pygame.image.load('meat.png')
        meat = pygame.transform.scale(meat,(40,40))
        screen.blit(meat,(self.x+camera_x,self.y))
# Boss
boss_rect=pygame.Rect(900,326,55,70)
boss_life = 15
def boss():
    global boss_shoot, boss_count, boss_x, boss_y,y,x
    pygame.draw.line(screen,color['red'],(boss_x - 2 + camera_x,boss_y),(boss_x + 58 + camera_x,boss_y),5)
    pygame.draw.line(screen,color['lightgreen'],(boss_x - 2 + camera_x,boss_y),(boss_x + boss_life*4-2 + camera_x,boss_y),5)
    pygame.draw.rect(screen,color['white'],(boss_x - 2 + camera_x,boss_y-3,61,6),1)
    steps = [pygame.transform.scale(pygame.image.load('bots img/step-1.png'),(55,70)),
             pygame.transform.scale(pygame.image.load('bots img/step-2.png'),(55,70)),
             pygame.transform.scale(pygame.image.load('bots img/step-3.png'),(55,70)),
             pygame.transform.scale(pygame.image.load('bots img/step-4.png'),(55,70))]
    steps += [pygame.transform.scale(pygame.image.load('bots img/step-1.png'),(55,70))]*4
    boss_count %= 50
    screen.blit(steps[boss_count//7],(boss_x+camera_x,boss_y))
    boss_count+=1
    if boss_count == 15:
        if boss_y <= y <= boss_y+70:
            boss_shoots.append(Shoot(boss_x,boss_y+30))
        else:
            angle = int(math.degrees(math.asin(y/((boss_x-x)**2+y**2))))
            if y+camera_y > boss_y+70:
                vel = -20*math.sin(math.radians(angle))/math.sin(math.radians(90-angle))
                boss_shoots.append(Shoot(boss_x,boss_y+30,'boss',-1,vel,-(angle)))
                #screen.blit(pygame.transform.rotate(suriken,self.angle*(-1)),(self.x+camera_x,self.y))
                #self.y -= (20*math.sin(math.radians(self.angle))/math.sin(math.radians(90-self.angle)))
            if y+camera_y < boss_y:
                vel = 20*math.sin(math.radians(angle))/math.sin(math.radians(90-angle))
                boss_shoots.append(Shoot(boss_x,boss_y+30,'boss',-1,vel,angle))
                #screen.blit(pygame.transform.rotate(suriken,self.angle),(self.x+camera_x,self.y))
                #self.y += (20*math.sin(math.radians(self.angle))/math.sin(math.radians(90-self.angle)))
            
# meat and paper images and shrift sizes
paper = pygame.transform.rotozoom(pygame.image.load('scroll_paper.png'),60,0.12)
meat = pygame.image.load('meat.png')
meat = pygame.transform.scale(meat,(40,50))
score_size = pygame.font.SysFont('Comic Sans',50)

# game over variables
gameover = pygame.font.SysFont('ALGERIAN', 100)
# you win variables
youwin = pygame.font.SysFont('Comic Sans', 40,True)
youwin_ph = pygame.image.load('you win.png')
youwin_ph = pygame.transform.scale(youwin_ph,(600,400))
#general game loop
done = False
pygame.mixer.music.play(-1)
while not done:
    if phase==preview:
        Preview()
        if elite_count==350:
            phase = phase_menu
            music(phase_menu)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                Sure()
    if phase== phase_menu or phase== phase_help or phase==phase_options or phase==phase_skin:
        #general background
        fps = 35
        list_of_stars.append(Stars())
        screen.blit(menu_bckgr, (0,0)) 
        for i in list_of_stars:
            i.move()
            if i.y>600:
                list_of_stars.remove(i)

        left_eye_y, right_eye_y= 0,460
        load_count = 0

        if phase==phase_menu:
            # main menu
            mouse = pygame.mouse.get_pos()
            for i in list_of_items:
                if i[0]<mouse[0]<i[0]+250 and i[1]<mouse[1]<i[1]+70:
                    numb_item = i[-1]
                if numb_item == i[-1]:
                    screen.blit(str1.render(i[2],True,i[3],color['black']),(i[0],i[1])) 
                else:
                    screen.blit(str1.render(i[2],True,i[3]),(i[0],i[1]))
                    numb_item = 0

            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    click_sound.play()
                    Sure()
                if i.type==pygame.MOUSEBUTTONDOWN and i.button==pygame.BUTTON_LEFT:
                    if 100<=i.pos[0]<=100+150 and 100<=i.pos[1]<=100+70: #позиции для выбора плэй
                        click_sound.play()
                        phase=phase_skin     
                    if 100<=i.pos[0]<=100+150 and 300<=i.pos[1]<=300+70:
                        click_sound.play()
                        phase=phase_help
                    if 100<=i.pos[0]<=100+200 and 200<=i.pos[1]<=200+70:
                        click_sound.play()
                        phase=phase_options
                    if 100<=i.pos[0]<=100+150 and 400<=i.pos[1]<=400+70:
                        click_sound.play()
                        Sure()
            x_speed = 10
            y_speed = -28
        if phase== phase_help:
            # Help
            mouse = pygame.mouse.get_pos()
            if 50<=mouse[0]<=50+120 and 25<=mouse[1]<=25+55:
                pygame.draw.polygon(screen,color ['darkgoldenrod4'], [(50, 50), (80, 80), (80, 25)])
                pygame.draw.line(screen,color['darkgoldenrod4'], [80, 50], [120, 50], 15)
            else:
                pygame.draw.polygon(screen,color['gold'], [(50, 50), (80, 80), (80, 25)])
                pygame.draw.line(screen,color['gold'], [80, 50], [120, 50], 15)
            a = 0
            for i in text_help.split('\n'):
                screen.blit(hshrift.render(i, True, color['darkolivegreen1']), (100,100+a))
                a+=50
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    click_sound.play()
                    Sure()
                if i.type==pygame.MOUSEBUTTONDOWN and i.button==pygame.BUTTON_LEFT:
                    if 50<=i.pos[0]<=50+120 and 25<=i.pos[1]<=25+55:
                        click_sound.play()
                        phase=phase_menu
        if phase==phase_options:
            #Options
            mouse = pygame.mouse.get_pos()
            if 50<=mouse[0]<=50+120 and 25<=mouse[1]<=25+55:
                pygame.draw.polygon(screen,color ['darkgoldenrod4'], [(50, 50), (80, 80), (80, 25)])
                pygame.draw.line(screen,color['darkgoldenrod4'], [80, 50], [120, 50], 15)
            else:
                pygame.draw.polygon(screen,color ['gold'], [(50, 50), (80, 80), (80, 25)])
                pygame.draw.line(screen,color['gold'], [80, 50], [120, 50], 15)
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    done=False
                if i.type==pygame.MOUSEBUTTONDOWN and i.button==pygame.BUTTON_LEFT:
                    if 50<=i.pos[0]<=50+120 and 25<=i.pos[1]<=25+55:
                        click_sound.play()
                        phase=phase_menu
                if i.type==pygame.MOUSEBUTTONDOWN and i.button==pygame.BUTTON_LEFT:
                    if 20<=i.pos[0]<=20+120 and 265<=i.pos[1]<=265+100:
                        click_sound.play()
                        pygame.mixer.music.set_volume(0)
                if i.type==pygame.MOUSEBUTTONDOWN and i.button==pygame.BUTTON_LEFT:
                    if 20<=i.pos[0]<=20+120 and 140<=i.pos[1]<=140+100:
                        click_sound.play()
                        pygame.mixer.music.set_volume(0.8)
                if i.type==pygame.MOUSEBUTTONDOWN and i.button==pygame.BUTTON_LEFT:
                    if 45<=i.pos[0]<=45+100 and 470<=i.pos[1]<=470+100:
                        click_sound.play()
                        volume+=0.1
                        pygame.mixer.music.set_volume(volume)
                if i.type==pygame.MOUSEBUTTONDOWN and i.button==pygame.BUTTON_LEFT:
                    if 180<=i.pos[0]<=180+100 and 470<=i.pos[1]<=470+100:
                        click_sound.play()
                        volume-=0.1
                        pygame.mixer.music.set_volume(volume)
            screen.blit(sound_off, (20,265))
            screen.blit(sound_on, (20,140))
            screen.blit(option_str.render('Music', True, color['gold']), (60,100))
            screen.blit(option_str1.render('- on', True, color['gold']), (180,185))
            screen.blit(option_str1.render('- off', True, color['gold']), (180,305))
            screen.blit(option_str.render('Volume', True, color['gold']), (50,400))
            screen.blit(zagolovok.render('Options', True, color['deepskyblue']), (350,15))
            screen.blit(plus, (45,470))
            screen.blit(minus, (180,470))

        if phase == phase_skin:
            screen.blit(option_str.render('Choose the skin to start', True, color['dodgerblue4']), (130,100))
            skin_bg=[
                [250,200,200,250], # координаты рамки наруто
                [600,200,200,250]  # координаты рамки саске
            ]
            mouse = pygame.mouse.get_pos()
            if 50<=mouse[0]<=50+120 and 25<=mouse[1]<=25+55:
                pygame.draw.polygon(screen,color ['darkgoldenrod4'], [(50, 50), (80, 80), (80, 25)])
                pygame.draw.line(screen,color['darkgoldenrod4'], [80, 50], [120, 50], 15)
            else:
                pygame.draw.polygon(screen,color ['gold'], [(50, 50), (80, 80), (80, 25)])
                pygame.draw.line(screen,color['gold'], [80, 50], [120, 50], 15)
            for i in skin_bg:
                if i[0]<=mouse[0]<=i[0]+i[2] and i[1]<=mouse[1]<=i[1]+i[3]:
                    pygame.draw.rect(screen,color['dodgerblue4'],i,10,6)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    click_sound.play()
                    Sure()
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == pygame.BUTTON_LEFT:
                    if 50<=i.pos[0]<=50+120 and 25<=i.pos[1]<=25+55:
                        click_sound.play()
                        phase = phase_menu
                    if 250<=i.pos[0]<=250+200 and 200<=i.pos[1]<=200+250:
                        click_sound.play()
                        chosen = 'naruto'
                        music(phase_game)
                        Loading(phase_game)
                    if 600<=i.pos[0]<=600+200 and 200<=i.pos[1]<=200+250:
                        click_sound.play()
                        chosen = 'sasuke'
                        music(phase_game)
                        Loading(phase_game)
            screen.blit(pygame.transform.scale(pygame.image.load('menu/naruto.png'),(200,200)),(250,200))
            screen.blit(pygame.transform.scale(pygame.image.load('menu/sasuke.png'),(200,200)),(600,200))
            screen.blit(option_str1.render('NARUTO', True, color['black'], color['orange']), (280,470))
            screen.blit(option_str1.render('SASUKE', True, color['black'], color['royalblue']), (620,470))
            lefts = [
                pygame.image.load(chosen+'/k.png'),
                pygame.image.load(chosen+'/l.png'),
                pygame.image.load(chosen+'/m.png'),
                pygame.image.load(chosen+'/n.png'),
                pygame.image.load(chosen+'/o.png'),
                pygame.image.load(chosen+'/q.png')
            ]
            rights = [
                pygame.image.load(chosen+'/d.png'),
                pygame.image.load(chosen+'/e.png'),
                pygame.image.load(chosen+'/f.png'),
                pygame.image.load(chosen+'/g.png'),
                pygame.image.load(chosen+'/h.png'),
                pygame.image.load(chosen+'/i.png')
            ]
            start_pos = pygame.image.load(chosen+'/a.png')
            jumping = pygame.image.load(chosen+'/c.png')
            right_attacks = [
                pygame.image.load(chosen+'/b.png'),
                pygame.image.load(chosen+'/t.png')
            ]
            left_attacks = [
                pygame.image.load(chosen+'/p.png'),
                pygame.image.load(chosen+'/v.png')
            ]
            damaged = pygame.image.load(chosen+'/r.png')
            lying = pygame.image.load(chosen+'/j.png')

            # приравниваем переменные на перванальные чтобы рестартить
            list_bots_1 = []
            list_bots_2 = []
            list_bots_3 = []
            list_papers_1 = []
            list_papers_2 = []
            list_papers_3 = []
            list_meat_1 = []
            list_meat_2 = []
            list_meat_3 = []
            x = 240
            y = 0
            m = level1
            skin_life = 5
            camera_x, camera_y = 0, 0
            meat_count = 0
            paper_count = 0
            for i in range(len(level1)):
                for j in range(len(level1[i])):
                    if level1[i][j]=='H':
                        list_bots_1.append(EarthBots(j*block_size,i*block_size+10,'boar'))
                    if level1[i][j]=='P':
                        list_papers_1.append(Papers(j*block_size,i*block_size))
                    
            for i in range(len(level2)):
                for j in range(len(level2[i])):
                    if level2[i][j]=='k':
                        list_bots_2.append(AirBots(j*block_size,i*block_size))
                    if level2[i][j]=='G':
                        list_bots_2.append(EarthBots(j*block_size,i*block_size-35,'bear'))
                    if level2[i][j]=='P':
                        list_papers_2.append(Papers(j*block_size,i*block_size))

            for i in range(len(level3)):
                for j in range(len(level3[i])):
                    if level3[i][j]=='k':
                        list_bots_3.append(AirBots(j*block_size,i*block_size))
                    if level3[i][j]=='P':
                        list_papers_3.append(Papers(j*block_size,i*block_size))
            boss_x,boss_y = 900,326
            boss_count = 0
            boss_shoots = []
            boss_life = 15
            skin_shoots = []
            game_y = 620
            gameover_velocity = 5
            youwin_y = 620
            youwin_velocity = 2
            youwin1_y = -20
            youwin1_velocity = 2
            music_up = False
            left_eye_y, right_eye_y= 0,460
            win_count = 0
    if phase == phase_game:
        if x < 0:
            x = 0
        # level backgrounds
        bg_pos=(camera_x//6)%size[0] 
        
        if m==level1:
            screen.blit(bg1,(bg_pos,0))
            screen.blit(bg1,(bg_pos-size[0],0))
        elif m==level2:
            screen.blit(bg,(bg_pos,0))
            screen.blit(bg,(bg_pos-size[0],0))
        elif  m==level3:
            screen.blit(bg2,(bg_pos,0))
            screen.blit(bg2,(bg_pos-size[0],0))
        
        if m==level1:
            fps = 45
            if y > 600:
                m = level2
                x = 860
                y = 000
                camera_x,camera_y=0,0
        elif m==level2:
            fps = 45
            if y > 600:
                m = level3
                x = 300
                y = 000
                camera_x,camera_y=0,0
        
        dy += gravity
        if dy > 20:
            dy = 20
        # save x and y
        save_x, save_y = x, y
        # increase y
        y += dy
        skin_rect = pygame.Rect(x, y, 50, 50)
        collide = False
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] in "2st3bzuovBCDEFfqgehm6":
                    rect2 = pygame.Rect(j*block_size, i*block_size, block_size, block_size)
                    if skin_rect.colliderect(rect2):
                        collide = True
                elif m[i][j] in 'd8x':
                    rect4=pygame.Rect(j*block_size+24, i*block_size+12, block_size, block_size)
                    rect3=pygame.Rect(j*block_size+12, i*block_size+24, block_size, block_size)
                    rect5=pygame.Rect(j*block_size+35, i*block_size, block_size, block_size)
                    rect6=pygame.Rect(j*block_size, i*block_size+35, block_size, block_size)
                    if skin_rect.colliderect(rect3) or skin_rect.colliderect(rect4) or skin_rect.colliderect(rect5)or skin_rect.colliderect(rect6):
                        collide=True
                elif m[i][j] in 'i7A':
                    rect5=pygame.Rect(j*block_size-17, i*block_size+17, block_size, block_size)
                    rect6=pygame.Rect(j*block_size+1, i*block_size+35, block_size, block_size)
                    if skin_rect.colliderect(rect3) or skin_rect.colliderect(rect4)or skin_rect.colliderect(rect5)or skin_rect.colliderect(rect6):
                        collide=True

        if collide:
            y = save_y
            # collide while going down?
            if dy > 0:
                jump_is_allowed = True
            dy = 0
        if y+camera_y > size[1]*1:
            camera_y=camera_y
        if y+camera_y < size[1]*0.01:
            camera_y=camera_y 

        # change x
        x += dx
        skin_rect = pygame.Rect(x, y, 50, 50)
        collide = False
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] in "2st3bzuovBCDEFfqgehm6" :
                    rect2 = pygame.Rect(j*block_size, i*block_size, block_size, block_size)
                    if skin_rect.colliderect(rect2):
                        collide = True
                elif m[i][j] in 'd8x':
                    rect4=pygame.Rect(j*block_size+24, i*block_size+12, block_size, block_size)
                    rect3=pygame.Rect(j*block_size+12, i*block_size+24, block_size, block_size)
                    rect5=pygame.Rect(j*block_size+35, i*block_size, block_size, block_size)
                    rect6=pygame.Rect(j*block_size, i*block_size+35, block_size, block_size)
                    if skin_rect.colliderect(rect3) or skin_rect.colliderect(rect4)or skin_rect.colliderect(rect5)or skin_rect.colliderect(rect6):
                        collide=True
                elif m[i][j] in 'i7A':
                    #rect4=pygame.Rect(j*block_size-24, i*block_size-12, block_size, block_size)
                    rect3=pygame.Rect(j*block_size, i*block_size+17, block_size//2, block_size//2)
                    rect5=pygame.Rect(j*block_size-17, i*block_size+17, block_size, block_size)
                    rect6=pygame.Rect(j*block_size+1, i*block_size+35, block_size, block_size)
                    if skin_rect.colliderect(rect3) or skin_rect.colliderect(rect4) or skin_rect.colliderect(rect5)or skin_rect.colliderect(rect6):
                        collide=True

        if collide:
            x = save_x

        if x + camera_x > size[0]*0.7:
            camera_x = camera_x - 10
        if x + camera_x < size[0]*0.3:
            camera_x = camera_x + 10

        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == "b":
                    screen.blit(block1, (j*block_size + camera_x,i*block_size+ camera_y))
                if m[i][j] == "L":
                    screen.blit(level, (j*block_size + camera_x,i*block_size+ camera_y))    
                if m[i][j] == "c":
                    screen.blit(cloud, (j*block_size + camera_x//3, i*block_size+ camera_y))
                if m[i][j] == "2":
                    screen.blit(block2, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "3":
                    screen.blit(block3, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "s":
                    screen.blit(block5, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "6":
                    screen.blit(block, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "7":
                    screen.blit(block7, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "n":
                    screen.blit(block7c, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "8":
                    screen.blit(block8, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "9":
                    screen.blit(block9, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "w":
                    screen.blit(block10, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "q":
                    screen.blit(block12, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "e":
                    screen.blit(block11, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "r":
                    screen.blit(block13, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "t":
                    screen.blit(block14, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "y":
                    screen.blit(block15, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "g":
                    screen.blit(block16, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "h":
                    screen.blit(block17, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "m":
                    screen.blit(block18, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "d":
                    screen.blit(block19, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "i":
                    screen.blit(block20, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "j":
                    screen.blit(block21, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "f":
                    screen.blit(block22, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "o":
                    screen.blit(block23, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "u":
                    screen.blit(block24, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "z":
                    screen.blit(block25, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "x":
                    screen.blit(block26, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "v":
                    screen.blit(block27, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "A":
                    screen.blit(block28, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "B":
                    screen.blit(block29, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "C":
                    screen.blit(block30, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "D":
                    screen.blit(block31, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "E":
                    screen.blit(block32, (j*block_size + camera_x, i*block_size+ camera_y))
                if m[i][j] == "F":
                    screen.blit(block33, (j*block_size + camera_x, i*block_size+ camera_y))
        screen.blit(pause_button,(930,0))
        if m==level1:
            for i in list_bots_1:
                i.move()
                if i.life==0:
                    list_meat_1.append(Meat(i.turn[i.c],i.y))
                    list_bots_1.remove(i)
                    fps-=1   
                bot_rect = pygame.Rect(i.turn[i.c],i.y,i.width,i.height)
                if skin_rect.colliderect(bot_rect):
                    damage = True
                    skin_life-=0.5
                    break
            for i in list_papers_1:
                i.move()
                if i.up:
                    rect_paper = pygame.Rect(i.x,i.list[i.c],40,25)
                else:
                    rect_paper = pygame.Rect(i.x,i.reverse[i.c],40,25)
                if skin_rect.colliderect(rect_paper):
                    bonus_sound.play()
                    paper_count+=1
                    list_papers_1.remove(i)
            for i in list_meat_1:
                i.draw()
                meat_rect = pygame.Rect(i.x,i.y,40,40)
                if skin_rect.colliderect(meat_rect):
                    bonus_sound.play()
                    meat_count+=1
                    list_meat_1.remove(i)
        if m==level2:
            for i in list_bots_2:
                i.move()
                if i.life==0:
                    list_bots_2.remove(i)
                    list_meat_2.append(Meat(i.turn[i.c],i.y))
                    fps-=1
                bot_rect= pygame.Rect(i.turn[i.c],i.y,i.width,i.height)
                if skin_rect.colliderect(bot_rect):
                    damage=True
                    skin_life-=0.5
            for i in list_papers_2:
                i.move()
                if i.up:
                    rect_paper = pygame.Rect(i.x,i.list[i.c],40,25)
                else:
                    rect_paper = pygame.Rect(i.x,i.reverse[i.c],40,25)
                if skin_rect.colliderect(rect_paper):
                    bonus_sound.play()
                    paper_count+=1
                    list_papers_2.remove(i)
            for i in list_meat_2:
                i.draw()
                meat_rect = pygame.Rect(i.x,i.y,40,40)
                if skin_rect.colliderect(meat_rect):
                    bonus_sound.play()
                    meat_count+=1
                    list_meat_2.remove(i)
        if m==level3:
            fps = 25
            if boss_life>0:
                boss()
                if boss_rect.colliderect(skin_rect):
                    damage=True
                    skin_life-=0.5
            for i in boss_shoots:
                i.move()
                boss_shoot_rect=pygame.Rect(i.x-15,i.y,30,25)
                if boss_shoot_rect.colliderect(skin_rect):
                    damage=True
                    skin_life-=1
                    boss_shoots.remove(i)
                for j in range(len(m)):
                    for k in range(len(m[j])):
                        if m[j][k] in "2ws3zuxvfbegmh6di87qDFt":
                            rect2 = pygame.Rect(k*block_size, j*block_size, block_size, block_size)
                            if boss_shoot_rect.colliderect(rect2):
                                boss_shoots.remove(i)
            for i in list_bots_3:
                i.move()
                if i.life==0:
                    list_bots_3.remove(i)
                bot_rect= pygame.Rect(i.turn[i.c],i.y,i.width,i.height)
                if skin_rect.colliderect(bot_rect):
                    damage=True
                    skin_life-=0.5
            for i in list_papers_3:
                i.move()
                if i.up:
                    rect_paper = pygame.Rect(i.x,i.list[i.c],40,25)
                else:
                    rect_paper = pygame.Rect(i.x,i.reverse[i.c],40,25)
                if skin_rect.colliderect(rect_paper):
                    bonus_sound.play()
                    paper_count+=1
                    list_papers_3.remove(i)
            if boss_life==0:
                if not music_up:
                    music(boss_life)
                    music_up = True
                win_count+=1
                screen.blit(youwin.render('Congratulations on completing', True, color['green']), (550,youwin_y))
                screen.blit(youwin.render('the “Naruto’s Adventure” game', True, color['green']), (550,youwin_y+40))
                screen.blit(youwin.render('from the Elite studio', True, color['green']), (580,youwin_y+80))
                youwin_y-=youwin_velocity
                screen.blit(youwin_ph, (200,youwin1_y))
                youwin1_y += youwin1_velocity
                if youwin_y==450:
                    youwin_velocity=0
                if youwin1_y==50:
                    youwin1_velocity=0
                if win_count == 200:
                    Titles()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Sure()
                    if event.type==pygame.MOUSEBUTTONDOWN and event.button==pygame.BUTTON_LEFT:
                        if 50<=event.pos[0]<=50+120 and 25<=event.pos[1]<=25+55:
                            click_sound.play()
                            phase = phase_menu
                            music(phase_menu)

        # naruto's move animation
        if skin_life>0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Sure()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Pause()
                    if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                        if jump_is_allowed:
                            jump_sound.play()
                            dy = -28
                            jump_is_allowed = False
                    if event.key == pygame.K_a:
                        dx = -(x_speed)
                        left = True
                        right = False
                    if event.key == pygame.K_d:
                        dx = x_speed
                        left = False
                        right = True
                    if event.key == pygame.K_COMMA:
                        if len(skin_shoots)<=0:
                            left_attack = True
                            skin_shoots.append(Shoot(x+20,y+20,'naruto',-1))
                            shoot_sound.play()
                    if event.key == pygame.K_PERIOD:
                        if len(skin_shoots)<=0:
                            right_attack = True
                            skin_shoots.append(Shoot(x,y+20,'naruto',1))
                            shoot_sound.play()
                if event.type == pygame.KEYUP:  # Released something
                    if event.key == pygame.K_a:
                        if dx < 0:
                            dx = 0
                            left = False
                            right = False
                            count_anim = 0
                    if event.key == pygame.K_d:
                        if dx > 0:
                            dx = 0
                            left = False
                            right = False
                            count_anim = 0
                    if event.key == pygame.K_COMMA:
                        left_attack = False
                        attack_anim = 0
                    if event.key == pygame.K_PERIOD:
                        right_attack = False
                        attack_anim = 0
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT and 930<=event.pos[0]<=1000 and 0<=event.pos[1]<=70:
                    click_sound.play()
                    Pause()
            if damage_anim >= 10:
                damage = False
                damage_anim = 0
            count_anim %= 15
            attack_anim %=18
            if damage:
                jump_is_allowed = False
                dx = 0
                screen.blit(damaged,(x+camera_x,y+camera_y))
                x-=10
                y-=17
                damage_anim+=1
            elif right_attack:
                screen.blit(right_attacks[attack_anim//6],(x+camera_x,y+ camera_y))
            elif left_attack:
                screen.blit(left_attacks[attack_anim//6],(x+camera_x,y+ camera_y))
            elif not jump_is_allowed:
                screen.blit(jumping,(x+camera_x,y+ camera_y))
            elif left:
                screen.blit(lefts[count_anim//3],(x+camera_x,y+ camera_y))
                count_anim+=1
            elif right:
                screen.blit(rights[count_anim//3],(x+camera_x,y+ camera_y))
                count_anim+=1
            else:
                screen.blit(start_pos,(x+camera_x,y+ camera_y))
            # for life heart
            if skin_life < 5 and meat_count>  0:
                skin_life = skin_life + 0.25
                meat_count -= 1
                
                if skin_life>5:
                    skin_life = 5 
            screen.blit(pygame.transform.scale(full_heart,(35,35)),(-3,-3))
            pygame.draw.line(screen,color['red'],(35,15),(260,15),20)
            pygame.draw.line(screen,color['green'],(35,15),(35 + 45*skin_life,15),20)
            pygame.draw.rect(screen,color['white'],(35,5,225,20),2)
            # for paper and meat count
            screen.blit(paper,(0,35))
            screen.blit(score_size.render(f': {paper_count}/25',True,color['orangered2']),(40,45))
            screen.blit(meat,(0,85))
            screen.blit(score_size.render(f': {meat_count}/20',True,color['orangered2']),(40,90))            
        else:# when he loses
            if not music_up:
                music(skin_life)
                music_up = True
            screen.blit(lying,(x+camera_x,y+camera_y))
            dx = 0
            screen.blit(gameover.render('Game Over!', True, color['red4']), (220,game_y))
            game_y-=gameover_velocity
            if game_y==300:
                gameover_velocity=0
            pygame.draw.polygon(screen,color ['gold'], [(50, 50), (80, 80), (80, 25)])
            pygame.draw.line(screen,color['gold'], [80, 50], [120, 50], 15) 
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Sure()
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==pygame.BUTTON_LEFT:
                    if 50<=event.pos[0]<=50+120 and 25<=event.pos[1]<=25+55:
                        click_sound.play()
                        Loading(phase_menu)
                        music(phase_menu)

        for i in skin_shoots:
            i.move()
            shoot=pygame.Rect(i.x-15,i.y,30,25)
            for j in range(len(m)):
                for k in range(len(m[j])):
                    if m[j][k] in "2ws3zuxvfbegmh6di87qDFt":
                        rect2 = pygame.Rect(k*block_size, j*block_size, block_size, block_size)
                        if shoot.colliderect(rect2):
                            if i in skin_shoots:
                                skin_shoots.remove(i)
            if m==level1:    
                for j in list_bots_1:
                    bot_rect=pygame.Rect(j.turn[j.c],j.y,j.width,j.height)
                    if shoot.colliderect(bot_rect):
                        shoot_collide.play()
                        j.life-=1
                        if i in skin_shoots:
                            skin_shoots.remove(i)
            if m==level2:
                for j in list_bots_2:
                    bot_rect=pygame.Rect(j.turn[j.c],j.y,j.width,j.height)
                    if shoot.colliderect(bot_rect):
                        shoot_collide.play()
                        j.life-=1
                        if i in skin_shoots:
                            skin_shoots.remove(i)
            if m==level3:
                for j in list_bots_3:
                    bot_rect=pygame.Rect(j.turn[j.c],j.y,j.width,j.height)
                    if shoot.colliderect(bot_rect):
                        shoot_collide.play()
                        j.life-=1
                        if i in skin_shoots:
                            skin_shoots.remove(i)
                if shoot.colliderect(boss_rect):
                        shoot_collide.play()
                        boss_life-=1
                        if i in skin_shoots:
                            skin_shoots.remove(i)
                if boss_life == 0:
                    music(boss_life)
            if i.x > x+600 or i.x < x-600:
                if i in skin_shoots:
                    skin_shoots.remove(i)
        if (m==level2 or m==level3) and 0<=y<90:
            screen.fill(color['black'])
            screen.blit(fon,(0,150))
            y-=1
        
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
