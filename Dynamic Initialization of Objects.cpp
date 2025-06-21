#include<iostream>
using namespace std;
class X
{
	int n; float avg; 
	public:
		X(int p,float q)
		{
			n=p;
			avg=q;
		}
	void disp()
	{
		cout<<"Roll number"<<n;
		cout<<"Average"<<avg;
	}};
	int main()
	{
	
	int a; float b;
	cout<<"Enter the Roll Number:";
	cin>>a;
	cout<<"Enter the Average:";
	cin>>b;
	X x(a,b);
	x.disp();
	return 0;
}
