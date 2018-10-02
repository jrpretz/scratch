import std.concurrency;

shared class MyData{
  int x;
  int y;
  string message;

  this(){x = 1 ; y = -1 ; message="hello world";}
}

shared MyData my_data;

void foo(){
}

int main(){
  //MyData mine = new MyData();
  //  my_data = cast!(shared MyData)(mine);
  my_data = new MyData();
  spawn(&foo);
  
  return 0;
}
