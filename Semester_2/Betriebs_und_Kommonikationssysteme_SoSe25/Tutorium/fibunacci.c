#include <stdio.h>

int fibo(int zahl);

int main(){
  int fib_zahl = 8;

  for (int i = 0; i <= fib_zahl; i++){
    printf("fib(%d) = %d\n",i,fibo(i));
  }

  return 0;
}

int fibo(int zahl){

  if (zahl <= 1){
    return zahl;
  }
  else{
    return fibo(zahl-1) + fibo(zahl-2);
  }
}
