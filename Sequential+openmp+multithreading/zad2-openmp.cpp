#include <iostream>
#include <chrono>
#include <omp.h>
#include "functions.h"

double sampling_variance_openmp(int observations[], int size) {
    using namespace std::chrono_literals;
    double sum_of_squares_el = 0;
    double sum_of_el = 0;

    #pragma omp parallel for reduction(+: sum_of_squares_el, sum_of_el)
    for (int i = 0; i < size; i++) {
        sum_of_squares_el += observations[i] * observations[i];
        sum_of_el += observations[i];
    }

    return (sum_of_squares_el / size) - ((sum_of_el * sum_of_el) / (size * size));
}