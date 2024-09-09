#include <18F4550.h>
#fuses XT,NOWDT,NOPROTECT,NOLVP

#use delay (clock = 4000000)
#include <lcd.c>
#use fast_io(B)

int x[4]; //arreglo de contraseña con 4 valores en ascii decimal
int y[4]; // arreglo para almacenar intento de escribir contraseña
int i=0; 
int k;    // var para almacenar la lectura del teclado
int j=0;
int t=1; // var para indicar si la contraseña es correcta
int l=1; //intentos de contraseña
int q = 30;

int teclado(){

         output_b(6);
         k = !input(pin_b0)*!input(pin_b3) + !input(pin_b0)*!input(pin_b4)*2 + !input(pin_b0)*!input(pin_b5)*3;
         if(k!=0){return k;}
         delay_ms(q);
         
         output_b(5);
         k = !input(pin_b1)*!input(pin_b3)*4 + !input(pin_b1)*!input(pin_b4)*5 + !input(pin_b1)*!input(pin_b5)*6;
         if(k!=0){return k;}
         delay_ms(q);
         
         output_b(3);
         k = !input(pin_b2)*!input(pin_b3)*7 + !input(pin_b2)*!input(pin_b4)*8 + !input(pin_b2)*!input(pin_b5)*9;
         if(k!=0){return k;}
         delay_ms(q);
        
        return 0;
       
}

void main()
{

   set_tris_b(0x38);
   lcd_init();
   port_b_pullups(TRUE);//pullups para las 12 teclas
   
   
  while(TRUE){
  
   if(i==0){ lcd_putc("\fNew password\n"); } //i==0 inicia el programa, si contraseña es correcta se reinicia el programa
   
   
   while(i<4){
   k = teclado();
        if(k!=0){
        lcd_gotoxy(i+1,2);
        printf(lcd_putc, "%i", k); //imprime cada lectura
        delay_ms(100);
        x[i]=k;      //almacena lectura en posicion i del arreglo
        delay_ms(100); 
        if(i==3){ lcd_putc("\f****"); delay_ms(500); } //muestra que la contraseña se guardo al llegar a 4 digitos
        i++; //aumenta el valor de i para salir de este while
        }
   }
   
   delay_ms(500);
   lcd_putc("\fPassword: \n"); //pide ingresar contraseña
   
   while(i>=4 && j<4){
   k = teclado();
        if(k!=0){
        lcd_gotoxy(j+1,2);
        printf(lcd_putc, "%i", k);      //imprime cada lectura 
        y[j]=k;          //almacena en arreglo la lectura para ser comparada con la contraseña 
        if(y[j] != x[j]){ t=0; }  //cambia el valor del indicador t, si un digito no coincide el indicador es 0.
        lcd_gotoxy(j+1,2);
        lcd_putc("*");            //protege visualizacion de la contraseña ingresada
        delay_ms(100); 
        if(j==3){ printf(lcd_putc,"\f****"); } //indica que recibio la contraseña ingresada
        j++;
        }
   }
  
   
    if(t==0){      // si es incorrecta por el indicador t=0, reinicia los valores del indicador y las posiciones j, menos los valores de i para no ingresar al loop que almacena la contraseña inicial
         lcd_putc("\fIncorrect pass");
         delay_ms(1000);
         lcd_putc('\f');
         j=0;
         t=1;
         if(l==3){ lcd_putc("\fSuperaste el numero\n"); lcd_putc("de intentos"); i=0; j=0; t=1; l=1; delay_ms(2000); } //superas 3 intentos y reinicia el programa
         l++;
       }
      else{ // si t=1 la contraseña es correcta y reinicia todos los valores para reiniciar el programa
        lcd_putc("\fCorrect password");
        delay_ms(1500);
        lcd_putc('\f');
        i=0;
        j=0;
        t=1;
       }
   
  
  }
  
   
  
  
   
      //TODO: User Code
}
