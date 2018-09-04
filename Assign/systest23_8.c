#include<stdio.h>
#include<stdlib.h>
#include<string.h>
FILE *fp;

int main()
{
   int i,j=0,k;
   char *arr,**list;
   arr=malloc(sizeof(char)*100);
   list=malloc(sizeof(char *)*1);
   fp=fopen("assignment_1.asm","r");
   while(!feof(fp))
   {
     if(feof(fp))
       break;
     fscanf(fp,"%s",arr);
     //printf("%s\n",arr);
     if((strcasecmp(arr,"global"))==0)
     {
        fscanf(fp,"%s",arr);
        for(i=0;arr[i]!='\0';i++)
        {
          if(i==0)
           list[j]=malloc(sizeof(char)*1);
          else
           list[j]=realloc(list[j],sizeof(char)*(i+1));  
          list[j][i]=arr[i];
        }
        j+=1;
        list=(char **)realloc(list,sizeof(char *)*(j+1));
     }
     if((strcasecmp(arr,"extern"))==0)
     {
       fscanf(fp,"%s",arr);
       for(i=0,k=0;arr[i]!='\0';i++,k++)
       {
         if(arr[i]!=',')
         {
          if(k==0)
           list[j]=malloc(sizeof(char)*1);
          else
           list[j]=realloc(list[j],sizeof(char)*(i+1));
       	  list[j][k]=arr[i];
       	 }
       	 else if(arr[i]==',')
       	 {
       	   j+=1;
       	   list=(char **)realloc(list,sizeof(char *)*(j+1));
       	   k=-1;
         }
       }
       j+=1;
       list=(char **)realloc(list,sizeof(char *)*(j+1));
     }
     if((strcasecmp(arr,"jmp"))==0 || (strcasecmp(arr,"jz"))==0 || (strcasecmp(arr,"jnz"))==0)
     {
        fscanf(fp,"%s",arr);
        for(i=0;arr[i]!='\0';i++)
        {
          if(i==0)
           list[j]=malloc(sizeof(char)*1);
          else
           list[j]=realloc(list[j],sizeof(char)*(i+1));  
          list[j][i]=arr[i];
        }
        j+=1;
        list=(char **)realloc(list,sizeof(char *)*(j+1));
     }
   }
   for(k=0;k<j;k++)
     printf("%s\n",list[k]);
}
    
