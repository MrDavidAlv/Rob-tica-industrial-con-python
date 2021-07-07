import pygame, sys,random, time , math
pi=math.pi
i=-300
gama=pi/6
inc=0
inc2=0
teta=0
beta=0

#Colores
BLACK2=(56,56,56);BLACK =(0,0,0);WHITE=(255,255,255);GREEN=(0,255,0)
RED=(255,0,0);RED2=(100,150,150);BLUE=(0,0,255);YELLOW=(255,255,0);
YELLOW2=(180,180,0)


#Funcion Vacia para los TrackBar
def nothing(x):
   pass

#Funciones Trigonométricas
def cos(q):
    a=math.cos(q)
    return a
def sin(q):
    a=math.sin(q)
    return a
def da_formato(a):  #ingresa un valor en grados entre -90 y 90
    #obtenemos el signo
    signo='+'
    if a>0:
        signo='+'
    if a<0:
        signo='-'
    if a==0:
        signo='+'
    #preguntamos si se trata de decenas
    if abs(a)>9.9:
        return (signo + str(abs(a)))
    #preguntamos si se trata de solo unidades
    if abs(a)<10:
        return (signo + '0' + str(abs(a)))
    
    


                #asp ,rz , rx
def pixel(x,y,z,gama,teta,beta,escala): #funcion de ubicación en la pantalla
    x=x*escala
    y=y*escala
    z=z*escala
    #transformación RZ
    x2=(x*math.cos(teta) - y*math.sin(teta))
    y2=(y*math.cos(teta) + x*math.sin(teta))
    z2=z
    #transformacion en Rx
    x3= x2
    y3= y2*math.cos(beta) - z2*math.sin(beta)
    z3= z2*math.cos(beta) + y2*math.sin(beta)
    
    
    #print(x,y,z,"Reales")
    x_screen=int(  -x3*math.cos(gama) + y3*math.cos(gama))
    y_screen=int( -x3*math.sin(gama) -y3*math.sin(gama) +z3)
     
    x_screen=(x_screen+400)
    y_screen=(abs(y_screen-400))

    return (x_screen,y_screen)
 
def cd_eslabon2(xf,yf,zf,L1,L2,q1,q2):
    x=L2*math.cos(q1)*math.cos(q2 + pi/2) - yf*math.sin(q1) + xf*math.cos(q1)*math.cos(q2 + pi/2) - zf*math.cos(q1)*math.sin(q2 + pi/2)
    y=yf*math.cos(q1) + L2*math.cos(q2 + pi/2)*math.sin(q1) + xf*math.cos(q2 + pi/2)*math.sin(q1) - zf*math.sin(q1)*math.sin(q2 + pi/2) 
    z=L1 + L2*math.sin(q2 + pi/2) + zf*math.cos(q2 + pi/2) + xf*math.sin(q2 + pi/2)
    return (x,y,z);
def cd_eslabon3(tx,ty,tz,L1,L2,L3,q1,q2,q3):
    x=L2*math.cos(q1)*math.cos(q2 + pi/2) - tx*(math.cos(q1)*math.sin(q3)*math.sin(q2 + pi/2) - math.cos(q1)*math.cos(q3)*math.cos(q2 + pi/2)) - tz*(math.cos(q1)*math.cos(q3)*math.sin(q2 + pi/2) + math.cos(q1)*math.cos(q2 + pi/2)*math.sin(q3)) - ty*math.sin(q1) - L3*(math.cos(q1)*math.sin(q3)*math.sin(q2 + pi/2) - math.cos(q1)*math.cos(q3)*math.cos(q2 + pi/2))
    y=ty*math.cos(q1) - tx*(math.sin(q1)*math.sin(q3)*math.sin(q2 + pi/2) - math.cos(q3)*math.cos(q2 + pi/2)*math.sin(q1)) - tz*(math.cos(q3)*math.sin(q1)*math.sin(q2 + pi/2) + math.cos(q2 + pi/2)*math.sin(q1)*math.sin(q3)) - L3*(math.sin(q1)*math.sin(q3)*math.sin(q2 + pi/2) - math.cos(q3)*math.cos(q2 + pi/2)*math.sin(q1)) + L2*math.cos(q2 + pi/2)*math.sin(q1)
    z=L1 + L3*(math.cos(q3)*math.sin(q2 + pi/2) + math.cos(q2 + pi/2)*math.sin(q3)) + tx*(math.cos(q3)*math.sin(q2 + pi/2) + math.cos(q2 + pi/2)*math.sin(q3)) + tz*(math.cos(q3)*math.cos(q2 + pi/2) - math.sin(q3)*math.sin(q2 + pi/2)) + L2*math.sin(q2 + pi/2)
    return (x,y,z)
