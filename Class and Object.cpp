#include<iostream>
using namespace std;
class Arithmetic
{
	public:
		int a,b;
	
		void Sum()
		{
			cout<<"The Sum is:"<<a+b<<endl;
			
		}
		void Sub()
		{
			cout<<"The Difference is:"<<a-b<<endl;
		}
		void Product()
		{
			cout<<"The Product is:"<<a*b<<endl;
		}
		void Division()
		{
			cout<<"The Division is:"<<a/b<<endl;
		}
		
};
	int main()
{
		Arithmetic obj;
		cout<<"Enter the two no:";
		cin>>obj.a>>obj.b;
		obj.Sum();
		obj.Sub();
		obj.Product();
		obj.Division();
}
				
