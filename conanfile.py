import os
import shutil

from conans import CMake, ConanFile, tools


class BenchmarkConan(ConanFile):
    name = "benchmark"
    version = "1.4.1"
    license = "MIT License"
    url = "https://github.com/AtaLuZiK/conan-benchmark"
    description = "A library to support the benchmarking of functions, similar to unit-tests."
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "enable_exceptions": [True, False], # Enable the use of exceptions in the benchmark library.
        "enable_lto": [True, False],        # Enable link time optimisation of the benchmark library.
        "use_libcxx": [True, False],        # Build and test using libc++ as the standard library.
    }
    default_options = (
        "enable_exceptions=True", 
        "enable_lto=False",
        "use_libcxx=False",
    )
    exports_sources = ["benchmark-config.cmake"]
    generators = "cmake"

    @property
    def zip_folder_name(self):
        return "%s-%s" % (self.name, self.version)

    def source(self):
        zip_name = "%s.tar.gz" % self.version
        tools.download("https://github.com/google/benchmark/archive/v%s" % zip_name, zip_name)
        tools.check_md5(zip_name, "482dddb22bec43f5507a000456d6bb88")
        tools.unzip(zip_name)
        os.unlink(zip_name)
        with tools.chdir(self.zip_folder_name):
            tools.replace_in_file('CMakeLists.txt', 'project (benchmark)', '''project (benchmark)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BENCHMARK_ENABLE_TESTING"] = "OFF"
        cmake.definitions["BENCHMARK_ENABLE_EXCEPTIONS"] = "ON" if self.options.enable_exceptions else "OFF"
        cmake.definitions["BENCHMARK_ENABLE_LTO"] = "ON" if self.options.enable_lto else "OFF"
        cmake.definitions["BENCHMARK_USE_LIBCXX"] = "ON" if self.options.use_libcxx else "OFF"
        cmake.definitions["BENCHMARK_ENABLE_INSTALL"] = "OFF"
        cmake.definitions["BENCHMARK_ENABLE_GTEST_TESTS"] = "OFF"
        cmake.configure(source_dir=self.zip_folder_name)
        cmake.build()

    def package(self):
        source_dir = self.zip_folder_name
        self.copy("benchmark-config.cmake", ".", ".")
        self.copy("*.h", dst="include", src=source_dir + '/include')
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["benchmark"]
        if self.settings.os == "Windows":
            self.cpp_info.libs.append("shlwapi")
