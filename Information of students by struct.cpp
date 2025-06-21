#include<iostream>
#include<string>
using namespace std;
struct 
{
	float height;
	int age,weight;
}stud;
int main( )
{
	cout<<"\nInformation of Students";
	cout<<"\nEnter your height:";
	cin>>stud.height;
	cout<<"\nEnter your age:";
	cin>>stud.age;
	cout<<"\nEnter your weight:";
	cin>>stud.weight;
	cout<<"\nThe given information";
	cout<<stud.height<<"cm"<<"\t"<<stud.age<<"years old"<<"\t"<<stud.weight<<"kg";
	return 0;
}
