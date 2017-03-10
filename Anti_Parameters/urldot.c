#include<stdio.h>

main()
{	
	int i;
	char url[100];
	int d=0;
	//scanf("%s",url);
	gets(url);
	for(i=0;i<strlen(url);i++)
	{
		
		if(url[i]=='.')
		{
			d++;
		}
	}
	if (d>4)
		printf("True");
	else
		printf("False");
}