def cd_eslabon4(tx,ty,tz,L1,L2,L3,L4,q1,q2,q3,q4):
    x=L2*cos(q1)*cos(q2 + pi/2) - L4*(cos(q4)*(cos(q1)*sin(q3)*sin(q2 + pi/2) - cos(q1)*cos(q3)*cos(q2 + pi/2)) + sin(q4)*(cos(q1)*cos(q3)*sin(q2 + pi/2) + cos(q1)*cos(q2 + pi/2)*sin(q3))) - tx*(cos(q4)*(cos(q1)*sin(q3)*sin(q2 + pi/2) - cos(q1)*cos(q3)*cos(q2 + pi/2)) + sin(q4)*(cos(q1)*cos(q3)*sin(q2 + pi/2) + cos(q1)*cos(q2 + pi/2)*sin(q3))) - tz*(cos(q4)*(cos(q1)*cos(q3)*sin(q2 + pi/2) + cos(q1)*cos(q2 + pi/2)*sin(q3)) - sin(q4)*(cos(q1)*sin(q3)*sin(q2 + pi/2) - cos(q1)*cos(q3)*cos(q2 + pi/2))) - ty*sin(q1) - L3*(cos(q1)*sin(q3)*sin(q2 + pi/2) - cos(q1)*cos(q3)*cos(q2 + pi/2))
    y=ty*cos(q1) - L4*(cos(q4)*(sin(q1)*sin(q3)*sin(q2 + pi/2) - cos(q3)*cos(q2 + pi/2)*sin(q1)) + sin(q4)*(cos(q3)*sin(q1)*sin(q2 + pi/2) + cos(q2 + pi/2)*sin(q1)*sin(q3))) - tx*(cos(q4)*(sin(q1)*sin(q3)*sin(q2 + pi/2) - cos(q3)*cos(q2 + pi/2)*sin(q1)) + sin(q4)*(cos(q3)*sin(q1)*sin(q2 + pi/2) + cos(q2 + pi/2)*sin(q1)*sin(q3))) - tz*(cos(q4)*(cos(q3)*sin(q1)*sin(q2 + pi/2) + cos(q2 + pi/2)*sin(q1)*sin(q3)) - sin(q4)*(sin(q1)*sin(q3)*sin(q2 + pi/2) - cos(q3)*cos(q2 + pi/2)*sin(q1))) - L3*(sin(q1)*sin(q3)*sin(q2 + pi/2) - cos(q3)*cos(q2 + pi/2)*sin(q1)) + L2*cos(q2 + pi/2)*sin(q1)
    z=L1 + tx*(cos(q4)*(cos(q3)*sin(q2 + pi/2) + cos(q2 + pi/2)*sin(q3)) + sin(q4)*(cos(q3)*cos(q2 + pi/2) - sin(q3)*sin(q2 + pi/2))) + tz*(cos(q4)*(cos(q3)*cos(q2 + pi/2) - sin(q3)*sin(q2 + pi/2)) - sin(q4)*(cos(q3)*sin(q2 + pi/2) + cos(q2 + pi/2)*sin(q3))) + L3*(cos(q3)*sin(q2 + pi/2) + cos(q2 + pi/2)*sin(q3)) + L2*sin(q2 + pi/2) + L4*(cos(q4)*(cos(q3)*sin(q2 + pi/2) + cos(q2 + pi/2)*sin(q3)) + sin(q4)*(cos(q3)*cos(q2 + pi/2) - sin(q3)*sin(q2 + pi/2)))
    return (x,y,z)

 

def cd_2 (q1,q2,l1,l2):
    x=l2*math.cos(q2)*math.cos(q1)
    y=l2*math.cos(q2)*math.sin(q1)
    z=l1+l2*math.sin(q2)
    return (x,y,z)
def cd_3 (q1,q2,q3,l1,l2,l3):
    x=(l2*math.cos(q2) +l3*math.cos(q2+q3)) *math.cos(q1)
    y=(l2*math.cos(q2) +l3*math.cos(q2+q3)) *math.sin(q1)
    z=l1+l2*math.sin(q2) +l3*math.sin(q2+q3)
    return (x,y,z)
