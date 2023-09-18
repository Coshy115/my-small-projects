#include <iostream>
#include <list>
#include <algorithm>
#include <conio.h>
using namespace std;

int main()
{
    string choice;
    int amount;
    list<int> nums = {};

    cout << "Min or Max?" << endl;

    cin >> choice;

    transform(choice.begin(), choice.end(), choice.begin(), ::tolower);

    if(choice == "min")
    {
        cout << "How many numbers?" << endl;
        cin >> amount;

        for(int i; i < amount; ++i)
        {
            int userInput;
            cout << "Enter Number " << (i+1) << ": ";
            cin >> userInput;
            nums.push_back(userInput);
        }

        cout << "\nYour List: ";

        for(int num : nums)
        {
            cout << num << " ";
        }

        int min;

        for(int num : nums)
        {
            if(num < min)
            {
                min = num;
            }
        }
        cout << "\nMinimum: " << min;
    }
    else if(choice == "max")
    {
        cout << "How many numbers?" << endl;
        cin >> amount;

        for(int i; i < amount; ++i)
        {
            int userInput;
            cout << "Enter Number " << (i+1) << ": ";
            cin >> userInput;
            nums.push_back(userInput);
        }

        cout << "\nYour List: ";

        for(int num : nums)
        {
            cout << num << " ";
        }

        int max;

        for(int num : nums)
        {
            if(num > max)
            {
                max = num;
            }
        }
        cout << "\nMaximum: " << max << endl;
    }
    cout << "\nPress ENTER to exit..." << endl;
    getch();
}
