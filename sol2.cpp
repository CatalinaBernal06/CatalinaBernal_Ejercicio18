#include <iostream>

int main(){
  float y = 1;
  float x = 0;
  float z = 0;
  float h = 0.1;
  float N = 10/h;

  for(int i=0; i<N; i++){
    z = z - h*y;
    y = y + h*z;
    x = x+h;
    
    std::cout << x << " " << y << " " << z <<  std::endl;
  }
}
