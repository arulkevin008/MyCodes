#include<iostream>
using namespace std;
class distance
{
	public:
	float inch,feet;
}d1,d2;
int main()
{
	cout<<"\nInformation for first number.";
	cout<<"\nEnter the feet:";
	cin>>d1.feet;
	cout<<"\nEnter the inch:";
	cin>>d1.inch;
	cout<<"\nInformation for second number.";
	cout<<"\nEnter the feet:";
	cin>>d2.feet;
	cout<<"\nEnter the inch:";
	cin>>d2.inch;
	cout<<"\nSum of feet:"<<d1.feet+d2.feet;
	cout<<"\nSum of inch:"<<d1.inch+d2.inch<<endl;
	cout<<d1.feet+d2.feet<<"feet"<<d1.inch+d2.inch<<"inches";
	return 0;	
}
