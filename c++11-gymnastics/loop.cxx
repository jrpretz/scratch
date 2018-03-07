#include <vector>
#include <iostream>

using namespace std;

class Data{
 public:
  Data() {data = 0.; cout<<"Creating a Data"<<endl;}
  Data(const Data& d) : data(d.data){cout<<"Copying a Data"<<endl;}
  ~Data(){cout<<"Deleting a Data"<<endl;}
  int data;
};

int main(){
 int max = 3;
 cout<<"**first by reference**"<<endl;
 {
  vector<Data> v(max);
  for(int i = 0 ; i < max ; i++)
    v[i].data = i;
  for(Data& d : v)
    cout<<d.data<<endl;
 }
 cout<<"**now by value**\n"<<endl;
 {
  vector<Data> v(max);
  for(int i = 0 ; i < max ; i++)
    v[i].data = i;
  for(Data d : v)
    cout<<d.data<<endl;
 }
}

