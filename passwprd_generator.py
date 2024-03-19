#importing secrets as it provides more security 
import secrets as se
import string as s

l = int(input("Enter the length for the password: "))
ch = s.ascii_letters + s.digits + s.punctuation
p = ''.join(se.choice(ch) for i in range(l))
print(f"The password generated is: {p}")

