#include<iostream>
using namespace std;
void disp()
{
	int a,b;
	cout<<"The value inside display function:"<<a*a<<endl;
}
int main()
{
	int a;
	cout<<"Function call by value method"<<endl;
	cout<<"Enter the value:";
	cin>>a;
	cout<<"The value inside main function:"<<a;
	disp(a);
	return 0;
	
}
