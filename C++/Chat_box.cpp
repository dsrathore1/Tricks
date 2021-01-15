#include <iostream>
using namespace std;

int main () 
{
	
	string name;
	
	string Qn;
	
	int age;
	
	cout << "Hello, I am AISHA. What is your name?\n";
	
	cin >> name;
	
	cout << " \nHello " << name << ", what is your age?\n";
	
	cin >> age;
	
	if (age <= 10)
	{
		cout << "Sorry," << name <<  "your age is " << age << ". So you do not have vaild age to ask any Question Please try after some years, Thank You!\n";
	}
	
	else
	{
		cout << "\nYour age is " << age << " How may I help you?\n";
	}
	
	cin >> Qn;
	
	cout << "\nOk your Question is " << Qn;
	
	cout << "\n\nSorry, I don't have any answer of your Question. Google it";

}


