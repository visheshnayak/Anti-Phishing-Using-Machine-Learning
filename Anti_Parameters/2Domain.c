#include<stdio.h>

main()
{	
	int i;
	char url[100];
	int w=0;
	int flag=0;
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
}