def cd_4 (q1,q2,q3,q4,l1,l2,l3,l4):
    x=(l2*math.cos(q2) +l3*math.cos(q2+q3)+l4*math.cos(q2+q3+q4)) *math.cos(q1)
    y=(l2*math.cos(q2) +l3*math.cos(q2+q3)+l4*math.cos(q2+q3+q4)) *math.sin(q1)
    z=l1+l2*math.sin(q2) +l3*math.sin(q2+q3)+l4*math.sin(q2+q3+q4)
    return (x,y,z)
#librería Shoubi V3
def robot_esqueleto(screen,gama,teta,beta,escala,q1,q2,q3,q4):
    #Longitud de los eslabones
    l1=10.48
    l2=16.43
    l3=9.27
    l4=7.78
    #Puntos de control
    A=(0,0,0)
    B=(0,0,l1)
    C=cd_2(q1,q2,l1,l2)
    D=cd_3(q1,q2,q3,l1,l2,l3)
    E=cd_4(q1,q2,q3,q4,l1,l2,l3,l4)
    #Convertimos R3 a R2 Virtual
    A2=pixel(A[0],A[1],A[2],gama,teta,beta,escala)
    B2=pixel(B[0],B[1],B[2],gama,teta,beta,escala)
    C2=pixel(C[0],C[1],C[2],gama,teta,beta,escala)
    D2=pixel(D[0],D[1],D[2],gama,teta,beta,escala)
    E2=pixel(E[0],E[1],E[2],gama,teta,beta,escala)
    #los dibujamos y luego los unimos
    pygame.draw.circle(screen, RED2, (A2) , 3)
    pygame.draw.circle(screen, RED2, (B2) , 3)
    pygame.draw.circle(screen, RED2, (C2) , 3)
    pygame.draw.circle(screen, RED2, (D2) , 3)
    pygame.draw.circle(screen, RED2, (E2) , 3)
    
    pygame.draw.line(screen,RED2,A2,B2)
    pygame.draw.line(screen,RED2,B2,C2)
    pygame.draw.line(screen,RED2,C2,D2)
    pygame.draw.line(screen,RED2,D2,E2)
