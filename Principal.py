#Programa Graficador de Robots por Ing. Lino Esteban Camacho Tapia:

#Se busca Graficar en 3D a Shoubi con el nivel de detalle máximo
#funcion de entradas: (q1,q2,q3,q4, edo Gripper):
#siempre activa y con memoria, de manera que si no se invoca deberá
#de mantener el mismo dibujo del robot en pantalla.
#Rapida y ligera de procesar
import cv2
import numpy as np
from Libreria_ShoubiV3 import*
import serial

arduinoMega = serial.Serial("COM3", 9600)
time.sleep(2) # Tiempo para el enlace de Arduino

#Barras de control para mover el robot
cv2.namedWindow('Shoubi_space')
cv2.createTrackbar('Q1','Shoubi_space',0,180,nothing) #-90 0 90
cv2.createTrackbar('Q2','Shoubi_space',0,180,nothing)
cv2.createTrackbar('Q3','Shoubi_space',0,180,nothing)
cv2.createTrackbar('Q4','Shoubi_space',0,180,nothing)
cv2.createTrackbar('On-OFF','Shoubi_space',0,1,nothing)# Se ocupa para enviar informacion al robot
cv2.createTrackbar('Print','Shoubi_space',0,1,nothing) # Imprimir en pantalla el punto en el espacio X,Y,Z

pygame.init()  #iniciamos pygame
pygame.mixer.init()  #Herramienta de audio

       #x,y
size =(800,800) #definimos Tamaño de Ventana
clock= pygame.time.Clock() #Creamos el Tiempo del videojuego
screen=pygame.display.set_mode(size)
pygame.display.set_caption("ShoubiSpace")
while True:
    for event in pygame.event.get():    #AQUI TIENE LUGAR EL Motor Gráfico
        if event.type==pygame.QUIT:     #CONDICION QUE PERMITE CERRAR EL PROGRAMA
            sys.exit()
#-------#Eventos del Teclado------------------------------------
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                inc=+0.01
            if event.key==pygame.K_RIGHT:
                inc=-0.01
            if event.key == pygame.K_UP:
                inc2=+0.01
            if event.key==pygame.K_DOWN:
                inc2=-0.01
            #AL DEJAR DE PRECIONAR
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                inc=0
            if event.key==pygame.K_RIGHT:
                inc=0
            if event.key==pygame.K_UP:
                inc2=0
            if event.key==pygame.K_DOWN:
                inc2=0
    teta+=inc; #rotaciones sobre el eje Z
    beta+=inc2; #rotacion sobre el eje X
    screen.fill(BLACK2) #Fondo del dibujo
#-------------------------------------------------
#    dibujamos los ejes de referencia
        #Puntos iniciales que definen los ejes en el espacio R3 virtual R2
    x_nega=pixel(-300,0,0,gama,teta,beta,1);x_posi=pixel(300,0,0,gama,teta,beta,1);y_nega=pixel(0,-300,0,gama,teta,beta,1)
    y_posi=pixel(0,300,0,gama,teta,beta,1);z_nega=pixel(0,0,-300,gama,teta,beta,1);z_posi=pixel(0,0,300,gama,teta,beta,1)    
                                #x,y1    x,y2
    pygame.draw.line(screen,GREEN,x_nega,x_posi) # eje horizontal X
    pygame.draw.line(screen,BLUE,y_nega,y_posi)  # eje vertical   Y  
    pygame.draw.line(screen,RED,z_nega,z_posi)  # eje vertical   Z  
#--------------Aqui estamos ya Dentro del entorno virtual creado------------------
    #obtenemos lecturas de las barras de control
    Q1 = cv2.getTrackbarPos('Q1','Shoubi_space')
    Q2 = cv2.getTrackbarPos('Q2','Shoubi_space')
    Q3 = cv2.getTrackbarPos('Q3','Shoubi_space')
    Q4= cv2.getTrackbarPos('Q4','Shoubi_space')
    Q5= cv2.getTrackbarPos('On-OFF','Shoubi_space')
    Q6= cv2.getTrackbarPos('Print','Shoubi_space')
    #Lo enviamos de ser necesario por el puerto Serial
    if Q5>0:
        valor1=da_formato(Q1-90)
        valor2=da_formato(Q2-90)
        valor3=da_formato(Q3-90)
        valor4=da_formato(Q4-90)
        clave='A'+ valor1 +'B'+ valor2 +'C'+ valor3 +'D'+ valor4 +'E+90'+'\n'
        arduinoMega.write (clave.encode())
        
        #arduino.write(b'1') #A+09B....
           
    #las convertimos a grados
    q1=(Q1-90)*pi/180
    q2=(Q2-90)*pi/180
    q3=(Q3-90)*pi/180
    q4=(Q4-90)*pi/180
    On_Off=Q5
    #dimensiones del robot
    l1=10.48
    l2=16.43
    l3=9.27
    l4=7.78
    escala=7
    #Dibujamos al robot
    eslabon_1 (screen,gama,teta,beta,escala)
    eslabon_2 (screen,gama,teta,beta,escala,q1+pi/2)
    eslabon_q2 (screen,gama,teta,beta,escala,q1,q2)
    eslabon_q3 (screen,gama,teta,beta,escala,q1,q2,q3)
    eslabon_q4 (screen,gama,teta,beta,escala,q1,q2,q3,q4)
    robot_esqueleto(screen,gama,teta,beta,escala,q1,q2+pi/2,q3,q4)
 
    
    #Evaluamos cinemática directa del robot
    if Q6>0:
        q2=q2+pi/2
        xf=(l2*math.cos(q2) +l3*math.cos(q2+q3)+l4*math.cos(q2+q3+q4)) *math.cos(q1)
        yf=(l2*math.cos(q2) +l3*math.cos(q2+q3)+l4*math.cos(q2+q3+q4)) *math.sin(q1)
        zf=l1+l2*math.sin(q2) +l3*math.sin(q2+q3)+l4*math.sin(q2+q3+q4)
        print("X= ",xf,"Y= ",yf,"Z= ",zf)
        
        
    
#------------------------------------------------------------------    
    #actualizar Pantalla
    pygame.display.flip()
    clock.tick(48)
arduinoMega.closed()
