import pygame
import math
pygame.init()
screen=pygame.display.set_mode((700,600))
clock = pygame.time.Clock()
pygame.display.set_caption('Sprouts')
screen.fill("green")
f=True
pen=False
c=0
dot=False
drawing=False
intersection=False
dots=[]
lines=[]
coordinates=[]
pen_cursor = pygame.image.load('pen.png').convert_alpha()
dot_cursor = pygame.image.load('dot.png').convert_alpha()
common_p=[]

def draw_line(position):
    global c
    pos=position
    if c%2==0:
        pygame.draw.circle(screen,"black",pos,5)
    elif c%2==1:
        pygame.draw.circle(screen,"blue",pos,5)
    pygame.display.flip()
    clock.tick(500)
def distance(p1,p2):
    d=math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return d
def list_d(l,p):
    s=False
    for j in l:
        if distance(j,p)<=10:
            s=True
    return s
def points_no(i):
    points=0
    for j in lines:
        s=False
        j1=[j[0]]
        j2=[j[-1]]
        j3=j[10:len(j)-10]
        if list_d(j1,i):
            points+=1

            if j1==j2:
                points+=1
        elif list_d(j2,i):

            points+=1

            if j1==j2:
                points+=1
        elif list_d(j3,i):

            points+=2
    return points                        
    
while f:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:

            if mouse[0]>5 and mouse[0]<40 and mouse[1]>560 and mouse[1]<590:
                if pen==True:
                    pygame.draw.rect(screen,(200,200,200),[5,565,30,30])
                    pygame.mouse.set_visible(True)
                    pen=False

                else:
                    dot=False
                    pygame.draw.rect(screen,(230,230,230),[5,565,30,30])
                    pen=True
                 
            elif mouse[0]>45 and mouse[0]<70 and mouse[1]>560 and mouse[1]<590:
                if dot==True:
                    pygame.draw.rect(screen,(200,200,200),[47,565,30,30])
                    pygame.mouse.set_visible(True)
                    dot=False
                
                else:
                    pygame.draw.rect(screen,(230,230,230),[47,565,30,30])
                    pen=False
                    dot=True
                   
                    
        if event.type==pygame.MOUSEBUTTONDOWN and dot==True and mouse[1]<570:
                pygame.draw.circle(screen,"red",pygame.mouse.get_pos(),10)
                dots.append(pygame.mouse.get_pos())
                pygame.display.flip()
                
        elif event.type == pygame.MOUSEMOTION and pen==True and mouse[1]<570 :
                if (drawing):
                    (x,y) = pygame.mouse.get_pos()
                    coordinates.append((x,y))
                    draw_line((x,y))
        elif event.type == pygame.MOUSEBUTTONDOWN and pen==True and mouse[1]<570:
            points=0
            for i in dots:
                if distance(i,pygame.mouse.get_pos())<=15:
                    points=points_no(i)
                    coordinates=[]
                    if points<3:
                        pygame.mouse.set_pos(i)
                        coordinates.append(i)
                        c+=1
                        drawing=True
                    
            
        elif event.type==pygame.MOUSEBUTTONUP and pen==True and mouse[1]<560:
            found=False
            three=False
            for i in dots:
                if distance(i,pygame.mouse.get_pos())<=15:
                    found=True
                    s=1
                    if points_no(i)>=3:
                        three=True

                        for j in coordinates[5:len(coordinates)-5:1]:
                            pygame.draw.circle(screen,"green",j,5)
                        pygame.draw.circle(screen,"red",i,10)
                        pygame.draw.circle(screen,"red",coordinates[0],10)
                        c-=1
                    else:
                        
                        draw_line(i)
                        coordinates.append(i)
                        pygame.mouse.set_pos(i)
            if found==False and coordinates!=[]:
                print("not  found")
                c-=1
                try:
                    d=coordinates[0]
                except:
                    pass
                for j in coordinates[4:len(coordinates)]:
                    pygame.draw.circle(screen,"green",j,5)
                pygame.draw.circle(screen,"red",d,10)
                pygame.draw.circle(screen,"red",d,10)
            common_p=[]
            list_col=[]
            intersection=False
            for s in coordinates[10:len(coordinates)-10]:
                h=0
                for i in lines:
                    for j in i:
                        if distance(s,j)<=4:
                            common_p.append(s)
                            list_col.append([s,h])
                            intersection=True
                    h+=1
            if intersection== True and found == True and not three:

                c-=1
                try:
                    d=coordinates[0]
                except:
                    pass
                for j in coordinates[4:len(coordinates)]:
                    if j not in common_p:
                        pygame.draw.circle(screen,"green",j,5)
                pygame.draw.circle(screen,"red",d,10)
                pygame.draw.circle(screen,"red",coordinates[-1],10)
                for p in list_col:
                    if p[1]%2==0:
                        pygame.draw.circle(screen,"blue",p[0],4)
                    else:
                        pygame.draw.circle(screen,"black",p[0],4)
            
            if found==True and intersection==False and not three:
                lines.append(coordinates)
            coordinates=[]
            drawing = False
    
    image_pen=pygame.image.load("pen.png")
    image_dot=pygame.image.load("dot.png")
    mouse = pygame.mouse.get_pos()
    if mouse[0]>5 and mouse[0]<40 and mouse[1]>560 and mouse[1]<590:
         pygame.draw.rect(screen,(230,230,230),[5,565,30,30])
    else:
        pygame.draw.rect(screen,(200,200,200),[5,565,30,30])
        
    if mouse[0]>45 and mouse[0]<70 and mouse[1]>560 and mouse[1]<590:
         pygame.draw.rect(screen,(230,230,230),[47,565,30,30])
    else:
        pygame.draw.rect(screen,(200,200,200),[47,565,30,30])
   

    
        
    pygame.draw.line(screen,"red",(0,560),(700,560),width=2)            
    screen.blit(image_pen,(5,565))
    screen.blit(image_dot,(50,567))
    pygame.display.flip()
    #



