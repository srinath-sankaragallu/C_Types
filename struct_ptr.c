#include <stdio.h>
#include <string.h>
struct student
{
    char name[50];
    int age;
};

// function prototype
void display(struct student *s);

int main()
{

	printf("Welcome to Cprogramming\n");
    
    return 0;
}
void display(struct student *s) 
{
  printf("\nDisplaying information\n");
  printf("Name: %s", s->name);
  printf("\nAge: %d", s->age);
}

struct student getInformation() 
{
  struct student s1;

  printf("Enter name: ");
  scanf ("%[^\n]%*c", s1.name);

  printf("Enter age: ");
  scanf("%d", &s1.age);
  
  return s1;
}

void updateinfo(struct student *s)
{
	strcpy(s->name , "renamed");
	s->age = 45;
	
}
