import std.random;
import std.stdio;
import std.concurrency;

import core.thread;

import core.atomic;

  shared int ncalls;

void print_thread(int thread){

  foreach(i; 1..10){
    Thread.sleep(dur!("msecs")( 50 ));
    writeln(ncalls," ",thread," ",uniform01());
    core.atomic.atomicOp!"+="(ncalls, 1);
  }
}

int main(){

  writeln(uniform01());

  foreach(i ;1..10)
    spawn(&print_thread,i);

  return 0;
}
