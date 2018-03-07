#include <vector>
#include <iostream>
#include <map>

using namespace std;

int main(){
  vector<int> vec({0,1,2,3,4,5,6,7});

  for(int item : vec){
    cout<<item<<" ";
  }
  cout<<endl;

  map<string,string> mp ({{"foo","abc"},{"bar","efg"},{"goo","hij"}});

  for(pair<string,string> item : mp){
    cout<<item.first<<":"<<item.second<<" ";
  }
  cout<<endl;
}
