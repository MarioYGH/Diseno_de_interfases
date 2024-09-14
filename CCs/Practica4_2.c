// Diseñe un programa en lenguaje C que permita resolver numéricamente (por el método de Runge-Kutta cuarto orden) la ecuación diferencial que se muestra
// abajo. La solución numérica de la ecuación diferencial debe ser convertida en una señal analógica usando el DAC MCP4921. La señal generada tendrá que ser
// verificada en un osciloscopio. )dx^2/dt2) − μ(1 − x^2)*(dx/dt) + x = 0
// Considere que μ = 4, y que las condiciones iniciales son y(0) = 0.1 y y′(0) = 0.2.

#include <ec2.h>

#fuses XT, NOWDT,NOPUT,NOLVP,NOPROTECT,BROWNOUT
#use delay(clock=20000000) 
#include <mcp4921.c>
#use fast_io(B)

float mu = 4;
float dt = 0.01;
float x[2] = {0.1, 0.0};
float z[2] = {0.2, 0.0};
float g1 = 0.0;
float g2 = 0.0;
float g3 = 0.0;
float g4 = 0.0;
float f1 = 0.0;
float f2 = 0.0;
float f3 = 0.0;
float f4 = 0.0;
float valor = 0.0;
int16 r = 2048;

void main()
{
   
   init_dac();
   
   while(TRUE)
   {
   


        g1 = z[0];
        f1 = mu * (1.0 - x[0] * x[0]) * z[0] - x[0];
        g2 = z[0] + (dt/2.0) * f1;
        f2 = mu * (1.0 - (x[0] + (dt / 2.0) * g1) * (x[0] + (dt / 2.0) * g1)) * (z[0] + (dt / 2.0) * f1) - (x[0] + (dt / 2.0) * g1);
        g3 = z[0] + (dt / 2.0) * f2;
        f3 = mu * (1.0 - (x[0] + (dt / 2.0) * g2) * (x[0] + (dt / 2.0) * g2)) * (z[0] + (dt / 2.0) * f2) - (x[0] + (dt / 2.0) * g2);
        g4 = z[0] + dt * f3;
        f4 = mu * (1.0 - (x[0] + dt * g3) * (x[0] + dt * g3)) * (z[0] + dt * f3) - (x[0] + dt * g3);
        x[1] = x[0] + (dt / 6.0) * (g1 + (2.0*g2) + (2.0*g3) + g4);
        z[1] = z[0] + (dt / 6.0) * (f1 + (2.0*f2) + (2.0*f3) + f4); 
        
        
        valor = (int16) ((x[1]+2.5)*2048.0)/2.5;
        write_dac(valor);
        x[0] = x[1];
        z[0] = z[1];     

   }

}
