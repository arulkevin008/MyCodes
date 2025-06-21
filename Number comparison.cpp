#include<iostream>
using namespace std;
int main()
{
	int a,b;
	cout<<"Enter the first number:";
	cin>>a;
	cout<<"\nEnter the second number:";
	cin>>b;
	if (a>b)
	{
	cout<<"\nThe least number is "<<b;
	cout<<"\nThe greatest number is "<<a;
}
	else if (a<b)
	{
	cout<<"\nThe least number is "<<a;
	cout<<"\nThe greatest number is "<<b;
}
	else if (a==b)
	cout<<"\nBoth are equal.";
	return 0;
}
