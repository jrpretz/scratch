import std.stdio;

class Foobar{
  static int a;
  static int b;
  static int c;
  static this(){
    writeln("Foobar static");
    a = 0;
    b = 1;
    c = 2;
  }


};

void main(){
    writeln("Entering main");
    writeln(Foobar.a,' ',Foobar.b,' ',Foobar.c);

}
