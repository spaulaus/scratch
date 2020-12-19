#include <chrono>
#include <iostream>
#include <fstream>
#include <random>
#include <tuple>
#include <vector>

int main(int argc, char** argv) {


    std::mt19937_64 generator(1337);
    std::discrete_distribution<int> distribution{4.18, 36, 3.63, 85.6, 79.9, 81.5, 64.9, 98.4, 85.1, 94, 99.86, 99.98,
                                                 99.4};
    std::vector<std::normal_distribution<double>> vals = {std::normal_distribution<double>(46.539, 0.46539),
                                                          std::normal_distribution<double>(59.5409, 0.595409),
                                                          std::normal_distribution<double>(88.0336, 0.880336),
                                                          std::normal_distribution<double>(122.06065, 1.2206065),
                                                          std::normal_distribution<double>(165.8575, 1.658575),
                                                          std::normal_distribution<double>(279.1952, 2.791952),
                                                          std::normal_distribution<double>(391.669, 3.91669),
                                                          std::normal_distribution<double>(514.0067, 5.140067),
                                                          std::normal_distribution<double>(661.657, 6.61657),
                                                          std::normal_distribution<double>(898.042, 8.98042),
                                                          std::normal_distribution<double>(1173.228, 11.73228),
                                                          std::normal_distribution<double>(1332.492, 13.32492),
                                                          std::normal_distribution<double>(1836.063, 18.36063),};
    std::ofstream file("source.txt", std::ios::out);
    for (unsigned int i = 0; i < 10000; i++) {
        file << vals[distribution(generator)](generator) << std::endl;
        std::cout << std::chrono::system_clock::now().time_since_epoch() / std::chrono::milliseconds(1) << std::endl;
    }
    file.close();
}