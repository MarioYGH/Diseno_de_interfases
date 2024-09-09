// Asigne un numero decimal a cada LED, por ejemplo, LED D1 número 0, LED D2 número 1, etc. Ahora, diseñe un programa en lenguaje C que lea el numero binario
// descrito por el estado de los pines RD0 a RD2 y lo convierta a base decimal. Para visualizar el resultado en base decimal encienda el LED correspondiente.

#include <18F4550.h>
#fuses XT,NOPROTECT,NOWDT,NOBROWNOUT,PUT,NOLVP 
#use delay(clock=4000000)
#use fast_io(B)
#use fast_io(D)

#byte portb = 0xF81
#byte portd = 0xF83


void main(){
set_tris_B(0x00); 
set_tris_D(0xFF); 
portb = 0;
portd = 0;
int op;

while(TRUE){ 
op = input_d();
switch(op){

case 0x00:
portb = 0;
break;

case 0x01:
portb = 0;
output_b(0x01); //UNO
break;

case 0x02:
portb = 0;
output_b(0x02); //DOS
break;

case 0x03:
portb = 0;
output_b(0x04); //TRES 
break;

case 0x04:
portb = 0;
output_b(0x08); //CUATRO 
break;

case 0x05:
portb = 0;
output_b(0x10); //CINCO
break;

case 0x06:
portb = 0;
output_b(0x20); //SEIS
break;

case 0x07:
portb = 0;
output_b(0x40); //SIETE
break;

case 0x08:
portb = 0;
output_b(0x80); //OCHO
break;


  }
 }
}
   
