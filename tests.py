import sys
sys.path.append('/Users/david.rodval74/AI-Agent/functions')

from functions.second_function import write_file
from functions.run_python import run_python_file

def run_tests():
    # Test 1: Write to "lorem.txt" in the "calculator" directory
    working_directory = "calculator"
    file_path = "lorem.txt"
    content = "wait, this isn't lorem ipsum"
    result = write_file(working_directory, file_path, content)
    print("Result for 'lorem.txt':")
    print(result)

    # Test 2: Write to "pkg/morelorem.txt" in the "calculator/pkg" directory
    file_path = "pkg/morelorem.txt"
    content = "lorem ipsum dolor sit amet"
    result = write_file(working_directory, file_path, content)
    print("\nResult for 'pkg/morelorem.txt':")
    print(result)

    # Test 3: Attempt to write to "/tmp/temp.txt" outside the "calculator" directory
    file_path = "/tmp/temp.txt"
    content = "this should not be allowed"
    result = write_file(working_directory, file_path, content)
    print("\nResult for '/tmp/temp.txt':")
    print(result)


print("\nTest: main.py")
result = run_python_file("calculator", "main.py")
print(result)

print("\nTest: tests.py")
result = run_python_file("calculator", "tests.py")
print(result)

print("\nTest: ../main.py (should error)")
result = run_python_file("calculator", "../main.py")
print(result)

print("\nTest: nonexistent.py (should error)")
result = run_python_file("calculator", "nonexistent.py")
print(result)


if __name__ == "__main__":
    run_tests()

