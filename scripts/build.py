#!/usr/bin/env python3
"""
Build and run CSES C++ solutions.

Usage:
    python build.py <file.cpp>            # compile
    python build.py <file.cpp> --run      # compile and run
    python build.py <file.cpp> --debug    # compile with sanitizers
    python build.py <file.cpp> --clean    # remove build output for this file
    python build.py --clean-all           # remove all build output

Examples (from any directory):
    python scripts/build.py 01_introductory_problems/01_weird_algorithm.cpp
    python scripts/build.py 01_weird_algorithm.cpp --run     # from within the problem dir
    python scripts/build.py 01_weird_algorithm --run         # .cpp extension is optional
"""

import argparse
import os
import shutil
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Compiler search order: prefer real GCC, fall back to system g++ (clang on macOS)
GCC_CANDIDATES = ["g++-14", "g++-13", "g++-12", "g++-11", "g++"]

COMMON_FLAGS = ["-std=c++17", "-O2", "-Wall", "-Wextra", "-pedantic", "-Wshadow",
                "-Wformat=2", "-Wfloat-equal", "-Wcast-qual", "-Wcast-align",
                "-Wno-unused-result", "-Wno-sign-conversion"]

GCC_ONLY_FLAGS = ["-Wlogical-op", "-Wshift-overflow=2", "-Wduplicated-cond"]

DEBUG_FLAGS = ["-fsanitize=address", "-fsanitize=undefined",
               "-fno-sanitize-recover=all", "-fstack-protector-all",
               "-D_GLIBCXX_DEBUG", "-D_GLIBCXX_DEBUG_PEDANTIC", "-g"]

GCC_DEBUG_FLAGS = ["-D_FORTIFY_SOURCE=2"]


def find_compiler(prefer_clang=False):
    """Find a C++ compiler. prefer_clang=True for debug builds on macOS
    where GCC lacks bundled sanitizer libraries."""
    if prefer_clang:
        for name in ["clang++", "g++"]:
            path = shutil.which(name)
            if path:
                return path, name
    for name in GCC_CANDIDATES:
        path = shutil.which(name)
        if path:
            return path, name
    print("Error: no C++ compiler found", file=sys.stderr)
    sys.exit(1)


def is_real_gcc(compiler_path):
    try:
        out = subprocess.check_output([compiler_path, "--version"],
                                      stderr=subprocess.STDOUT, text=True)
        return "GCC" in out and "clang" not in out.lower()
    except Exception:
        return False


def resolve_source(raw_path):
    """Find the .cpp file from a possibly incomplete path."""
    if not raw_path.endswith(".cpp"):
        raw_path += ".cpp"

    if os.path.isfile(raw_path):
        return os.path.abspath(raw_path)

    full = os.path.join(REPO_ROOT, raw_path)
    if os.path.isfile(full):
        return os.path.abspath(full)

    print(f"Error: cannot find source file '{raw_path}'", file=sys.stderr)
    sys.exit(1)


def build(source, debug=False):
    use_clang = debug and sys.platform == "darwin"
    compiler, name = find_compiler(prefer_clang=use_clang)
    gcc = is_real_gcc(compiler)

    stem = os.path.splitext(os.path.basename(source))[0]
    out_dir = os.path.join(REPO_ROOT, "output")
    os.makedirs(out_dir, exist_ok=True)
    binary = os.path.join(out_dir, stem)

    flags = list(COMMON_FLAGS)
    if gcc:
        flags.extend(GCC_ONLY_FLAGS)
    if debug:
        flags.extend(DEBUG_FLAGS)
        if gcc:
            flags.extend(GCC_DEBUG_FLAGS)

    cmd = [compiler] + flags + [source, "-o", binary]
    print(f"[build] {name} {os.path.basename(source)}" +
          (" (debug)" if debug else ""))
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(result.returncode)

    print(f"[build] -> {os.path.relpath(binary)}")
    return binary


def run(binary):
    print(f"[run]   {os.path.relpath(binary)}\n")
    result = subprocess.run([binary])
    sys.exit(result.returncode)


def clean(source):
    stem = os.path.splitext(os.path.basename(source))[0]
    binary = os.path.join(REPO_ROOT, "output", stem)
    if os.path.isfile(binary):
        os.remove(binary)
        print(f"[clean] removed {os.path.relpath(binary)}")
    else:
        print("[clean] nothing to clean")


def clean_all():
    out_dir = os.path.join(REPO_ROOT, "output")
    if os.path.isdir(out_dir):
        count = sum(1 for f in os.listdir(out_dir) if os.path.isfile(os.path.join(out_dir, f)))
        shutil.rmtree(out_dir)
        print(f"[clean] removed {count} file(s) from output/")
    else:
        print("[clean] nothing to clean")


def main():
    parser = argparse.ArgumentParser(
        description="Build and run CSES C++ solutions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("source", nargs="?", help="C++ source file (.cpp extension optional)")
    parser.add_argument("--run", "-r", action="store_true", help="run after building")
    parser.add_argument("--debug", "-d", action="store_true", help="enable sanitizers")
    parser.add_argument("--clean", "-c", action="store_true", help="remove build output for this file")
    parser.add_argument("--clean-all", action="store_true", help="remove all build output")
    args = parser.parse_args()

    if args.clean_all:
        clean_all()
        return

    if not args.source:
        parser.print_help()
        sys.exit(1)

    source = resolve_source(args.source)

    if args.clean:
        clean(source)
        return

    binary = build(source, debug=args.debug)

    if args.run:
        run(binary)


if __name__ == "__main__":
    main()
