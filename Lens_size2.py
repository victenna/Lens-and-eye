import pygame,sys
pygame.init()
timer = pygame.time.Clock()
screen = pygame.display.set_mode([1400,800])
screen.fill([68,242,244])
keep_going = True
img = pygame.image.load('lens4.png')
img1,img1_rev=[],[]
img2=pygame.image.load('eye1.png')
img2=pygame.transform.scale(img2,(500,450))

Point1=(50,290)
Point2=(355,290)
Point3=Point2

Point5=(50,450)
Point6=(355,450)
Point7=Point6



N=50
for i in range(N):
    img1.append(pygame.transform.scale(img,(50+2*i,700)))
img1_rev=img1[::-1]
for i in range(N,2*N):
    img1.append(img1_rev[i-N])


img3=pygame.image.load('triangle3.png')
img4,img4_rev=[],[]

for i in range(N):
    img4.append(pygame.transform.scale(img3,(450-3*i,120-i)))
img4_rev=img4[::-1]
for i in range(N,2*N):
    img4.append(img4_rev[i-N])

img5=pygame.image.load('lens_eye2.png')
img6=pygame.image.load('lens_eye2(2).png')
img7=pygame.image.load('lens_eye2(3).png')
#img5=pygame.transform.scale(img5,(300,200))
n,n1=0,0    
keep_going=True
while keep_going:
    n=n+1
    n1=n%(2*N)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill('goldenrod')
    #----------------------------------------------------------------
   
    screen.blit(img5,(500,10))
    screen.blit(img6,(550,580))
    screen.blit(img7,(1050,580))
    
    screen.blit(img2,(730,140))
    screen.blit(img1[n1],(330,40))
    if n1<N:
        Point4=(800,315+n1*0.5)
        Point8=(800,435-n1*0.5)
        
        
        screen.blit(img4[n1],(800,315+n1*0.5))
        N2=315+n1
        N3=435-n1
    if n1>N-1:
        Point4=(800,N2-n1*0.5)
        Point8=(800,N3+n1*0.5)
        
        screen.blit(img4[n1],(800,N2-n1*0.5))
    
    
    
    #Point7=Point6
    pygame.draw.lines(screen,'gold',False,[Point1,Point2,Point3,Point4],3)
    pygame.draw.lines(screen,'gold',False,[Point5,Point6,Point7,Point8],3)
    
 
    pygame.display.update()
    timer.tick(10)
pygame.quit()

