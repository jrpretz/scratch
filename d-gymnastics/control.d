import std.stdio;


void main(){
  // basic for loop
  for(int i = 0 ; i < 7 ; i++){
    writef("%d ",i);
  }
  writef("\n");

  // while loop
  int j = 0;
  while(j < 7){
    writef("%d ",j);
    j++;
  }
  writef("\n");

  // foreach
  int[7] arr = [0,1,2,3,4,5,6];  
  foreach(int val ; arr){
    writef("%d ",val);
  }
  writef("\n");


  // for each over a range
  foreach(int i ; 0..7){
    writef("%d ",i);
  }
  writef("\n");
}
