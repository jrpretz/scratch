import std.stdio;

import std.random;
import std.stdio;
import std.concurrency;

import core.thread;

import core.atomic;


shared int globalCount;

void print_global_count(int threadNo,int period){
  int ncalls = 0;
  while(true){
    Thread.sleep(dur!("msecs")( period ));
    writeln(threadNo," ",ncalls," ",globalCount);
    ncalls += 1;
  }
}

void main(){
  writeln(globalCount);

  int[int] numbersAndPeriods;
  numbersAndPeriods[1] = 223;
  numbersAndPeriods[2] = 750;
  numbersAndPeriods[3] = 1000;
  numbersAndPeriods[4] = 9837;

  foreach(num,period ; numbersAndPeriods){
    spawn(&print_global_count,num,period);
  }
  while(true){
    core.atomic.atomicOp!"+="(globalCount, 1);
    Thread.sleep(dur!("msecs")(1000));
  }
}