def eslabon_1 (screen,gama,teta,beta,escala):
    A=pixel(5.3,0,0,gama,teta,beta,escala)
    B=pixel(5.3*math.cos(pi/8),5.3*math.sin(pi/8),0,gama,teta,beta,escala)
    C=pixel(5.3*math.cos(2*pi/8),5.3*math.sin(2*pi/8),0,gama,teta,beta,escala)
    D=pixel(5.3*math.cos(3*pi/8),5.3*math.sin(3*pi/8),0,gama,teta,beta,escala)
    E=pixel(5.3*math.cos(4*pi/8),5.3*math.sin(4*pi/8),0,gama,teta,beta,escala)
    F=pixel(5.3*math.cos(5*pi/8),5.3*math.sin(5*pi/8),0,gama,teta,beta,escala)
    G=pixel(5.3*math.cos(6*pi/8),5.3*math.sin(6*pi/8),0,gama,teta,beta,escala)
    H=pixel(5.3*math.cos(7*pi/8),5.3*math.sin(7*pi/8),0,gama,teta,beta,escala)
    I=pixel(5.3*math.cos(8*pi/8),5.3*math.sin(8*pi/8),0,gama,teta,beta,escala)
    J=pixel(5.3*math.cos(9*pi/8),5.3*math.sin(9*pi/8),0,gama,teta,beta,escala)
    K=pixel(5.3*math.cos(10*pi/8),5.3*math.sin(10*pi/8),0,gama,teta,beta,escala)
    L=pixel(5.3*math.cos(11*pi/8),5.3*math.sin(11*pi/8),0,gama,teta,beta,escala)
    M=pixel(5.3*math.cos(12*pi/8),5.3*math.sin(12*pi/8),0,gama,teta,beta,escala)
    N=pixel(5.3*math.cos(13*pi/8),5.3*math.sin(13*pi/8),0,gama,teta,beta,escala)
    O=pixel(5.3*math.cos(14*pi/8),5.3*math.sin(14*pi/8),0,gama,teta,beta,escala)
    P=pixel(5.3*math.cos(15*pi/8),5.3*math.sin(15*pi/8),0,gama,teta,beta,escala)
    AZ=pixel(5.3,0,5.7,gama,teta,beta,escala)
    BZ=pixel(5.3*math.cos(pi/8),5.3*math.sin(pi/8),5.7,gama,teta,beta,escala)
    CZ=pixel(5.3*math.cos(2*pi/8),5.3*math.sin(2*pi/8),5.7,gama,teta,beta,escala)
    DZ=pixel(5.3*math.cos(3*pi/8),5.3*math.sin(3*pi/8),5.7,gama,teta,beta,escala)
    EZ=pixel(5.3*math.cos(4*pi/8),5.3*math.sin(4*pi/8),5.7,gama,teta,beta,escala)
    FZ=pixel(5.3*math.cos(5*pi/8),5.3*math.sin(5*pi/8),5.7,gama,teta,beta,escala)
    GZ=pixel(5.3*math.cos(6*pi/8),5.3*math.sin(6*pi/8),5.7,gama,teta,beta,escala)
    HZ=pixel(5.3*math.cos(7*pi/8),5.3*math.sin(7*pi/8),5.7,gama,teta,beta,escala)
    IZ=pixel(5.3*math.cos(8*pi/8),5.3*math.sin(8*pi/8),5.7,gama,teta,beta,escala)
    JZ=pixel(5.3*math.cos(9*pi/8),5.3*math.sin(9*pi/8),5.7,gama,teta,beta,escala)
    KZ=pixel(5.3*math.cos(10*pi/8),5.3*math.sin(10*pi/8),5.7,gama,teta,beta,escala)
    LZ=pixel(5.3*math.cos(11*pi/8),5.3*math.sin(11*pi/8),5.7,gama,teta,beta,escala)
    MZ=pixel(5.3*math.cos(12*pi/8),5.3*math.sin(12*pi/8),5.7,gama,teta,beta,escala)
    NZ=pixel(5.3*math.cos(13*pi/8),5.3*math.sin(13*pi/8),5.7,gama,teta,beta,escala)
    OZ=pixel(5.3*math.cos(14*pi/8),5.3*math.sin(14*pi/8),5.7,gama,teta,beta,escala)
    PZ=pixel(5.3*math.cos(15*pi/8),5.3*math.sin(15*pi/8),5.7,gama,teta,beta,escala)
    
    #CARAS LATERALES
    pygame.draw.polygon(screen,YELLOW,(A,B,BZ,AZ))
    pygame.draw.polygon(screen,YELLOW,(B,C,CZ,BZ))
    pygame.draw.polygon(screen,YELLOW2,(C,D,DZ,CZ))
    pygame.draw.polygon(screen,YELLOW2,(D,E,EZ,DZ))

    pygame.draw.polygon(screen,YELLOW,(E,F,FZ,EZ))
    pygame.draw.polygon(screen,YELLOW,(F,G,GZ,FZ))
    pygame.draw.polygon(screen,YELLOW2,(G,H,HZ,GZ))
    pygame.draw.polygon(screen,YELLOW2,(H,I,IZ,HZ))

    pygame.draw.polygon(screen,YELLOW,(I,J,JZ,IZ))
    pygame.draw.polygon(screen,YELLOW,(J,K,KZ,JZ))
    pygame.draw.polygon(screen,YELLOW2,(K,L,LZ,KZ))
    pygame.draw.polygon(screen,YELLOW2,(L,M,MZ,LZ))

    pygame.draw.polygon(screen,YELLOW,(M,N,NZ,MZ))
    pygame.draw.polygon(screen,YELLOW2,(N,O,OZ,NZ))
    pygame.draw.polygon(screen,YELLOW,(O,P,PZ,OZ))
    #CARAS SUPERIORES
    pygame.draw.polygon(screen,YELLOW,(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P),0)
    pygame.draw.polygon(screen,YELLOW,(AZ,BZ,CZ,DZ,EZ,FZ,GZ,HZ,IZ,JZ,KZ,LZ,MZ,NZ,OZ,PZ),0)
    pygame.draw.polygon(screen,BLACK,(AZ,BZ,CZ,DZ,EZ,FZ,GZ,HZ,IZ,JZ,KZ,LZ,MZ,NZ,OZ,PZ),1)
    
    return 0;
