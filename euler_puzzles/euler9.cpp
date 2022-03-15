#include <iostream>
#include <math.h>

using namespace std;

int sum_vals(int a,int b, int c){
    return a+b+c;
}

int check_pyth(int a, int b, int c){
    int s1 = pow(a,2) + pow(b,2);
    cout<<s1<<"\n";
    cout<<pow(c,2)<<"\n";
    if (s1 == pow(c,2)){
        return 1;
        }
    else {
        return 0;
        }
}

int main(void) {
//    cout<<"Something happened here\n";
    int a =3;
    int b=4 ;
    int break_loop=0;
    double c=5;
    cout<<"a ="<<a<<" b="<<b<<" c="<< c<<"\n";
    cout<<sum_vals(a,b,c)<<"\n";
    cout<<"Equal:"<<check_pyth(a,b,c)<<"\n";

    int val_squares[998][2];
    for (b=2; b<=998; b++){
        if (break_loop==0){
            for (a=1; a<b; a++){
                c = sqrt(pow(a,2) + pow(b,2));
                if (floor(c) == c){
                    if (a+b+c == 1000){
                        cout<<"a ="<<a<<" b="<<b<<" c="<< c<<" a+b+c "<<a+b+c<<"\n";
                        cout<<a*b*c;
                        break_loop=1;
                        break;
                    }
                }
            }
        }
    }
    cout<<"a ="<<a<<" b="<<b<<" c="<< c<<"\n";
    return 0;
}
