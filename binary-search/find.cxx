#include <vector>
#include <cstdlib>
#include <iostream>

using namespace std;

int find(vector<int>& haystack,int needle,int low,int high){
  if(low > high)
    return -1;
  if(haystack[low] == needle)
    return low;
}

int find(vector<int>& haystack,int needle){
  int low = 0;
  int high = 99;
  int found = -1;
  while(low <= high){
    int mid = low + (high - low)/2;
    if(haystack[mid] == needle){
      found = mid;
      break;
    }
    if(haystack[mid] < needle)
      low = mid +1;
    else
      high = mid - 1;
    
  }
  return found;
}

int main(){

  vector<int> haystack;
  int cumulative = 0;
  for(unsigned i = 0 ; i < 100 ; i++){
    haystack.push_back(cumulative);
    cumulative = 2 + cumulative + rand() % 30;
  }

  // for(unsigned i = 0; i < haystack.size() ; i++){
  //   cout<<i<<" "<<haystack[i]<<endl;
  // }

  // elements we know are there
  for(int needleIndex = 0 ; needleIndex < 99 ; needleIndex++){
    int needle = haystack[needleIndex];
    int found = find(haystack,needle);
    if(needleIndex != found){
      cout<<"Akkkk"<<" "<<needleIndex<<" "<<found<<endl;
    }

  }

  // elements we know aren't to be found
  for(int needleIndex = 0 ; needleIndex < 99 ; needleIndex++){
    int needle = haystack[needleIndex]+1;
    int found = find(haystack,needle);
    if(found != -1){
      cout<<"Akkkk"<<" "<<needleIndex<<" "<<found<<endl;
    }

  }
}
