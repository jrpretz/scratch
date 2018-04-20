import std.stdio;
import std.complex;

void main(){
  {
    bool b = false;
    b = true;
    writef("bool: %d\n",b);
  }

  {
    byte b = 0xC;
    writef("byte: %d\n",b);
    writef("byte: %x\n",b);
  }

  {
    double d = 3.14159;
    writef("double: %f\n",d);

    double d2;
    writef("double: %f\n",d2);
  }

  {
    double[5] double_array = [1,2,3,4,5];
    writef("double array: [");
    foreach(double d ; double_array){
      writef(" %f",d);
    }
    writef("]\n");
  }

  {
    auto id = complex(3,4);
    writef("%g\n",id);
    writef("%f + %fi\n",id.re,id.im);

  }
}