def eslabon_2 (screen,gama,teta,beta,escala,q1):
    #definimos puntos en el espacio
    A= (-1.3,-1.3,5.7)
    B= (1.3 ,-1.3,5.7)
    C= (1.3 ,1.3 ,5.7)
    D= (-1.3,1.3 ,5.7)
 
    AZ= (-1.3,-1.3,11.9)
    BZ= (1.3 ,-1.3,11.9)
    CZ= (1.3 ,1.3 ,11.9)
    DZ= (-1.3,1.3 ,11.9)
    
    E=(-3*1.3,-1.3,9)
    F=(3*1.3 ,-1.3,9)
    G=(3*1.3 ,1.3 ,9)
    H=(-3*1.3,1.3 ,9)
    
    EZ=(-3*1.3,-1.3,11.9)
    FZ=(3*1.3 ,-1.3,11.9)
    GZ=(3*1.3 ,1.3 ,11.9)
    HZ=(-3*1.3,1.3 ,11.9)
    
    
    
    #Los Rotamos en RZ(q1)
    A=(A[0]*math.cos(q1) - A[1]*math.sin(q1),A[1]*math.cos(q1) + A[0]*math.sin(q1),A[2])
    B=(B[0]*math.cos(q1) - B[1]*math.sin(q1),B[1]*math.cos(q1) + B[0]*math.sin(q1),B[2])
    C=(C[0]*math.cos(q1) - C[1]*math.sin(q1),C[1]*math.cos(q1) + C[0]*math.sin(q1),C[2])
    D=(D[0]*math.cos(q1) - D[1]*math.sin(q1),D[1]*math.cos(q1) + D[0]*math.sin(q1),D[2])
    E=(E[0]*math.cos(q1) - E[1]*math.sin(q1),E[1]*math.cos(q1) + E[0]*math.sin(q1),E[2])
    F=(F[0]*math.cos(q1) - F[1]*math.sin(q1),F[1]*math.cos(q1) + F[0]*math.sin(q1),F[2])
    G=(G[0]*math.cos(q1) - G[1]*math.sin(q1),G[1]*math.cos(q1) + G[0]*math.sin(q1),G[2])
    H=(H[0]*math.cos(q1) - H[1]*math.sin(q1),H[1]*math.cos(q1) + H[0]*math.sin(q1),H[2])
    
    
    
    
    AZ=(AZ[0]*math.cos(q1) - AZ[1]*math.sin(q1),AZ[1]*math.cos(q1) + AZ[0]*math.sin(q1),AZ[2])
    BZ=(BZ[0]*math.cos(q1) - BZ[1]*math.sin(q1),BZ[1]*math.cos(q1) + BZ[0]*math.sin(q1),BZ[2])
    CZ=(CZ[0]*math.cos(q1) - CZ[1]*math.sin(q1),CZ[1]*math.cos(q1) + CZ[0]*math.sin(q1),CZ[2])
    DZ=(DZ[0]*math.cos(q1) - DZ[1]*math.sin(q1),DZ[1]*math.cos(q1) + DZ[0]*math.sin(q1),DZ[2])
    EZ=(EZ[0]*math.cos(q1) - EZ[1]*math.sin(q1),EZ[1]*math.cos(q1) + EZ[0]*math.sin(q1),EZ[2])
    FZ=(FZ[0]*math.cos(q1) - FZ[1]*math.sin(q1),FZ[1]*math.cos(q1) + FZ[0]*math.sin(q1),FZ[2])
    GZ=(GZ[0]*math.cos(q1) - GZ[1]*math.sin(q1),GZ[1]*math.cos(q1) + GZ[0]*math.sin(q1),GZ[2])
    HZ=(HZ[0]*math.cos(q1) - HZ[1]*math.sin(q1),HZ[1]*math.cos(q1) + HZ[0]*math.sin(q1),HZ[2])
    
    
    #Los convertimos a representación en R2
    A2= pixel(A[0],A[1],A[2],gama,teta,beta,escala)
    B2= pixel(B[0],B[1],B[2],gama,teta,beta,escala)
    C2= pixel(C[0],C[1],C[2],gama,teta,beta,escala)
    D2= pixel(D[0],D[1],D[2],gama,teta,beta,escala)
    E2= pixel(E[0],E[1],E[2],gama,teta,beta,escala)
    F2= pixel(F[0],F[1],F[2],gama,teta,beta,escala)
    G2= pixel(G[0],G[1],G[2],gama,teta,beta,escala)
    H2= pixel(H[0],H[1],H[2],gama,teta,beta,escala)
    
    AZ2= pixel(AZ[0],AZ[1],AZ[2],gama,teta,beta,escala)
    BZ2= pixel(BZ[0],BZ[1],BZ[2],gama,teta,beta,escala)
    CZ2= pixel(CZ[0],CZ[1],CZ[2],gama,teta,beta,escala)
    DZ2= pixel(DZ[0],DZ[1],DZ[2],gama,teta,beta,escala)
    EZ2= pixel(EZ[0],EZ[1],EZ[2],gama,teta,beta,escala)
    FZ2= pixel(FZ[0],FZ[1],FZ[2],gama,teta,beta,escala)
    GZ2= pixel(GZ[0],GZ[1],GZ[2],gama,teta,beta,escala)
    HZ2= pixel(HZ[0],HZ[1],HZ[2],gama,teta,beta,escala)
    
    #Dibujamos
    pygame.draw.polygon(screen,BLACK,(A2,B2,C2,D2)) 
    pygame.draw.polygon(screen,BLACK,(AZ2,BZ2,CZ2,DZ2))
    pygame.draw.polygon(screen,BLACK,(A2,B2,BZ2,AZ2))
    pygame.draw.polygon(screen,BLACK,(C2,D2,DZ2,CZ2))
    pygame.draw.polygon(screen,BLACK,(A2,D2,DZ2,AZ2))
    pygame.draw.polygon(screen,BLACK,(B2,C2,CZ2,BZ2))
    
    
    pygame.draw.polygon(screen,BLACK,(E2,F2,G2,H2))
    pygame.draw.polygon(screen,BLACK,(EZ2,FZ2,GZ2,HZ2))
    pygame.draw.polygon(screen,BLACK,(E2,F2,FZ2,EZ2))
    pygame.draw.polygon(screen,BLACK,(H2,G2,GZ2,HZ2))
    
    
        
    #x2=(x*math.cos(teta) - y*math.sin(teta))
    #y2=(y*math.cos(teta) + x*math.sin(teta))
    #z2=z
    
    
    return 0;
