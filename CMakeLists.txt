cmake_minimum_required(VERSION 3.8)

project(CppNumericalSolvers)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
endif()
set(buildTypeMsg "Choose the type of build, options are: Debug (default), Release, RelWithDebInfo, MinSizeRel.")
set(CMAKE_BUILD_TYPE ${CMAKE_BUILD_TYPE} CACHE STRING ${buildTypeMsg} FORCE)
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")

if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME) # !IsSubmodule()
    message(STATUS "Top Level Build")
else()
    message(STATUS "Submodule Build")
endif()

include(importCMakeUtility.cmake)

include_directories(${PROJECT_SOURCE_DIR}/include)
