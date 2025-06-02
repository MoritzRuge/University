#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[]){
	char *end;
	for(int i =0; argv[1][i]!='\0';i++){
		if(!isdigit(argv[1][i])){
			fprintf(stderr, "Given argument %s is no valid integer\nExit status 1\n", argv[1]);
			return 1;
		}
	}
        for(int i =0; argv[2][i]!='\0';i++){
                if(!isdigit(argv[2][i])){
                        fprintf(stderr, "Given argument %s is no valid integer\nExit status 1\n", argv[2]);
                        return 1;
                }
        }
	long int wert1 = strtol(argv[1], &end, 10);
	long int wert2 = strtol(argv[2], &end, 10);
        if(argc < 3){
                fprintf(stderr, "Required summand is missing!\nExit Status 1\n");
                return 1;
        }
        if(argc > 3){
                fprintf(stderr, "Superfluous argument was given! Only two are allowed. \nExit Status 1 \n");
                return 1;
        }
	printf("%li \n", wert1+wert2);
return 0;
}
