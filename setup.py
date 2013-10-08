import sys

from cx_Freeze import setup, Executable

base = "Win32GUI"

buildOptions = dict(
        compressed = True,
        includes = ["atexit"],
        path = sys.path)

setup(
        name = "Combinatorics",
        version = "1.0",
        author = "Bohdan Fedys",
        description = "Simple program for combination and permutation some sequence.",
        options = dict(build_exe = buildOptions),
        executables = [Executable(
            "main.py",
            base = base,
			targetName = "Combinatorics.exe", # otherwise will be controller.exe (same as script name)
        )]
)
