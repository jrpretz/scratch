import std.stdio;

immutable int pi = 3;
const int pibar = -3;

class MyClass{
  this(int x_in, int y_in){
    x = x_in;
    y = y_in;
  }

  pure @nogc int sum(int z) const{
    return x + y + z + pi + pibar;
  }

  pure setX(const int x_in) {
    x = x_in;
  }

  int x;
  int y;

}


int main(){
  const MyClass mc = new MyClass(4,-2);

  //mc.setX(89);
  
  writeln(mc.sum(6));


  return 0;
}
