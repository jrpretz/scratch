#include <stdint.h>

template <class T>
T endian_swap(T t){
  T toReturn = 0;
  for(unsigned i = 0 ; i < sizeof(T) ; i++)
    {
      T shifted = t >> ((sizeof(T) - (i + 1)) * 8) & 0xFF;
      shifted = shifted << (i * 8);
      toReturn = toReturn | shifted;
    }
  return toReturn;
}

#include <iostream>

using namespace std;

int main(){
  uint32_t x = 5;
  cout<<x<<" "<<endian_swap(x)<<endl;
}
