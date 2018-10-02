import std.stdio;
import std.conv;

int main(){
  {
    int i = 56;
    
    string j = to!string(i);
    
    const char[] k = j;
    
    writeln(k[0],k[1]);
    writeln(j[0],j[1]);
  }

  {
    uint l = uint.max;
    writeln(l);
    
    int m = l;
    writeln(m);
  }

  {
    int x = 1;
    foreach(i ; 0 .. 40){
      writeln(x);
      x = x << 1;
    }
    
  }
  
  return 0;
}   
