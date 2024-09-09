// Diseñe un programa en lenguaje C que imprima dos mensajes deslizantes en un display LCD. El primer mensaje se debe visualizar en el renglón 1 del display y
// deslizarse hacia la derecha. El segundo mensaje se debe localizar en el renglón 2 del display y deslizarse hacia la izquierda.


#include <18F4550.h>
#fuses NOWDT,XT,NOPROTECT

#use delay (clock=4000000)
#include <lcd.c>

char M[] = {"Hola, somos Mario y OscarC  "}; // Variable con el mensaje que se va a desplazar
int largoMensaje = 27; // Largo del mensaje sin contar los espacios finales

void imprimir_mensaje(char *msg, int inicio, int fila) {
    int i;
    lcd_gotoxy(1, fila); 

    // Imprimimos desde 'inicio' hasta el final del mensaje
    for (i = 0; i < 16; i++) { // 16 caracteres es el ancho de una fila del LCD 16x2
        int idx = (inicio + i) % largoMensaje; // Índice circular en el mensaje
        lcd_putc(msg[idx]); // Imprimimos el carácter correspondiente
    }
}

void main() {
    lcd_init(); 

    int inicio_fila1 = 0; 
    int inicio_fila2 = largoMensaje - 1; 
    
    fila1: 
    imprimir_mensaje(M, inicio_fila1, 1); 
    delay_ms(200); 

    inicio_fila1 = (inicio_fila1 + 1) % largoMensaje; // Avanzamos al siguiente índice circularmente

    // Cuando el mensaje completo ha sido impreso en la fila 1, saltamos a la fila 2
    if (inicio_fila1 == 0) {
        lcd_putc('\f'); 
        goto fila2; 
    }

    goto fila1; 

    
    fila2: 
    imprimir_mensaje(M, inicio_fila2, 2); 
    delay_ms(200); 

    inicio_fila2 = (inicio_fila2 - 1 + largoMensaje) % largoMensaje; // Retrocedemos en el índice circularmente

    // Cuando el mensaje completo ha sido impreso en la fila 2, volvemos a la fila 1
    if (inicio_fila2 == largoMensaje - 1) {
        lcd_putc('\f'); 
        goto fila1; 
    }

    goto fila2; 
}
