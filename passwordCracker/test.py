import hashlib

password = "test124";
hash_fn = hashlib.md5;
hashed = hash_fn(password.encode()).hexdigest();

print(f"The password is : {hashed}");


with open("wordlist.txt", "w") as f:
 f.write("pass1\npass2\npass3\n") 
with open("wordlist.txt", "r") as f:
 passwords = [line.strip() for line in f.readlines()]
 print("Loaded passwords:",passwords)