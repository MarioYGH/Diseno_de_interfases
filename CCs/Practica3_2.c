// Diseñe un programa en lenguaje C que permita controlar el tiempo en estado alto de una señal cuadrada con frecuencia 1 Hz, generada en el PIN A0. Cada botón
// del teclado será designado para establecer un múltiplo de la duración base (100 ms) en estado alto. De manera que, el botón 1 generará una señal cuadrada con
// 100 ms en estado alto y 900 ms en estado bajo; el botón 2: 200 ms en estado alto y 800 ms en estado bajo; el botón 3: 300 ms en estado alto y 700 ms en estado bajo.
// Este procedimiento será aplicado de la misma manera para los 9 botones. En eldisplay LCD se debe visualizar la selección que el usuario estableció a través del teclado. Las señales generadas se verificarán con un osciloscopio.

#include <18F4550.h>
#fuses XT,NOWDT,NOPROTECT,NOLVP
#use delay(clock=4000000)
#include <lcd.c>
#use fast_io(B)

float k = 0.0;
int q = 30;

float teclado() {
    output_b(6);
    k = !input(pin_b0) * !input(pin_b3) * 0.1 + !input(pin_b0) * !input(pin_b4) * 0.2 + !input(pin_b0) * !input(pin_b5) * 0.3;
    if (k != 0.0) { return k; }
    delay_ms(q);

    output_b(5);
    k = !input(pin_b1) * !input(pin_b3) * 0.4 + !input(pin_b1) * !input(pin_b4) * 0.5 + !input(pin_b1) * !input(pin_b5) * 0.6;
    if (k != 0.0) { return k; }
    delay_ms(q);

    output_b(3);
    k = !input(pin_b2) * !input(pin_b3) * 0.7 + !input(pin_b2) * !input(pin_b4) * 0.8 + !input(pin_b2) * !input(pin_b5) * 0.9;
    if (k != 0.0) { return k; }
    delay_ms(q);

    return 0.0;
}

void generar_pwm_manual(float duty_cycle) {
    int tiempo_alto = duty_cycle * 1000;  // Tiempo en estado alto en ms
    int tiempo_bajo = 1000 - tiempo_alto; // Tiempo en estado bajo en ms
    
    // Generar la señal cuadrada con la duración en estado alto y bajo
    output_high(PIN_A0);  // Pon A0 en alto
    delay_ms(tiempo_alto); // Mantén el pin A0 en alto por "tiempo_alto"
    
    output_low(PIN_A0);   // Pon A0 en bajo
    delay_ms(tiempo_bajo); // Mantén el pin A0 en bajo por "tiempo_bajo"
}

void main() {
    // Configuración de los pines
    set_tris_b(0x38);  // Configura PORTB como entrada
    set_tris_a(0xFE);  // Configura PINA0 como salida
    lcd_init();
    port_b_pullups(TRUE);

    float j = 0.0;
    float i = 0.0;

    while(TRUE) {
        printf(lcd_putc, "\f p n alto: %f", 0.0);
        
        j = teclado();  // Lee la selección del teclado
        
        if (j != 0.0) {
            // Muestra el porcentaje en estado alto
            printf(lcd_putc, "\f p n alto: %f", j);
            
            while (TRUE) {
                generar_pwm_manual(j);  // Genera la señal PWM manualmente

                // Permite cambiar el ciclo de trabajo en tiempo real
                i = teclado();
                if (i != 0.0) {
                    j = i;  // Actualiza el ciclo de trabajo según el nuevo valor
                    printf(lcd_putc, "\f p n alto: %f", j);
                }
            }
        }
    }
}
