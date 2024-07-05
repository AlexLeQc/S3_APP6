#include <stdio.h>
#include <sys/timeb.h>
#include <string.h>
#include <stdlib.h>
#define CANARI_SIZE 10
#define RETURN check_canari(canari); return

char cmd[10000];
int variable_nulle = 0;
FILE *name_file;
int i, c;
int canari_global;
int c_op = 1;

void canari_op(int *canari) 
{
  int i;

  if (c_op == 0) {
    return;
  } else {
      *canari ^= 0x5555;
  }
}

int get_canari(void) 
{
  int tmp_canari;

  tmp_canari = canari_global;
  canari_op(&tmp_canari);
  return(tmp_canari);
}

void set_canari() 
{
  int i;
  struct timeb tb;
  int seed;
 
  ftime(&tb);
  seed = tb.millitm;
  srandom(seed);

  canari_global = (int) random();
}

void check_canari(int canari_a_verifier)
{
  int i;
  int tmp_canari;

  tmp_canari = canari_global;

  canari_op(&tmp_canari);
  if (tmp_canari != canari_a_verifier) {
    printf("Probleme de Buffer overflow\n");
    exit(1);
  }
}

void appel_problematique(char *usager) {
  int canari = get_canari();
  char usager_local[1024];

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
  
  if (i > 1024 ) {
    fclose(name_file);
    fprintf(stdout,"Fichier trop gros!\n");
    RETURN;
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

  RETURN;
}

int main (int argc, char **argv) {
  int i;
 
  set_canari();
  fprintf(stdout, "Lecture des donnees du fichier: \"%s\"\n", argv[1]);
  fflush(stdout);

  appel_problematique(argv[1]);

  exit(0);
}
