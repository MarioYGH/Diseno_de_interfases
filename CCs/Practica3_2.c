// Diseñe un programa en lenguaje C que permita controlar el tiempo en estado alto de una señal cuadrada con frecuencia 1 Hz, generada en el PIN A0. Cada botón
// del teclado será designado para establecer un múltiplo de la duración base (100 ms) en estado alto. De manera que, el botón 1 generará una señal cuadrada con
// 100 ms en estado alto y 900 ms en estado bajo; el botón 2: 200 ms en estado alto y 800 ms en estado bajo; el botón 3: 300 ms en estado alto y 700 ms en estado bajo.
// Este procedimiento será aplicado de la misma manera para los 9 botones. En eldisplay LCD se debe visualizar la selección que el usuario estableció a través del teclado. Las señales generadas se verificarán con un osciloscopio.

#include <18F4550.h>
#device ADC = 10
#fuses HS,NOWDT,NOPROTECT,NOPUT,NOLVP,BROWNOUT
#use delay(clock=20M)
#use standard_io(C)
#use standard_io(D)
#use fast_io(B)
#include <lcd.c>

#define pwm_ch0 PIN_A0        // Definimos el pin A0 como canal PWM

#define use_pwm_channel_0     // Utilizamos el canal de PWM para A0
#include <pwm_soft.c>
#include <map_function.c>

int q = 30;  // Tiempo de espera entre lecturas del teclado

float teclado() {
    float k = 0.0;
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

void generar_pwm_con_teclado(float duty_cycle) {
    // duty_cycle es un valor entre 0.0 y 1.0 que determina el ciclo de trabajo
    int duty = duty_cycle * 255;  // Escalamos a un valor de 0 a 255 para la función de PWM
    pwm_0_duty(duty);  // Aplica el ciclo de trabajo en el canal PWM 0 (PIN_A0)
}

void main() {
    // Configuración de los pines
    set_tris_b(0x38);  // Configura PORTB como entrada para el teclado
    set_tris_a(0xFE);  // Configura el pin A0 como salida
    lcd_init();        // Inicializa el LCD
    port_b_pullups(TRUE);  // Habilita resistencias pull-up en PORTB

    float j = 0.0;
    float i = 0.0;

    // Inicializa el PWM
    pwm_init();
    
    while(TRUE) {
        // Visualiza el valor inicial en el LCD
        printf(lcd_putc, "\f p n alto: %f", 0.0);
        
        j = teclado();  // Lee la selección del teclado para establecer el duty cycle
        
        if (j != 0.0) {
            // Muestra el ciclo de trabajo en el LCD
            printf(lcd_putc, "\f p n alto: %f", j);
            
            while (TRUE) {
                generar_pwm_con_teclado(j);  // Genera la señal PWM manualmente en el pin A0

                // Permite cambiar el ciclo de trabajo en tiempo real
                i = teclado();
                if (i != 0.0) {
                    j = i;  // Actualiza el ciclo de trabajo si se selecciona un nuevo valor
                    printf(lcd_putc, "\f p n alto: %f", j);  // Actualiza el LCD con el nuevo valor
                }
            }
        }
    }
}
