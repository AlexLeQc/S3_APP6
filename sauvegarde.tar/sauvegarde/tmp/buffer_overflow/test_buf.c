#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char cmd[10000];
int variable_nulle = 0;
FILE *name_file;
int i, c;

void appel_problematique(char *usager) {
	char usager_local[2048];

	strcpy(cmd,"echo \"Pouvez-vous faire afficher ce message?\"");
	name_file = fopen(usager,"r");
	c = fgetc(name_file);
	i = 0;
	while (c != EOF) {
		usager_local[i] = c;
		c = fgetc(name_file);
		i++;
	}
	usager_local[i-1] = 0;

	if (i > 2048 ) {
		fclose(name_file);
		fprintf(stdout,"Fichier trop gros!\n");
		return;
	} else {
		fclose(name_file);
		strcpy(cmd,"echo ");
		strcat(cmd,usager_local);
		system(cmd);
	}

	if (variable_nulle) {
	  strcpy(cmd,"echo \"Ce message ne devrait jamais etre affiche...\"");
	  system(cmd);
	}

	return;
}

int main (int argc, char **argv) {
	int i;

	fprintf(stdout, "Lecture des donnees du fichier: \"%s\"\n", argv[1]);
	fflush(stdout);

	appel_problematique(argv[1]);

	exit(0);
}
