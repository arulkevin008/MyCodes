#include<iostream>
using namespace std;
int main()
{
	int num,n,digit,rev=0;
	cout<<"Enter the number:";
	cin>>num;
	n=num;
	while (num)
	{
		digit=num%10;
		rev=(rev*10)+digit;
		num=num/10;
	}
	cout<<"The reverse of the number:"<<rev<<endl;
	if (n==rev)
	cout<<"The number is a palindrome.";
	else
	cout<<"The number is not a palindrome.";
	return 0;
}
