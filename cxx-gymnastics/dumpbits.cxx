#include <inttypes.h>
#include <iostream>
#include <cstdio>

using namespace std;

template <class T>
string dumpbits(T t){
  string bits(sizeof(T) * 8,'0');
  for(unsigned i = 0 ; i < sizeof(T) * 8 ; i++){
    unsigned offset = sizeof(T) * 8 -1 - i;
    T bit = (t >> offset) & 1;
    if(bit == 1)
      bits[i] = '1';
  }

  return bits;
}

int main(){


  // uint32_t a = 4;
  // cout<<(a)<<endl;
  // cout<<(a<<1)<<endl;
  // cout<<(a>>1)<<endl;
  // cout<<(a>>2)<<endl;
  //  uint32_t a = 4;

  //  cout<<dumpbits(a)<<endl;

  for(int8_t i = -100 ; i < 100 ; i++){
    printf("%04d %s\n",i,dumpbits(i).c_str());
  }
}
