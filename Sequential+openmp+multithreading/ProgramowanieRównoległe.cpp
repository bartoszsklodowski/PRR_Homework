// ProgramowanieRównoległe.cpp : Ten plik zawiera funkcję „main”. W nim rozpoczyna się i kończy wykonywanie programu.
//

#include <iostream>
#include <chrono>
#include "functions.h"

using namespace std;


void execution_time(double (*function)(int[], int), int observations[], int size) {
    using std::chrono::high_resolution_clock;
    using std::chrono::duration;
    auto t1 = high_resolution_clock::now();
    std::cout << function(observations, size) << std::endl;
    auto t2 = high_resolution_clock::now();

    duration<double, std::milli> ms_double = t2 - t1;
    std::cout << ms_double.count() << "ms\n";

}

int main()
{

    const int size = 1500;
    int observations[size];

    #pragma omp parallel for
    for (int i = 0; i < size; i++) {
        observations[i] = i + 1;
    }

    execution_time(sampling_variance_seq, observations, size);
    execution_time(sampling_variance_openmp, observations, size);
    execution_time(sampling_variance_multithreaded, observations, size);
    

    return 0;

}

