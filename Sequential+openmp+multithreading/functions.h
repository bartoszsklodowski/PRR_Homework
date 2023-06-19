// functions.h

#ifndef FUNCTIONS_H
#define FUNCTIONS_H

double sampling_variance_seq(int observations[], int size);
double sampling_variance_openmp(int observations[], int size);
double sampling_variance_multithreaded(int observations[], int size);

#endif
