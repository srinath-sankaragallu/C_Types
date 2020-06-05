#include<stdio.h>

int add(int a,int b)
{
	return a+b;
}
int sub(int a,int b)
{
	return a-b;
}
int mul(int a,int b)
{
	return a*b;
}

int main()
{
	int a = 10 , b = 5 , res;
	
	int  (*optr[])(int,int) = {add , sub , mul} ;
	
	res = (*optr[0])(a,b) ; 
	printf(" addition from function pointer : %d " , res);
	
	return 0;
}