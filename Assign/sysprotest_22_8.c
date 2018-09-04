#include<stdio.h>
#include<stdlib.h>
#include<string.h>
FILE *fp;

int main()
{
   int i,ct,cnt,db,dd,cdb,cdq,cdd,cdw;
   ct=cnt=dd=db=cdb=cdq=cdd=cdw=0;
   char *arr;
   arr=malloc(sizeof(char)*200);
   fp=fopen("test.asm","r");
   while(!feof(fp))
   {
     if(feof(fp))
       break;
     fscanf(fp,"%s",arr);
     printf("%s\n",arr);
     if((strcasecmp(arr,"db"))==0)
     { 
       cnt++;
       while(!feof(fp))
       {
         fscanf(fp,"%s",arr);
         printf("%s\n",arr);
         for(i=0;arr[i]!='\0';i++)
         {
       	   if(arr[i]=='"')
       	     ct+=1;
           if(arr[i]!='"')
           {
             if(arr[i]==','&&ct!=2)
               db+=1;  
             if(arr[i]!=',')
	     {
	       if(arr[i]!='%')
	         cdb+=1;
             }
           }
         }
         if(ct==2)
           break;
       }
     }
     if((strcasecmp(arr,"dd"))==0)
     {
       dd++;
       fscanf(fp,"%s",arr);
       for(i=0;arr[i]!='\0';i++)
       {
          if(arr[i]==',')
              cdd+=1;  
       }
       cdd++;
     }
     if((strcasecmp(arr,"resd"))==0)
     {
         
     }
    }
   printf("DB=%d\t%d",cnt,cdb+db);
   printf("\nDD=%d\t%d",dd,cdd);
}