def eslabon_q2 (screen,gama,teta,beta,escala,q1,q2):
    L1=10.48
    L2=16.43
    L3=9.27
    L4=7.78
    #Puntos en el espacio que dibujan el brazo
    A=cd_eslabon2(0,1,1,L1,L2,q1,q2)   #BASTAGO
    B=cd_eslabon2(0,-1,1,L1,L2,q1,q2)
    C=cd_eslabon2(0,-1,-1,L1,L2,q1,q2)
    D=cd_eslabon2(0,1,-1,L1,L2,q1,q2)
    
    AX=cd_eslabon2(-15,1,1,L1,L2,q1,q2)   #FIN 
    BX=cd_eslabon2(-15,-1,1,L1,L2,q1,q2)
    CX=cd_eslabon2(-15,-1,-1,L1,L2,q1,q2)
    DX=cd_eslabon2(-15,1,-1,L1,L2,q1,q2)
    
    #convertimos los puntos a R2
    A2= pixel(A[0],A[1],A[2],gama,teta,beta,escala)
    B2= pixel(B[0],B[1],B[2],gama,teta,beta,escala)
    C2= pixel(C[0],C[1],C[2],gama,teta,beta,escala)
    D2= pixel(D[0],D[1],D[2],gama,teta,beta,escala)
    
    A2X= pixel(AX[0],AX[1],AX[2],gama,teta,beta,escala)
    B2X= pixel(BX[0],BX[1],BX[2],gama,teta,beta,escala)
    C2X= pixel(CX[0],CX[1],CX[2],gama,teta,beta,escala)
    D2X= pixel(DX[0],DX[1],DX[2],gama,teta,beta,escala)
    
    #los dibujamos
    #pygame.draw.circle(screen, RED2, (A2) , 3)
    #pygame.draw.circle(screen, RED2, (B2) , 3)
    #pygame.draw.circle(screen, BLUE, (C2) , 3)
    #pygame.draw.circle(screen, BLUE, (D2) , 3)

    #pygame.draw.circle(screen, RED2, (A2X) , 3)
    #pygame.draw.circle(screen, RED2, (B2X) , 3)
    #pygame.draw.circle(screen, BLUE, (C2X) , 3)
    #pygame.draw.circle(screen, BLUE, (D2X) , 3)
    
    #dibujamos poligonos
    pygame.draw.polygon(screen,YELLOW,(A2,B2,C2,D2))
    pygame.draw.polygon(screen,YELLOW,(A2X,B2X,C2X,D2X))
    
    pygame.draw.polygon(screen,YELLOW2,(A2,B2,B2X,A2X))
    pygame.draw.polygon(screen,YELLOW2,(B2,C2,C2X,B2X))
    
    pygame.draw.polygon(screen,YELLOW2,(C2,D2,D2X,C2X))
    pygame.draw.polygon(screen,YELLOW,(D2,A2,A2X,D2X))
    #DIBUJAMOS UNION ESFÉRICA
    O=pixel(0,0,L1,gama,teta,beta,escala)
    pygame.draw.circle(screen, BLACK, (O) , 16)
    #DIBUJAMOS UNION ESFÉRICA FINAL
    #p=cd_eslabon2(0,0,0,L1,L2,q1,q2)
    #P=pixel(p[0],p[1],p[2],gama,teta,beta,escala)
    #pygame.draw.circle(screen, BLACK, (P) , 16)
    
