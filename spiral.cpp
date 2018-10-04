#include <iostream>
using namespace std;

bool IsPrintingPoint( int x, int y, int rows ) {
  //quick check
  if( (y == 0) || (y == rows -1)) return true;

  //TODO: here comes your logic for deciding what to print

  return false;
}


int main(){
  int input;
  cin>>input;
  for( int y = 0; y < input; y++ ) {
    for( int x = 0; x < input; x++ ) {
      bool result = IsPrintingPoint(x,y, input);
      printf( result ? " " : "* ");
    }
    printf("\n");
  }

  return 0 ;

}
