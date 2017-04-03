#include <iostream>
#include <cstdlib>

using namespace std;

template <class T>
class GenericMatrix{
public:
  GenericMatrix(unsigned rows, unsigned columns) : 
    rows_(rows), 
    columns_(columns){
    data_ = (double*)(malloc(sizeof(T) * rows* columns));
  }
  
  double* operator[](unsigned row){
    return data_ + columns_ * row;
  }
  
  ~GenericMatrix(){
    free(data_);
  }

private:
  T* data_;
  unsigned columns_;
  unsigned rows_;
};

typedef GenericMatrix<double> Matrix;



int main(){

  
}
