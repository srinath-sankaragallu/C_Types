int f(int n, int (*h)(int))
{ 
	return (*h)(n); 
}


int addone(int n)
{ 
	return n+1; 
}


int addtwo(int n)
{
	return n+2;
}