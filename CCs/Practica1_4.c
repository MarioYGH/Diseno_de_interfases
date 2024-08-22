#include <teclado.h>
#fuses XT, NOWDT, NOWRT,PUT
#use delay(clock=20000000) 
#use fast_io(B) 
#use fast_io(D)



int delay(){
   for(int i=0; i<9; i++){
      delay_ms(10);
      if(input(pin_d5)){return 1;}
   }
}

int secuencia(){
   for(int i=1; i<128; i = i*2){
      if(delay()) { return 1; }
      output_b(i);
   }
   for(int c=128; c>1/2; c=c/2){
      if(delay()) { return 1; }
      output_b(c);
   }
   
   return 1;
}


void main()
{
   set_tris_d(0xf8); 
   set_tris_b(0x00); 

   while(TRUE)
   {  
        
      output_d(1);
      output_b( input(pin_d0)*input(pin_d3) + input(pin_d0)*input(pin_d4)*2 + input(pin_d0)*input(pin_d5)*4 );
      delay_ms(2);
      
      output_d(2);
      output_b( input(pin_d1)*input(pin_d3)*8 + input(pin_d1)*input(pin_d4)*16 + input(pin_d1)*input(pin_d5)*32  );
      delay_ms(2);
      
      output_d(4);
      output_b( input(pin_d2)*input(pin_d3)*64 + input(pin_d2)*input(pin_d4)*128 );
      if(input(pin_d5)) {
         secuencia();
      }
      delay_ms(2);
      
   }

}
