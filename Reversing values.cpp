#include<iostream>
using namespace std;
int reverse(int n);
int main()
{
	int n=0,result=0;
	cout<<"Enter the number:";
	cin>>n;
	result=reverse(n);
	cout<<"The Reversed number is:"<<result;
		return 0;
}
int reverse(int n)
{
	 int digit=0,temp=0,rev=0;
	while(n!=0)
	{
		digit=n%10;
		rev=(rev*10)+digit;
		n=n/10;
	}
		return rev;
}
	
