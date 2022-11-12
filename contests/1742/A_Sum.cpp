#include <bits/stdc++.h>

template <typename T>
void print(T &vecOfElements, std::string delimeter = " , ")
{
    for (auto elem : vecOfElements)
        std::cout << elem << delimeter;
    std::cout << std::endl;
}

int main()
{
    int n;
    std::cin >> n;
    std::cin.ignore();

    for (int i = 0; i < n; i++)
    {
        std::string input_str;
        std::getline(std::cin, input_str);
        std::stringstream in(input_str);
        std::vector<int> ints{std::istream_iterator<int, char>{in}, std::istream_iterator<int, char>{}};

        std::sort(ints.begin(), ints.end());
        if ((ints.at(0) + ints.at(1)) == ints.at(2))
        {
            std::cout << "YES" << std::endl;
        }
        else
        {
            std::cout << "NO" << std::endl;
        }
    }

    return 0;
}