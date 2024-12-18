cmake_minimum_required(VERSION 3.23)
project(adventofcode)

set(CMAKE_CXX_STANDARD 23)

file(GLOB SOURCE_FILES "${CMAKE_CURRENT_SOURCE_DIR}/day*.cpp")
add_executable(${CMAKE_PROJECT_NAME} main.cpp ${SOURCE_FILES} "${CMAKE_CURRENT_SOURCE_DIR}/adventofcode.h")

file(GLOB INPUT_FILES "${CMAKE_CURRENT_SOURCE_DIR}/day*.txt")
file(COPY ${INPUT_FILES} DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
