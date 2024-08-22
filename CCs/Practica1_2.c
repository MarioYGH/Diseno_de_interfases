#include <18F4550.h>
#fuses XT,NOPROTECT,NOWDT,NOBROWNOUT,PUT,NOLVP 
#use delay(clock=4000000)

#BYTE PORTB = 0xF81

void main() {
    set_tris_b(0x00); // Configura el puerto B como salida
    PORTB = 0;        // Comienza con todos los LEDs apagados

    while(TRUE){
        // Encender los LEDs de RB0 a RB7 uno a uno
        
        for (int j = 0; j < 8; j++){
            bit_set(PORTB, j);  // Enciende el bit i del puerto B
            delay_ms(100);
            bit_clear(PORTB, j);
        
        }
        // Apagar los LEDs de RB7 a RB0 uno a uno
        for (int i = 6; i > 0; i--){
            bit_set(PORTB, i);
            delay_ms(100);
            bit_clear(PORTB, i); // Apaga el bit i del puerto B
                  
        }
    }
}
