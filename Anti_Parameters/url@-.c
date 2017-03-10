#include<stdio.h>

main()
{	
	int i;
	char url[100];
	int flag=0;
	//scanf("%s",url);
	gets(url);
	for(i=0;i<strlen(url);i++)
	{
		flag=0;
		if(url[i]=='@' || url[i]=='-')
		{
			flag = 1;
			break;
		}
	}
	if (flag==1)
		printf("True");
	else
		printf("False");
}
