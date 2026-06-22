import pikepdf,tqdm,itertools,string, argparse;
from concurrent.futures import ThreadPoolExecutor,as_completed
from tqdm import tqdm;

def generate_password(file):
    try:
        with open(file,"w") as f1:
            f1.write("sameer\nsameer123\nlol123\n123");
    except:
        print("Error occured while writing into the file")  

l = [];
def try_password(file,pa):
        try:
            with pikepdf.open(file, password=pa):
                print(f"Opened successfully with: {pa}")
                return pa

        except pikepdf.PasswordError:
            print("nothing")

def load_passwords(file):
    try:
        with open(file,"r") as f1:
            li = f1.readlines();
            for line in li:
                l.append(line.strip());
    except FileNotFoundError:
        print("File is not available. Check the directory if it exists");
    except:
        print("Error happened while reading a file");
        
def decrypt_pdf(fike):
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(try_password,fike,pa) for pa in l];
        for future in tqdm(
            as_completed(futures),
            total = len(futures),
            desc="Processing"):
            future.result();
            

if __name__ == "__main__":
    argParser = argparse.ArgumentParser(description="Pdf cracker");
    argParser.add_argument("PDFname", help="Name of the pdf u want to crack");
    argParser.add_argument("--WordList",help="Give the file which you want to test against the pdf");
    arg = argParser.parse_args();
    
    print(f"Testing against the file : {arg.PDFname} with wordList as : {arg.WordList}")
    generate_password(arg.WordList);
    load_passwords(arg.WordList);
    decrypt_pdf(arg.PDFname);
    
    print("Completed successfully\n");