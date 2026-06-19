import PyPDF2,sys
pdf1 = sys.argv[1];
pdf2 = sys.argv[2];

print("Input:", pdf1)
print("Output:", pdf2)

def create_password(pdf1,pdf2):
        password = input("Enter the password");
        with open(pdf1,"rb") as f1:
            with open(pdf2,"wb") as f2:
                reader1 = PyPDF2.PdfReader(f1);
                writer = PyPDF2.PdfWriter();

                for p in reader1.pages:
                    writer.add_page(p);
                    
                writer.encrypt(password);
                
                
                writer.write(f2);
                    
                    
    

# try:
#     with open(pdf1, "rb") as f1:
#         pdf_reader = PyPDF2.PdfReader(f1)
#         page_count = len(pdf_reader.pages)
#         print(f"The number of pages it contains: {page_count}")

# except FileNotFoundError:
#     print("File not found")
    
def main():
    pdf1 = sys.argv[1]
    pdf2 = sys.argv[2]

    create_password(pdf1, pdf2)

if __name__ == "__main__":
    main()
    