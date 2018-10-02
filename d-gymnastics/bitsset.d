uint bitsSet(uint value){
  uint result;
  for(;value;++result){
    value &= value -1;
  }
  return result;
}

int main(){
  import std.stdio;
  writeln(43," ",bitsSet(43));
  return 0;
}
