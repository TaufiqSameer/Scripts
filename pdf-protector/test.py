import sys

if len(sys.argv) != 3:
    print("UsageError : Need exactly 3 argument the program name, input file, output file");
    

inputFile = sys.argv[1];
outputFile = sys.argv[2];

with open(inputFile,"wb") as f2:
    f2.write(b"we are samming");
    
with open(inputFile,"rb") as source:
    data = source.read();
    with open(outputFile,"wb") as destination:
        destination.write(data);
        
print("Copied successfully\n");

def combiningFiles(f1,f2):
    try:
        with open(f1,"rb") as source1:
            with open(f2,"rb") as source2:
                with open("output.txt","wb") as destination:
                    data1 = source1.read();
                    data2 = source2.read();
                    content = data1 + data2;
                    destination.write(content);
                    print("Combined successfully");
    except FileNotFoundError:
        print("File not found. Try checking the directory");
    except FileExistsError:
        print("File already exists");
    except Exception as e:
        print("Unconventinal error : " + e);
combiningFiles(inputFile,outputFile);