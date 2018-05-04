import std.stdio;

class Square(int n){
  int getValue(){
    return n*n;
  }

  int value = n*n;
}

void main(){
  auto sq = new Square!(10);
  writeln(sq.getValue());
  writeln(sq.value);
  
}
