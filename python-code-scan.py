# Unnecessary use of global variables (Code Smells)
global_var = 10

def some_function():
  # Code here doesn't use global_var
  pass

# Hardcoded literals (Code Smells)
magic_number = 42
if x == magic_number:
  # Do something

# Unused variables (Code Smells)
unused_var = "This variable has no purpose"

# Unclosed file (Potential Resource Leak)
with open("myfile.txt") as f:
  # Process some lines from the file

# Unnecessary string concatenation (Potential Performance Issues)
name = "John"
greeting = "Hello, " + name + "!"  # Less efficient than string formatting

print("SonarQube might identify these potential issues!")
