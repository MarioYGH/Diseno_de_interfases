// Diseñe un programa en lenguaje C que implemente un contador del 0 al 9. La cuenta debe incrementar en uno, cada segundo. El resultado del conteo se debe
// mostrar en un display de 7 segmentos. Cuando el contador alcance la cuenta máxima (9) deberá reiniciar a cero (0) y continuar el conteo.


#include<18F4550.h>
#include<stdbool.h>
#fuses XT, NOWDT, NOPROTECT, NOLVP,PUT
#use delay(clock=4000000)
#use fast_io(B)
#use fast_io(D)

int1 x[7];
long display;
// && and
// || or
// ! not

//a !D&&B||!C&&!A||C&&B||D&&!C&&!B||!D&&C&&A   
//b !D&&!C||!D&&!B&&!A||!D&&B&&A||D&&!B&&A||!C&&!A
//c !D&&C||D&&!C||!D&&B||!C&&!A||D&&!B&&A ESTA MAAAL !D&&C||!C&&D||!B&&A||!D&&!B||!D&&A;
//d D&&!B&&!A||C&&!B&&A||C&&B&&!A||!C&&B&&A||!D&&!C&&!A
//e D&&C||D&&B||B&&!A||!C&&!A
//f D&&!C||D&&B||!D&&C&&!B||!D&&!B&&!A||C&&B&&!A
//g D||B&&!A||C&&!B||!C&&B

void main(){
set_tris_B(0x00); 
set_tris_D(0xFF); 

bool A = 0;
bool B = 0;
bool C = 0;
bool D = 0;
int i = 0;


while(TRUE){ 

if(i==0){ A=0; B=0; C=0; D=0; }
else if(i==1){ A=1;}
else if(i==2){ A=0; B=1; }
else if(i==3){ A=1; B=1; }
else if(i==4){ A=0; B=0; C=1; }
else if(i==5){ A=1; B=0; C=1;  }
else if(i==6){ A=0; B=1; C=1;  }
else if(i==7){ A=1; B=1; C=1;  }
else if(i==8){ A=0; B=0; C=0; D=1; }
else if(i==9){ A=1; B=0; C=0; D=1; }

x[0] = !D&&B||!C&&!A||C&&B||D&&!C&&!B||!D&&C&&A;   //a
x[1] = !D&&!C||!D&&!B&&!A||!D&&B&&A||D&&!B&&A||!C&&!A; //b
x[2] = !D&&C||!C&&D||!B&&A||!D&&!B||!D&&A; //c 
x[3] = D&&!B&&!A||C&&!B&&A||C&&B&&!A||!C&&B&&A||!D&&!C&&!A; //d
x[4] = D&&C||D&&B||B&&!A||!C&&!A; //e
x[5] = D&&!C||D&&B||!D&&C&&!B||!D&&!B&&!A||C&&B&&!A; //f
x[6] = D||B&&!A||C&&!B||!C&&B; //g

display = 64*x[6] + 32*x[5] + 16*x[4] + 8*x[3] + 4*x[2] + 2*x[1] + 1*x[0];  

output_b(display);
delay_ms(1000);
i=(i+1)%10;

 }
}
