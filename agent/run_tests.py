import subprocess

def run_tests(folder: str, test_class: str = "FruitTest") -> str:
    """Compiles all .java files in folder, then runs test_class.
    Returns combined output as text."""
    compile_result = subprocess.run(
        "javac *.java",
        cwd=folder, shell=True, capture_output=True, text=True
    )
    if compile_result.returncode != 0:
        return f"COMPILE ERROR:\n{compile_result.stdout}\n{compile_result.stderr}"

    run_result = subprocess.run(
        ["java", test_class],
        cwd=folder, capture_output=True, text=True, timeout=10
    )
    return f"STDOUT:\n{run_result.stdout}\nSTDERR:\n{run_result.stderr}"


if __name__ == "__main__":
    import sys
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    test_class = sys.argv[2] if len(sys.argv) > 2 else "FruitTest"
    print(run_tests(folder, test_class))