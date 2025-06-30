#include <stdio.h>
#include <unistd.h>


// timer Struct
struct Timer {
    char name[50];
    int seconds;
    int paused;
};


void printTime(struct Timer *t){
    if(!t->paused){
        printf("Timer: %s - Sekunden %d\n", t->name, t->seconds);
    }
}


void tick(struct Timer *t){
    if (!t->paused) {
        t->seconds++;
    }
}


int main(){



    // Initialisieren des Structs t, vergibt namen und initial werte
    struct Timer t = {"Küchenuhr", 0, 0};

    while(1){
        if (!t.paused){
            tick(&t); //&t übergibt die Addresse
            printTime(&t); // &t übergibt die Addresse
            sleep(1);

            if (t.seconds ==5) {
                t.paused = !t.paused;
                printf("Timer pausiert...\n");
            }
        }
        
    }

    return 0;
}