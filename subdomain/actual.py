import requests,threading

discovered_subdomains = [];

def check_domain(subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        req = requests.get(url);
        if req.status_code == 404:
            raise Exception;
        else:
            print(f"got {url}");
            
    except Exception:
        print(f"Could not open the url : {url}")
        
domain = "youtube.com";

lock = threading.Lock();

with open("subdomain/file.txt",'r') as f1:
    content = f1.read().splitlines();
    print(content);
    
for sub in content:
    t = threading.Thread(target=check_domain,args=(sub,));
    
    discovered_subdomains.append(t);
    t.start();
    
for t in discovered_subdomains:
    t.join();
    

    
    