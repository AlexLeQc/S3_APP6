#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TMP_CMD_SIZE 70
#define USAGER_LOCAL_SIZE 2048
#define CMD_SIZE 1000

char cmd[CMD_SIZE];
FILE *name_file;
int i, c;

void appel_problematique(char *usager) {
    char tmp_cmd[TMP_CMD_SIZE];
    char usager_local[USAGER_LOCAL_SIZE];

    strcpy(tmp_cmd,"/bin/bash -c \"cat /usr/local/share/tel_data|grep ");
    name_file = fopen(usager,"r");
    if (!name_file) {
        printf("Erreur: fichier \"%s\" introuvable\n",usager);
        exit(0);
    }

    c = fgetc(name_file);
    i = 0;
    while (c != EOF) {
        if (c != '\n') {
            usager_local[i] = c;
        }
        c = fgetc(name_file);
        i++;
    }

    usager_local[USAGER_LOCAL_SIZE-1] = 0;
    tmp_cmd[TMP_CMD_SIZE-1] = 0;
    strcpy(cmd,tmp_cmd);

    if (i >= USAGER_LOCAL_SIZE) {
        fclose(name_file);
        fprintf(stdout,"Fichier \"%s\" trop grand\n",usager_local);
    	return;
    } else {
        for (i = 0; i < USAGER_LOCAL_SIZE; i++) {
            if(!(((usager_local[i] >= 'a')
              && (usager_local[i] <= 'z'))
              || ((usager_local[i] >= 'A')
              && (usager_local[i] <= 'Z'))
              || ((usager_local[i] >= '0')
              && (usager_local[i] <= '9'))
              || (usager_local[i] == '_')
              || (usager_local[i] == '-'))) {
	        usager_local[i] = 0;
	        i = USAGER_LOCAL_SIZE;
	    }
	}

        fclose(name_file);
        strcat(cmd,usager_local);
        strcat(cmd,"; exit\"");
        system(cmd);
    }

    return;
}

int main (int argc, char **argv) {
    int i;

    fprintf(stdout, "\n", argv[1]);
    fflush(stdout);

    appel_problematique(argv[1]);

    exit(0);
}
