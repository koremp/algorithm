#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int N;
  cin >> N;

  vector<int> size_list(6);
  for (int i = 0; i < 6; i++)
  {
    cin >> size_list[i];
  }

  int T, P;
  cin >> T >> P;

  int count = 0;
  for (int i : size_list)
  {
    if (i > 0)
    {
      if (i % T != 0)
      {
        count += i / T + 1;
      }
      else
      {
        count += i / T;
      }
    }
  }

  cout << count << endl;
  cout << N / P << " " << N % P << endl;

  return 0;
}