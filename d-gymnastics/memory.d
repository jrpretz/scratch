import std.stdio;

class WasteData{
  this(){
    write("creating a WasteData\n");
  }
  ~this(){
    write("deleting a WasteData\n");
  }

  uint[10000] data;
};

void main(){
  for(uint i = 0 ; i < 10000; i++){
    WasteData wd = new WasteData();
    writef("%d\n",i);
  }
}
