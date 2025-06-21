#include<iostream>
using namespace std;
int main()
{
	int bs,gs,hra,da;
	cout<<"Enter the basic salary of an employee:";
	cin>>bs;
	if (bs<25000)
{
	da = bs*80/100;
	hra = bs*20/100;
	}	
	else if (bs>=25000 && bs<40000)
{
	da = bs*90/100;
	hra = bs*25/100;
	}	
	else if (bs>=40000)
{
	da = bs*95/100;
	hra = bs*30/100;
	}	
	gs=bs+hra+da;
	cout<<"\n\tBasic Salary:"<<bs;
	cout<<"\n\tDearness Allowance:"<<da;
	cout<<"\n\tHouse Rent Allowance:"<<hra;
	cout<<"\n\tGross Salary:"<<gs;
	return 0;
}
