#include <tr1/unordered_map>
#include <string>
#include <iostream>
#include <map>
#include <sstream>

using namespace std;
using namespace std::tr1;

int main(){
  unordered_map<string,int> um(100);
  cout<<um.bucket_count()<<" "<<um.size()<<endl;
  for(unsigned i = 0 ; i < 100 ; i++){
    ostringstream o;
    o<<i;
    um[o.str()] = i;
    cout<<um.bucket_count()<<" "<<um.size()<<endl;
  }
  
  // um["hello"] = 5;
  // um["world"] = 6;
  // um["my"] = -3;
  // um["name"] = 6;
  // um["is"] = 8;
  // um["john"] = 1;


  // //  cout<<um.bucket_count()<<endl;

  // hash<string> h;

  // for(unsigned i = 0 ; i < um.bucket_count() ; i++){
  //   cout<<"bucket "<<i<<endl;
  //   for(unordered_map<string,int>::local_iterator iter = um.begin(i) ; 
  //       iter != um.end(i) ; 
  //       iter++){
  //     cout<<iter->first<<" "<<iter->second<<"("<<h(iter->first)<<")"<<endl;
  //   }
  //   cout<<"----------"<<endl;
  // }
}
