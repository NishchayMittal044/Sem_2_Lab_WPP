# Write a class called Password_manager. The class should have a list called old_passwords that
# holds all of the user’s past passwords. The last item of the list is the user’s current pass word.
# There should be a method called get_password that returns the current password and a method
# called set_password that sets the user’s password. The set_password method should only
# change the password if the attempted password is different from all the user’s past passwords.
# Finally, create a method called is_correct that receives a string and returns a boolean True or
# False depending on whether the string is equal to the current password or not.

class PasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        """Returns the current password."""
        if self.old_passwords:
            return self.old_passwords[-1]
        else:
            None

    def set_password(self, new_password):
        """Sets a new password if it has never been used before."""
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False

    def is_correct(self, password):
        """Checks if the given password matches the current password."""
        return password == self.get_password()

# Example usage
pm = PasswordManager()
pm.set_password("password123")
print(pm.get_password())  # Output: password123
print(pm.is_correct("password123"))  # Output: True
print(pm.set_password("password123"))  # Output: False (Already used)
print(pm.set_password("newpassword456"))  # Output: True
