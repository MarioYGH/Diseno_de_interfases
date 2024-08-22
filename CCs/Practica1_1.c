#include <18F4550.h>
#fuses XT,NOPROTECT,NOWDT,NOBROWNOUT,PUT,NOLVP 
#use delay(clock=4000000)

#BYTE PORTB = 0xF81

void main(){
   set_tris_b(0x00); 
   //set_tris_d(0x0F); 
   PORTB=0;                         //Comienza con todos los Leds Apagados
   WHILE(TRUE)                     
   {
      PORTB=(0x01);                //Prendo unicamente el led de RB0
      DELAY_MS(100);                //Delay
      WHILE (!BIT_TEST(PORTB,7))    //Haga mientras el LED RB7 se encuentre apagado
      {
         PORTB=PORTB<<1;            //Rote hacia la izquierda una unidad
         DELAY_MS(100);             
      }
      DELAY_MS(100);                
      WHILE (!BIT_TEST(PORTB,0))    //Haga mientras el LED RB0 se encuentre apagado
      {
         PORTB=PORTB>>1;            //Rote hacia la derecha una unidad
         DELAY_MS(100);             
      }
   }
}
