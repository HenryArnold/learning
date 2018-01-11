# include <stdio.h>

int main()
{
	FILE *fp = NULL;
	
	fp = fopen("test.txt", "w+");
	fprintf(fp, "this is testing for fprint...\n");
	pfuts("this is testing for fputs...\n", fp);
	fclose(fp); 
}
