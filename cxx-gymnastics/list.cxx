#include <list>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
  list<int> l;
  for(unsigned i = 0 ; i < 10 ; i++){
    l.push_back(i);
  }
  
  // iterate forward
  for(list<int>::const_iterator iter = l.begin() ; 
      iter != l.end() ; 
      iter++){
    cout<<*iter<<endl;
  }

  // iterate backward
  for(list<int>::const_reverse_iterator iter = l.rbegin() ; 
      iter != l.rend() ; 
      iter++){
    cout<<*iter<<endl;
  }

  // insert 100 before 5
  list<int>::iterator dest = find(l.begin(),l.end(),5);
  l.insert(dest,100);

  // check that it's there
  for(list<int>::const_iterator iter = l.begin() ; 
      iter != l.end() ; 
      iter++){
    cout<<*iter; 
    if(*iter == 4)
      cout<<" (next should be 100)";
    cout<<endl;
  }


}
