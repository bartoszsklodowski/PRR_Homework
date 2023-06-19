#include <iostream>
#include <thread>
#include <vector>
#include <mutex>

double sum_of_squares_el = 0;
double sum_of_el = 0;
std::mutex mtx;

void compute_partial_sum(int observations[], int start, int end) {
    double partial_sum_of_squares_el = 0;
    double partial_sum_of_el = 0;

    for (int i = start; i < end; i++) {
        partial_sum_of_squares_el += observations[i] * observations[i];
        partial_sum_of_el += observations[i];
    }

    std::lock_guard<std::mutex> lock(mtx);
    sum_of_squares_el += partial_sum_of_squares_el;
    sum_of_el += partial_sum_of_el;
}

double sampling_variance_multithreaded(int observations[], int size) {
    const int num_threads = std::thread::hardware_concurrency();
    std::vector<std::thread> threads;
    const int chunk_size = size / num_threads;
    int start = 0;
    int end = 0;

    for (int i = 0; i < num_threads; i++) {
        start = i * chunk_size;
        end = (i == num_threads - 1) ? size : start + chunk_size;
        threads.emplace_back(compute_partial_sum, observations, start, end);
    }

    for (auto& thread : threads) {
        thread.join();
    }

    return (sum_of_squares_el / size) - ((sum_of_el * sum_of_el) / (size * size));
}

