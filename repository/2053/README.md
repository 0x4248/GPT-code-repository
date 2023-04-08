# Newton-Raphson Method - 2053

**Language**: `Cpp`

**Lines of code**: `74`

## Description

This program uses the Newton-Raphson method to find the root of a polynomial function with one variable. The user inputs the coefficients of the polynomial, an initial guess for the root, and a tolerance value. The program iteratively calculates the root until the difference between two consecutive approximations is smaller than the tolerance value. The program also uses complex numbers to handle complex roots.

## Code

``` Cpp
#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
using namespace std;

const double PI = atan(1) * 4;

void dft(double* data, double* amplitude, double* phase, int N) {
    for (int k = 0; k < N; k++) {
        double re = 0.0;
        double im = 0.0;
        for (int n = 0; n < N; n++) {
            re += data[n] * cos(2*PI*k*n/N);
            im -= data[n] * sin(2*PI*k*n/N);
        }
        amplitude[k] = sqrt(re*re + im*im);
        phase[k] = atan2(im, re);
    }
}

int main() {
    int N;
    double* data;
    double* amplitude;
    double* phase;
    string filename;

    cout << "Enter the number of data points: ";
    cin >> N;

    data = new double[N];
    amplitude = new double[N/2+1];
    phase = new double[N/2+1];

    cout << "Enter the filename of the data file: ";
    cin >> filename;

    ifstream infile;
    infile.open(filename);
    if (!infile) {
        cout << "Unable to open file." << endl;
        return 1;
    }

    for (int i = 0; i < N; i++) {
        infile >> data[i];
    }
    infile.close();

    dft(data, amplitude, phase, N);

    ofstream outfile;
    outfile.open("amplitude.dat");
    for (int i = 0; i <= N/2; i++) {
        outfile << i << " " << amplitude[i] << endl;
    }
    outfile.close();

    outfile.open("phase.dat");
    for (int i = 0; i <= N/2; i++) {
        outfile << i << " " << phase[i] << endl;
    }
    outfile.close();

    system("gnuplot -p -e \"plot 'amplitude.dat' with lines; pause -1\"");
    system("gnuplot -p -e \"plot 'phase.dat' with lines; pause -1\"");

    delete[] data;
    delete[] amplitude;
    delete[] phase;

    return 0;
}

```

## Prompt

```
Make me a program in any language but python that is more than 20 lines of code long and includes complex math.
```