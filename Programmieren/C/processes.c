#include <stdio.h>     // printf(), perror()
#include <stdlib.h>    // exit(), rand(), srand()
#include <unistd.h>    // fork(), sleep(), getpid()
#include <sys/wait.h>  // wait(), WEXITSTATUS()
#include <time.h>      // time()
#include <string.h>    // strcmp()


struct Process{
    int pid;
    int working;
};


int main(){

    srand(time(NULL));
    //int x = rand()%100;

    struct Process children[3];


    printf("Elternprozess PID: %d\n", getpid());

    for (int i = 0; i<3; i++){
        pid_t pid = fork();

        if (pid == 0){
            //Kindprozess
            printf("Ich bin ein Kind %d mit PID %d\n", i, getpid());
            sleep(2);
            exit(42 + i);
        } else if (pid > 0){
            //Elternprozess
            children[i].pid = pid;
            children[i].working = 1;
        } else{
            printf("Fehler");
        }
    }

    for (int i = 0; i < 3; i++){
        int status;
        waitpid(children[i].pid, &status, 0);
        children[i].working = 0;

        
        if(WIFEXITED(status)){
            int code = WIFEXITED(status);
            printf("Kind %d (PID %d) ist beendet mit Code: %d\n", i, children[i].pid, code);
        }
    }

    return 0;
}