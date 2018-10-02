import std.stdio;
import std.conv;

template GenStruct(string Name, string M1)
{
    const char[] GenStruct = "struct " ~ Name ~ "{ int " ~ M1 ~ "; }";
}

mixin(GenStruct!("Foo", "bar"));

template myfunc(string name){
  const char[] myfunc = "string " ~ name ~ "(){return \"" ~ name ~ "\";}";
}

mixin(myfunc!("foobar"));

int main(){
  //  writeln(__PRETTY_FUNCTION__);
  //  writeln(myfunc!("foobar",34));
  writeln(foobar());
  writeln(to!string(34));
  return 0;
}
