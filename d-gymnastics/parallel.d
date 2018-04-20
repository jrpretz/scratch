// from https://en.wikipedia.org/wiki/D_(programming_language)

import std.stdio : writeln;
import std.range : iota;
import std.parallelism : parallel;

void main(){
  foreach (i; iota(11).parallel) {
    // The body of the foreach loop is executed in parallel for each i
    writeln("processing ", i);
  }
}
