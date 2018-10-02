import std.stdio;

import std.random;
import std.stdio;
import std.concurrency;

import core.thread;

import core.atomic;


shared int terminate;

void compute(int threadNo,int period){
  writeln("compute ",threadNo," starting");
  while(true){
    writeln("sleeping thread ",threadNo);
    Thread.sleep(dur!("msecs")(period));
    if(terminate){
      writeln("terminating thread ",threadNo);
      return;
    }
  }
}

void main(){
  writeln(terminate);

  int[int] numbersAndPeriods;
  numbersAndPeriods[1] = 223;
  numbersAndPeriods[2] = 750;
  numbersAndPeriods[3] = 1000;
  numbersAndPeriods[4] = 9837;

  foreach(num,period ; numbersAndPeriods){
    spawn(&compute,num,period);
  }
  
  while(true){
    double rnd = uniform01();
    writeln("main thread:",rnd);
    if(rnd < 0.1){
      writeln("terminate threads!!");
      terminate = 1;
      break;
      //core.atomic.atomicOp!"+="(terminate, 1);
    }
    Thread.sleep(dur!("msecs")(1000));
  }
}
