import std.stdio;

void set_zero(int i){
  i = 0;	  
}

void set_zero(int* i){
  *i = 0;	  
}


void main(){
  int i = 5;
  set_zero(i);
  writef("%d\n",i);

  set_zero(&i);
  writef("%d\n",i);

}
