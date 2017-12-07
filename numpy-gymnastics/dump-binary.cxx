#include <cstdio>
#include <cmath>

using namespace std;

int main(){
  FILE* outfile = fopen("data.dat","w");

  for(int i = 0 ; i < 100 ; i++){
    double f = ((double)i) * 6.28 / 100.;
    double s = sin(f);
    double c = cos(f);
    double t = tan(f);
    fwrite(&f,sizeof(double),1,outfile);
    fwrite(&s,sizeof(double),1,outfile);
    fwrite(&c,sizeof(double),1,outfile);
    fwrite(&t,sizeof(double),1,outfile);
  }
}
