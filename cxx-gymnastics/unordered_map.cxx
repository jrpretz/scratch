#include <tr1/unordered_map>
#include <string>
#include <iostream>
#include <map>

struct bin{
  bin(int fbinIn,int ebinIn) : fbin(fbinIn),ebin(ebinIn){}
  int fbin;
  int ebin;

};

bool operator<(const bin& lhs,const bin& rhs){
  if(lhs.fbin < rhs.fbin)
    return true;
  if(lhs.fbin > rhs.fbin)
    return false;
  if(lhs.ebin < rhs.ebin)
    return true;
  return false;
}

bool operator==(const bin& lhs,const bin& rhs){
  return (lhs.fbin == rhs.fbin) && (lhs.ebin == rhs.ebin);
}

struct hash_X{
  size_t operator()(const bin &x) const{
    return std::tr1::hash<int>()(x.fbin) ^ std::tr1::hash<int>()(x.ebin);
  }
};

int main(){
  std::tr1::unordered_map<bin, int,hash_X> m;
  m[bin(0,0)] = 5;
  std::cout<<m[bin(0,0)]<<std::endl;

}
