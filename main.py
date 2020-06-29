#   make a tauple that contains a predefined list that will replace character
SECURE = (('a', '@'), ('A', '@'), ('e', '3'), ('E', '3'), ('i', '!'),
          ('I', '!'), ('m', 'w'), ('M', 'W'), ('o', '0'), ('O', '0'), ('s', '$'), ('S', '$'), ('and', '&'), ('And', '&'), ('AND', '&'))


#   make a function that will return secure password
#   this function take existing password as a input
#   replace existing password character with predefined set of character
def generateSecurePassword(existingPassword):
    #   a = tauple first character
    #   b = tauple second character
    for a, b in SECURE:
        #   replace() is used to replace a with b
        existingPassword = existingPassword.replace(a, b)
    #   return replaced character
    return existingPassword


if __name__ == "__main__":
    #   take existing password as input
    existingPassword = input("Enter Your Existing Password: ")

    #   call generateSecurePassword function with existingPassword
    existingPassword = generateSecurePassword(existingPassword)

    #   print secure password
    print(f"Your Secured Password is: {existingPassword}")
