


int main(){
  import std.stdio;

  int i = 0;
  {
    scope(exit) i = 0;
    i++;
    i++;
    i++;
  }
  writeln(i);
  return 0;
}
