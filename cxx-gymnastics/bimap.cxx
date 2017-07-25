#include <boost/bimap.hpp>

#include <iostream>

using namespace std;

int main(){
  boost::bimap<int,int> mapping;
  mapping.insert(boost::bimap<int,int>::value_type(3,4));
  mapping.insert(boost::bimap<int,int>::value_type(4,5));
  mapping.insert(boost::bimap<int,int>::value_type(7,11));


  for(boost::bimap<int,int>::const_iterator iter = mapping.begin();
      iter != mapping.end() ; 
      iter++){
    cout<<iter->left<<" "<<iter->right<<endl;
  }
  cout<<"------"<<endl;
  for(boost::bimap<int,int>::left_const_iterator iter = mapping.left.begin();
      iter != mapping.left.end() ; 
      iter++){
    cout<<iter->first<<" "<<iter->second<<endl;
  }
  cout<<"------"<<endl;
  for(boost::bimap<int,int>::right_const_iterator iter = mapping.right.begin();
      iter != mapping.right.end() ; 
      iter++){
    cout<<iter->first<<" "<<iter->second<<endl;
  }

}
