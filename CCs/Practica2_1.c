#include<16F877A.h>
#include<stdbool.h>
#fuses XT, NOWDT, NOPROTECT, NOLVP,PUT
#use delay(clock=4000000)
#use fast_io(B)
#use fast_io(D)

#byte portb = 0x06
#byte portd = 0x08
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
set_tris_B(0xFF); 
set_tris_D(0x00); 
portb = 0;
portd = 0;
bool A,B,C,D;


while(TRUE){ 
A = input(PIN_B0);
B = input(PIN_B1);
C = input(PIN_B2);
D = input(PIN_B3);

x[0] = !D&&B||!C&&!A||C&&B||D&&!C&&!B||!D&&C&&A;   //a
x[1] = !D&&!C||!D&&!B&&!A||!D&&B&&A||D&&!B&&A||!C&&!A; //b
x[2] = !D&&C||!C&&D||!B&&A||!D&&!B||!D&&A; //c 
x[3] = D&&!B&&!A||C&&!B&&A||C&&B&&!A||!C&&B&&A||!D&&!C&&!A; //d
x[4] = D&&C||D&&B||B&&!A||!C&&!A; //e
x[5] = D&&!C||D&&B||!D&&C&&!B||!D&&!B&&!A||C&&B&&!A; //f
x[6] = D||B&&!A||C&&!B||!C&&B; //g

display = 64*x[6] + 32*x[5] + 16*x[4] + 8*x[3] + 4*x[2] + 2*x[1] + 1*x[0];  

output_d(display);

 }
}
