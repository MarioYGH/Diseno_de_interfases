// Diseñe un programa en lenguaje C que implemente un frecuenciometro de 1 a 200 Hz para señales cuadradas con amplitud de 5V y offset 0. El valor de la frecuencia se debe
// visualizar en un display LCD. Cuando la frecuencia de la señal cuadrada sea mayor que 100 Hz, el LED D1 debe encender.

#include <18F4550.h>
#fuses XT,NOWDT,NOPROTECT,NOLVP
#use delay (clock = 4000000)
#include <lcd.c>
#use fast_io(B)

float t = 0.0;
float f = 0.0;
float f_inv = 0.0;
float vueltas = 0.0;

#int_timer1
void reset_timer(){
   set_timer1(0); //Resetea el timer1 max al segundo
   vueltas = vueltas + 1.0;
   }
#int_ext
void ext(){  
      t = (4.0/4000000.0)*8.0*get_timer1() + vueltas*0.5;
      if(t>0) {f_inv = t;} // obtiene el tiempo de pico a pico
      else{f_inv = 0.0;}
      set_timer1(0); // reinicia el contador
      vueltas = 0.0;
      }

void main(){  
   set_tris_b(0x01);
   setup_timer_1(T1_INTERNAL | T1_DIV_BY_8);  // Configura Timer1 con prescaler de 1:256
   set_timer1(0);                              // Inicializa Timer1 en 0
   enable_interrupts(int_timer1);             // Habilita la interrupción del Timer1
   enable_interrupts(int_ext);
   ext_int_edge(L_TO_H);
   enable_interrupts(GLOBAL); 
   lcd_init();
   while(TRUE){
      f = 1/f_inv;
      f = f/4.0;
      printf(lcd_putc, "\fFreq: %f", f );
      if(f >= 100.0){ output_bit(pin_b7, 1); }
      else {output_bit(pin_b7, 0);}
      delay_ms(30);   
   }
}
