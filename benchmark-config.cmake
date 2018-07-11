message(STATUS "${CONAN_LIB_DIRS_BENCHMARK}")

find_path(BENCHMARK_INCLUDE_DIR NAMES benchmark/benchmark.h PATHS ${CONAN_INCLUDE_DIRS_BENCHMARK})
find_library(BENCHMARK_LIBRARY NAMES benchmark PATHS ${CONAN_BUILD_DIRS_BENCHMARK})

set(BENCHMARK_INCLUDE_DIRS ${BENCHMARK_INCLUDE_DIR})
set(BENCHMARK_LIBRARIES ${CONAN_LIBS_BENCHMARK})
set(BENCHMARK_MAIN_LIBRARIES benchmark_main ${BENCHMARK_LIBRARIES})

add_library(benchmark INTERFACE IMPORTED)
target_include_directories(benchmark
  INTERFACE ${BENCHMARK_INCLUDE_DIRS}
)
target_link_libraries(benchmark
  INTERFACE ${BENCHMARK_LIBRARIES}
)

add_library(benchmark_main INTERFACE IMPORTED)
target_include_directories(benchmark_main
  INTERFACE ${BENCHMARK_INCLUDE_DIRS}
)
target_link_libraries(benchmark_main
  INTERFACE ${BENCHMARK_MAIN_LIBRARIES}
)

mark_as_advanced(BENCHMARK_LIBRARY BENCHMARK_INCLUDE_DIR)

message("** benchmark found by Conan!")
set(BENCHMARK_FOUND TRUE)
message("   - includes: ${BENCHMARK_INCLUDE_DIRS}")
message("   - libraries: ${CONAN_LIBS_BENCHMARK}")
