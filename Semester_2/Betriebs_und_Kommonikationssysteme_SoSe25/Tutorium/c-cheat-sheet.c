// Header file for input output functions
#include <stdio.h>

// Main function: entry point for execution
int main() {
  
  printf("Hello World");

  return 0 // This statement indicates that the programm ended successfully
}

// Compiling using GCC Compiling
// gcc filename.c -o filename

// Keywords
// %d - int
// %s - string
// %c - char
// %f - double / float

// If statement
if (a < b) {
  printf("A ist kleiner B");
}
else {
  printf("B ist größer als A");
}

// For loop
for (int i = 0; i < 5; i++) {
  printf("%d ", i);
}

// while loop
while (i < 3) {
  printf("Hi\n");
  i++;
}
