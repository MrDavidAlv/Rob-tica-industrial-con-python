//Programa desarrollado por Ing. Lino E. Camacho Tapia
#define DEBUG(a) Serial.println(a);
String data = "";
  #include <Servo.h>  
  Servo servo1; 
  Servo servo2; 
  Servo servo3; 
  Servo servo4; 
  Servo servo5; 
  Servo servo6; 
  
void setup() {         //Revisa el Esquemático
  Serial.begin(9600); //En este espacio configuraras el pin de cada servo segun los grados de libertad
  servo1.attach(4);   // es el equivalente a Q2-A
  servo2.attach(5);   //es el equivalente a  Q2-B
  servo3.attach(2);   //es el equivalente a  Q1
  servo4.attach(7);   //es el equivalente a  Q3
  servo5.attach(6);   //es el equivalente a  Q4
  servo6.attach(3);   //es el equivalente a  Q5
}
int tokens =1;
void loop()
{ 

    //RUTINAS PROGRAMADAS
  tokens=0;
  if(tokens==0)
  { 
   while (Serial.available())
   {
      char character = Serial.read();
      if (character != '\n')
      {
         data.concat(character);
      }
      else
      {
         //Serial.println(data);
         char a[25];
         data.toCharArray(a, 25);
         data = "";
         //Aqui comienza el algoritmo de decodificación
         if((a[0]=='A')&&(a[4]=='B')&&(a[8]=='C')&&(a[12]=='D')&&(a[16]=='E'))
          {
            char ang1[5] = {a[1],a[2],a[3]};
            int  num1= atoi(ang1);
            char ang2[5] = {a[5],a[6],a[7]};
            int  num2= atoi(ang2);
            char ang3[5] = {a[9],a[10],a[11]};
            int  num3= atoi(ang3);
            char ang4[5] = {a[13],a[14],a[15]};
            int  num4= atoi(ang4);
            char ang5[5] = {a[17],a[18],a[19]};
            int  num5= atoi(ang5);
            
            //TERMINA DECODIFICACIÓN Y COMIENZA ASIGNACION DE VALORES A LOS MOTORES
            int teta1=num1;
            int teta2=num2;
            int teta3=num3;
            int teta4=num4;
            int teta5=num5;
  
            //Calculamos cinemática Directa
            //Reacomodamos eslabones el robot
            q1(teta1);
            q2(teta2);
            q3(teta3);
            q4(teta4);
            q5(teta5);
          }


         
      }
   }
}
}
void q1(int a) //-90  0    90
{servo3.write(a+90);}
void q2(int a) //-90  0    90
{ ;
 servo1.write(a+90);
 servo2.write(abs(a+90-180));}
void q3(int a) //-90  0    90
{servo4.write(abs(-a+90-180));}
void q4(int a) //-90  0    90
{servo5.write(a+90);}
void q5(int a) //-90  0    90
{servo6.write(a+90);}
