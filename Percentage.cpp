#include<iostream>
using namespace std;
int main()
{
	int x;
	float per;
	cout<<"Enter the Percentage:";
	cin>>per;
	cout<<"You Scored"<<per<<"%"<<endl;
	x=per/10;
	switch(x)
{
	case 10:
	case 9:
	case 8:
	cout<<"You have passed with Distincion!";
	break;
	case 7:
	case 6:
	cout<<"You have passed with First Division!";
	break;
	case 5:
	cout<<"You have passed with Second Division!";
	break;
	case 4:
	cout<<"You have passed with Third Division!";
	break;
	default:
	cout<<"Sorry! You have Failed.";	
}
	return 0;
}
