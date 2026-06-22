file = "passwords.txt";

import itertools

with open(file,"w") as f1:
    try:
        f1.write("sameer\nsameer123\nlol123");
    except FileExistsError:
        print("File already exists");
    except: 
        print("Error occurred while trying to open the file" , file);
        
with open(file,"r") as f1:
    try:
        l = f1.readlines();
        for line in l :
            print(line,end="");
    except FileNotFoundError:
        print("File not found");
    except:
        print("Error happened while reading a file")
        
def generate(chars,len):
    for combo in itertools.product(chars,repeat=len):
        yield " ".join(combo);
        
chars = "ab"
for word in generate(chars,2):
    print(word)

        
        
