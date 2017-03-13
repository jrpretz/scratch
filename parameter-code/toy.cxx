#include "Parameter.h"

#include <vector>
#include <iostream>

using std::vector;
using std::cout;
using std::endl;

class TestClass{
  public:
    TestClass() : a_(0),b_(0),c_(0){}

    double getA() const{return a_;}
    double getB() const{return b_;}
    double getC() const{return c_;}
    void setA(double a){a_ = a;}
    void setB(double b){b_ = b;}
    void setC(double c){c_ = c;}

    vector<Parameter> getParameters(){
      vector<Parameter> parameters;
      Parameter pa(this,&TestClass::setA,&TestClass::getA,"a");
      parameters.push_back(pa);
      Parameter pb(this,&TestClass::setB,&TestClass::getB,"b");
      parameters.push_back(pb);
      Parameter pc(this,&TestClass::setC,&TestClass::getC,"c");
      parameters.push_back(pc);
      return parameters;
    }
  private:
    double a_;
    double b_;
    double c_;
};

int main(){
  TestClass tc;
  vector<Parameter> parameters = tc.getParameters();
  for(int i = 0 ; i < parameters.size() ; i++){
    cout<<"setting "<<parameters[i].name<<endl;
    parameters[i].setter(i);
  }
  for(int i = 0 ; i < parameters.size() ; i++){
    cout<<"getting "
	<<parameters[i].name
	<<":"
	<<parameters[i].getter()<<endl;;
  }

}
