#include <stdio.h>
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/uart.h"

// Pines de los LEDs
const int LED_PINS[8] = {19, 21, 22, 23, 25, 26, 27, 32};

// Configuración de UART
#define UART_NUM UART_NUM_0
#define BUF_SIZE (1024)

// Configurar los LEDs
void config_LEDs() {
    for (int i = 0; i < 8; i++) {
        gpio_reset_pin((gpio_num_t)LED_PINS[i]);
        gpio_set_direction((gpio_num_t)LED_PINS[i], GPIO_MODE_OUTPUT);
    }
}

// Función para encender o apagar un LED
void set_LED(int index, bool state) {
    if (index >= 0 && index < 8) {
        gpio_set_level((gpio_num_t)LED_PINS[index], state ? 1 : 0);
    }
}

void app_main(void) {
    // Configurar los LEDs
    config_LEDs();

    // Configurar UART
    uart_config_t uart_config = {
        .baud_rate = 115200,
        .data_bits = UART_DATA_8_BITS,
        .parity = UART_PARITY_DISABLE,
        .stop_bits = UART_STOP_BITS_1,
        .flow_ctrl = UART_HW_FLOWCTRL_DISABLE
    };
    uart_param_config(UART_NUM, &uart_config);
    uart_driver_install(UART_NUM, BUF_SIZE, 0, 0, NULL, 0);

    uint8_t data[BUF_SIZE];

    while (true) {
        // Leer datos de UART
        int len = uart_read_bytes(UART_NUM, data, BUF_SIZE, 20 / portTICK_PERIOD_MS);
        if (len > 0) {
            data[len] = '\0';  // Asegurar que el mensaje esté terminado
            printf("Recibido: %s\n", data);

            // Parsear el comando recibido
            int index;
            if (sscanf((char *)data, "ON %d", &index) == 1) {
                set_LED(index, true);  // Encender LED
            } else if (sscanf((char *)data, "OFF %d", &index) == 1) {
                set_LED(index, false);  // Apagar LED
            }
        }
        vTaskDelay(100 / portTICK_PERIOD_MS);  // Pequeño retraso para evitar saturación
    }
}
