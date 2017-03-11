#include<stdio.h>

main()
{	
	int i;
	char url[100];
	int w=0;
	int flag=0;
	int p=0;
	//scanf("%s",url);
	gets(url);
	for(i=0;i<4;i++)
	{
		
		if(url[i]=='w')
		{
			w++;
		}
	}
	if(url[3]=='.')
		flag=1;
	if (w<4 && flag==1)
		printf("False");
	else
		printf("True");
	for(i=4;i<strlen(url)-3;i++)
	{
		if(url[i]=='w' && url[i+1]=='w' && url[i+2]=='w' && url[i+3]=='.')
			p=1;
	}
	if(p==1)
		printf("\nTrue");
	else
		printf("\nFalse");
}
