import std.stdio;
import std.concurrency;
import core.thread;

void writer(){
  for(; ;){
    auto msg = receiveOnly!(Tid,int)();
    writeln("Secondary thread: ",msg[1]);
    msg[0].send(thisTid);
  }
}

int main(){
  auto low = 0;
  auto high = 100;
  auto tid = spawn(&writer);
  foreach(i; low .. high){
    writeln("Main thread: ",i);
    tid.send(thisTid,i);
    writeln(receiveOnly!Tid() , tid);

    Thread.sleep(dur!("msecs")( 50 ));
  }
  return 0;
}
