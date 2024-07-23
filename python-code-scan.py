# Unvalidated user input (SQL Injection Vulnerability)
username = input("Enter username: ")
password = "demo"

# Unsafe string formatting (SQL Injection Vulnerability)
connection = sqlite3.connect("users.db")
cursor = connection.cursor()
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"  # This is vulnerable
cursor.execute(query)
result = cursor.fetchone()

if result:
  print(f"Welcome back, {result[1]}!")  # Potential information disclosure
else:
  print("Login failed.")

connection.close()

# Hardcoded credentials (Security Misconfiguration)
API_KEY = "your_secret_api_key"  # Don't store sensitive information directly in code
def download_data(url):
  headers = {"Authorization": f"Token {API_KEY}"}
  # Download data using the headers

# Unhandled exceptions (Potential Denial-of-Service)
def process_data(data)
  try:
    # Process data here
  except Exception as e:
    print(f"An error occurred: {e}")  # This doesn't handle the exception gracefully and could crash the program

# Insecure direct file inclusion (Code Injection Vulnerability)
filename = input("Enter filename: ")
with open(filename) as f:
  # Process file contents here (This could execute malicious code if the filename is controlled by an attacker))

print("Done!")
