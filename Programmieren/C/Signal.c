#include <stdio.h> // Schreiben auf Konsole
#include <stdlib.h> // atoi() zum Konvertieren von String zu Integer
#include <unistd.h> // getpid(), sleep(), write(), etc.
#include <signal.h>


volatile int sigint_count = 0;
enum State {RUNNING = 0, PAUSED = 1};
volatile enum State status = RUNNING; // status = 0 -> aktiv, 1 -> pausiert
volatile int numberCount = 0;



void handler(int sig){
    if (sig == SIGINT){
        sigint_count++;
        status = !status;
        if (sigint_count == 1){
            printf("Signal %d - Erstes Signal empfangen - drücke nochmal zum beenden\n", sig);
            if (status){
                printf("Zähler pausiert\n");
            }
        } 
    } else if (sig == SIGTERM){
        printf("SIGTERM empfangen - beende Programm nach %d Sekunden.\n", numberCount);
        exit(0);
    }

}

void countLogic(){
    static int count = 0;
    if (!status){
        numberCount = count++;
    }
}

void printStatus(){
    if (!status){
        printf("Sekunden: %d\n", numberCount);
    }
}

int main() {

    struct sigaction sa;
    sa.sa_handler = handler; // setzt die Handler Funktion
    sigemptyset(&sa.sa_mask); // Leere Make: keine anderen Signale blockieren 
    sa.sa_flags = 0; // Keine speziellen Flags setzen

    printf("PID: %d\n", getpid());
    sigaction(SIGINT, &sa, NULL);
    sigaction(SIGTERM, &sa, NULL);

    while(1){
        countLogic();
        printStatus();
        sleep(1);
    }

    return 0;
}



