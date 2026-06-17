subdomains = ["www","mail","api"];

with open("subdomain/file.txt","w") as f1:
    for sub in subdomains:
        f1.write(sub + "\n");
        
with open("subdomain/file.txt","r") as f2:
    l1 = f2.read().splitlines();
    print(l1);
    