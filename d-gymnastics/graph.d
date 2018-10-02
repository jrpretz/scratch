import std.stdio;

struct Node{
  int id;
  int[] parents;
  
  this(int id_in, int[] parents_in){
    id = id_in;
    parents = parents_in;
  }
}

int main(){
  Node[] nodes;
  //  Node n = new Node(0,[]);
  nodes ~= [ Node(0,[])];
  nodes ~= [ Node(1,[0])];
  nodes ~= [ Node(2,[0,1])];
  nodes ~= [ Node(3,[0])];
  nodes ~= [ Node(4,[])];
  nodes ~= [ Node(5,[3,4])];
  nodes ~= [ Node(6,[5])];
  nodes ~= [ Node(7,[6])];
  nodes ~= [ Node(8,[7,2])];

  writeln("digraph G{");
  foreach(n ; nodes){
    //    writeln(n.id);

    foreach(p ; n.parents){
      writeln(p," -> ",n.id,";");
    }
  }
  writeln("}");
  
  return 0;
}
