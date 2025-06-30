#include <stdio.h> // für printf
#include <unistd.h> // für Pause



//Globale Variablen
struct Student {
    char name[50];
    int matrikelnummer;
    float durchschnitt;
};

// Ausgabefunktion für Studentennamen
void printStudent(struct Student* s){
    printf("Student: %s\n"
        "Matrikelnummer: %d\n"
        "Note: %.1f\n\n",s->name, s->matrikelnummer, s->durchschnitt);
}

void updateGrade(struct Student* s, float neueNote){
    s->durchschnitt = neueNote;
}

int main(){
    // Studenten initialisieren mit Array
    struct Student studenten[3] = {
        {"Alice", 12345, 2.4},
        {"Bob", 32451, 3.1},
        {"Hannes", 99999, 2.6}
    };


    for (int i =0; i < 3; i++) {
        printStudent(&studenten[i]);
    }
    
    // Alice Note aktuallisieren:
    updateGrade(&studenten[0], 3.3);
    // Ausgabe
    printf("Note aktuallisiert!\n");
    printStudent(&studenten[0]);
    
    
    return 0;
}