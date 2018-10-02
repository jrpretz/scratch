import std.stdio;

void whatType(T)(T t){
  writeln(__PRETTY_FUNCTION__);
}

int main(){
  auto f = File("data.txt", "r");

  foreach(line ; f.byLine()){
    writeln(line);
    whatType(line);
  }

  return 0;
}
