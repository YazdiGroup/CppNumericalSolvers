from conans import ConanFile


class CppNumericalSolversConan(ConanFile):
    name = "CppNumericalSolvers"
    version = "0.1"
    exports_sources = "include*"
    settings = "os", "compiler", "build_type", "arch"
    requires = ("eigen/3.3.9")
    generators = "cmake"
    no_copy_source = True

    def package(self):
        self.copy("*.h", dst="include", src="include")

    def package_info(self):
        self.info.header_only()
