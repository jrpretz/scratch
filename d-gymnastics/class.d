import std.stdio;
import std.math;

class MyClass{
  double x;
  double y;

  this(){
    writef("creating an instance of MyClass with default constructor\n");
    x = 0;
    y = 0;
  }

  this(double xin,double yin){
    writef("creating an instance of MyClass with x=%f,y=%f\n",xin,yin);
    x = xin;
    y = yin;
  }

  ~this(){
    writef("destroying and instance of MyClass with x=%f,y=%f\n",x,y);
  }

  double distance(){
    return sqrt(x*x + y*y);
  }
};

void print_distance(MyClass instance){
  writef("%f\n",instance.distance());
}

// pass by reference
void reset_MyClass(MyClass instance){
  instance.x = 0;
  instance.y = 0;
}

void main(){
  {
    MyClass null_instance;
    if(null_instance is null){
      writef("null_instance is null\n");
    }
    else{
      writef("null_instance ain't null\n");
    }
  }

  {
    MyClass default_instance = new MyClass();
    if(default_instance is null)
      writef("error.... default_instance is null");
    default_instance.destroy(); // force destructor

    default_instance = null;
    if(default_instance is null)
      writef("good.... default_instance is now null\n");


  }

  {
    MyClass instance = new MyClass(3,4);
    print_distance(instance);
    reset_MyClass(instance);
    writef("%f\n",instance.distance());
  }


}
