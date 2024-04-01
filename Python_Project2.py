def validate_password(password, username, old_passwords):
  # Check the minimum length
  if len(password) < 10:
      return "Password must be at least 10 characters long."

  # Check for character variety
  uppercase, lowercase, digits, special_chars = 0, 0, 0, 0
  for char in password:
      if char.isupper():
          uppercase += 1
      elif char.islower():
          lowercase += 1
      elif char.isdigit():
          digits += 1
      elif char in '@#$%&*!':
          special_chars += 1

  if uppercase < 2 or lowercase < 2 or digits < 2 or special_chars < 2:
      return "Password must contain at least two uppercase letters, two lowercase letters, two digits, and two special characters (@, #, $, %, &, *, !)."

  # Check for sequence and repetition restrictions
  for i in range(len(username) - 2):
      if username[i:i+3].lower() in password.lower():
          return "Password should not contain sequences of three or more consecutive characters from the username."
  for i in range(len(password) - 3):
      if password[i] == password[i+1] == password[i+2] == password[i+3]:
          return "No character should repeat more than three times in a row."

  # Historical password check
  if password in old_passwords:
      return "The new password must not be the same as the last three passwords used."

  # If all checks pass
  return "Password is valid."

# Example usage:
username = "User123"
old_passwords = ["Pass@1234", "OldPass#12", "Recent$123"]

while True:
  password = input("Enter your password: ")
  feedback = validate_password(password, username, old_passwords)
  print(feedback)
  if feedback == "Password is valid.":
      break
