cmake_minimum_required(VERSION 3.16)
project(scratch_cpp)

set(CMAKE_CXX_STANDARD 14)

add_executable(test_random_gamma_generation test_random_gamma_generation.cpp)
add_executable(numerical_recipes_fft numerical_recipes_fft.cpp)
add_executable(scratch scratch.cpp)

list(APPEND CMAKE_PREFIX_PATH $ENV{ROOTSYS}/cmake)
find_package(ROOT REQUIRED)
add_executable(test_root_cern test_root_cern.cpp)
target_include_directories(test_root_cern PRIVATE ${ROOT_INCLUDE_DIRS})
target_link_directories(test_root_cern PRIVATE ${ROOT_LIBRARY_DIR})
target_link_libraries(test_root_cern PRIVATE ${ROOT_LIBRARIES})
if (WIN32)
    target_compile_definitions(test_root_cern PUBLIC -D_WIN32)
endif (WIN32)