def eslabon_q3 (screen,gama,teta,beta,escala,q1,q2,q3):
    L1=10.48
    L2=16.43
    L3=9.27
    L4=7.78
    #Puntos en el espacio que dibujan el brazo
    A=cd_eslabon3(0,1,1,L1,L2,L3,q1,q2,q3)   #BASTAGO
    B=cd_eslabon3(0,-1,1,L1,L2,L3,q1,q2,q3)
    C=cd_eslabon3(0,-1,-1,L1,L2,L3,q1,q2,q3)
    D=cd_eslabon3(0,1,-1,L1,L2,L3,q1,q2,q3)
    
    O=cd_eslabon3(0,0,0,L1,L2,L3,q1,q2,q3)
    P=cd_eslabon3(-9.27,0,0,L1,L2,L3,q1,q2,q3)
    
    AX=cd_eslabon3(-9,1,1,L1,L2,L3,q1,q2,q3)   #FIN 
    BX=cd_eslabon3(-9,-1,1,L1,L2,L3,q1,q2,q3)
    CX=cd_eslabon3(-9,-1,-1,L1,L2,L3,q1,q2,q3)
    DX=cd_eslabon3(-9,1,-1,L1,L2,L3,q1,q2,q3)
    
    #convertimos los puntos a R2
    A2= pixel(A[0],A[1],A[2],gama,teta,beta,escala)
    B2= pixel(B[0],B[1],B[2],gama,teta,beta,escala)
    C2= pixel(C[0],C[1],C[2],gama,teta,beta,escala)
    D2= pixel(D[0],D[1],D[2],gama,teta,beta,escala)
    
    O2= pixel(O[0],O[1],O[2],gama,teta,beta,escala)
    P2= pixel(P[0],P[1],P[2],gama,teta,beta,escala)
    
    A2X= pixel(AX[0],AX[1],AX[2],gama,teta,beta,escala)
    B2X= pixel(BX[0],BX[1],BX[2],gama,teta,beta,escala)
    C2X= pixel(CX[0],CX[1],CX[2],gama,teta,beta,escala)
    D2X= pixel(DX[0],DX[1],DX[2],gama,teta,beta,escala)
    
    #los dibujamos
    #pygame.draw.circle(screen, RED2, (A2) , 3)
    #pygame.draw.circle(screen, RED2, (B2) , 3)
    #pygame.draw.circle(screen, BLUE, (C2) , 3)
    #pygame.draw.circle(screen, BLUE, (D2) , 3)

    #pygame.draw.circle(screen, RED2, (A2X) , 3)
    #pygame.draw.circle(screen, RED2, (B2X) , 3)
    #pygame.draw.circle(screen, BLUE, (C2X) , 3)
    #pygame.draw.circle(screen, BLUE, (D2X) , 3)
    
    #dibujamos poligonos
    pygame.draw.polygon(screen,YELLOW,(A2,B2,C2,D2))
    pygame.draw.polygon(screen,YELLOW,(A2X,B2X,C2X,D2X))
    
    pygame.draw.polygon(screen,YELLOW2,(A2,B2,B2X,A2X))
    pygame.draw.polygon(screen,YELLOW2,(B2,C2,C2X,B2X))
    
    pygame.draw.polygon(screen,YELLOW2,(C2,D2,D2X,C2X))
    pygame.draw.polygon(screen,YELLOW,(D2,A2,A2X,D2X))
    #DIBUJAMOS UNION ESFÉRICA
    pygame.draw.circle(screen, BLACK, (O2) , 10)
    #DIBUJAMOS UNION ESFÉRICA FINAL
    pygame.draw.circle(screen, BLACK, (P2) , 12)
    
