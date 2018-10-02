import std.stdio;
import std.concurrency;
import core.thread;

class MyClass{
    this(int id, double x_start){
    id_ = id;
    x_ =     x_start;
  }

  void iterate(){
    x_ = x_ * x_ -2;
  }

  int id_;
  double x_;
}

void fun(int id){
  MyClass mc = new MyClass(id,0.2 + id * 0.01);
  foreach(i ; 0 .. 100)
    mc.iterate();
  writeln(id," ",mc.x_);
}

int main(){
  foreach(i ; 0 .. 10){
    spawn(&fun,i);
  }
  return 0;
}