def eslabon_q4 (screen,gama,teta,beta,escala,q1,q2,q3,q4):
    L1=10.48
    L2=16.43
    L3=9.27
    L4=7.78
    
    #Gripper
    E=cd_eslabon4(0,3,.7,L1,L2,L3,L4,q1,q2,q3,q4)   #BASTAGO
    F=cd_eslabon4(0,-3,.7,L1,L2,L3,L4,q1,q2,q3,q4)
    G=cd_eslabon4(0,-3,-.7,L1,L2,L3,L4,q1,q2,q3,q4)
    H=cd_eslabon4(0,3,-.7,L1,L2,L3,L4,q1,q2,q3,q4)
    
    I=cd_eslabon4(3,-3,-.7,L1,L2,L3,L4,q1,q2,q3,q4)
    J=cd_eslabon4(3,3,-.7,L1,L2,L3,L4,q1,q2,q3,q4)
    
    
    
    #Puntos en el espacio que dibujan el brazo
    A=cd_eslabon4(0,.7,.7,L1,L2,L3,L4,q1,q2,q3,q4)   #BASTAGO
    B=cd_eslabon4(0,-.7,.7,L1,L2,L3,L4,q1,q2,q3,q4)
    C=cd_eslabon4(0,-.7,-.7,L1,L2,L3,L4,q1,q2,q3,q4)
    D=cd_eslabon4(0,.7,-.7,L1,L2,L3,L4,q1,q2,q3,q4)
    
    O=cd_eslabon4(0,0,0,L1,L2,L3,L4,q1,q2,q3,q4)
    P=cd_eslabon4(-7.78,0,0,L1,L2,L4,L3,q1,q2,q3,q4)
    
    AX=cd_eslabon4(-7.78,.7,.7,L1,L2,L3,L4,q1,q2,q3,q4)   #FIN 
    BX=cd_eslabon4(-7.78,-.7,.7,L1,L2,L3,L4,q1,q2,q3,q4)
    CX=cd_eslabon4(-7.78,-.7,-.7,L1,L2,L3,L4,q1,q2,q3,q4)
    DX=cd_eslabon4(-7.78,.7,-.7,L1,L2,L3,L4,q1,q2,q3,q4)
    
    #convertimos los puntos a R2
    A2= pixel(A[0],A[1],A[2],gama,teta,beta,escala)
    B2= pixel(B[0],B[1],B[2],gama,teta,beta,escala)
    C2= pixel(C[0],C[1],C[2],gama,teta,beta,escala)
    D2= pixel(D[0],D[1],D[2],gama,teta,beta,escala)
    
    E2= pixel(E[0],E[1],E[2],gama,teta,beta,escala)
    F2= pixel(F[0],F[1],F[2],gama,teta,beta,escala)
    G2= pixel(G[0],G[1],G[2],gama,teta,beta,escala)
    H2= pixel(H[0],H[1],H[2],gama,teta,beta,escala)
    
    I2= pixel(I[0],I[1],I[2],gama,teta,beta,escala)
    J2= pixel(J[0],J[1],J[2],gama,teta,beta,escala)
    
    
    O2= pixel(O[0],O[1],O[2],gama,teta,beta,escala)
    P2= pixel(P[0],P[1],P[2],gama,teta,beta,escala)
    
    A2X= pixel(AX[0],AX[1],AX[2],gama,teta,beta,escala)
    B2X= pixel(BX[0],BX[1],BX[2],gama,teta,beta,escala)
    C2X= pixel(CX[0],CX[1],CX[2],gama,teta,beta,escala)
    D2X= pixel(DX[0],DX[1],DX[2],gama,teta,beta,escala)
    
    #los dibujamos
    #pygame.draw.circle(screen, RED2, (A2) , 3)
    #pygame.draw.circle(screen, RED2, (B2) , 3)
    #pygame.draw.circle(screen, BLUE, (C2) , 3)
    #pygame.draw.circle(screen, BLUE, (D2) , 3)

    #pygame.draw.circle(screen, RED2, (A2X) , 3)
    #pygame.draw.circle(screen, RED2, (H2) , 3)
    #pygame.draw.circle(screen, BLUE, (J2) , 3)
    #pygame.draw.circle(screen, BLUE, (E2) , 3)
    
    #dibujamos poligonos
    pygame.draw.polygon(screen,YELLOW,(A2,B2,C2,D2))
    pygame.draw.polygon(screen,YELLOW,(A2X,B2X,C2X,D2X))
    
    pygame.draw.polygon(screen,YELLOW2,(A2,B2,B2X,A2X))
    pygame.draw.polygon(screen,YELLOW2,(B2,C2,C2X,B2X))
    
    pygame.draw.polygon(screen,YELLOW2,(C2,D2,D2X,C2X))
    pygame.draw.polygon(screen,YELLOW,(D2,A2,A2X,D2X))
    
    #DIBUJAMOS UNION ESFÉRICA
    pygame.draw.circle(screen, BLACK, (O2) , 10)
    #DIBUJAMOS UNION ESFÉRICA FINAL
   # pygame.draw.circle(screen, BLACK, (P2) , 12)
    
    pygame.draw.polygon(screen,RED,(E2,F2,G2,H2))
    pygame.draw.polygon(screen,RED2,(H2,J2,E2))
    pygame.draw.polygon(screen,RED2,(F2,G2,I2))
    
