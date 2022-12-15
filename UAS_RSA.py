def menu():
    print ('Pilihan Menu')
    print ('1. Enkripsi PDF')
    print ('2. Enkripsi Dekripsi CSV')
    print ('3. Enkripsi Dekripsi Image')
    print ('4. Dekripsi PDF')

def enkripsipdf():
    from PyPDF2 import PdfFileWriter, PdfFileReader 
    out = PdfFileWriter() # buat objek pdf writer
    file = PdfFileReader("D:/Coding/SKD/File/file_pdf.pdf") # buka file pdf asli 
    num = file.numPages # identifikasi total halaman file
    for idx in range(num): #program membaca setiap halaman file sesuai halaman yg diidentifikasi 
        page = file.getPage(idx)
        out.addPage(page) 
    password = "pass"  # masukkan password enkripsi 
    out.encrypt(password) # enkripsi masing-masing halaman
    with open("D:/Coding/SKD/File/file_pdf_encrypted.pdf", "wb") as f:  # buka file enkripsi "file_pdf_encrypted.pdf"
        out.write(f) # simpan pdf 
def encdeccsv():
    from cryptography.fernet import Fernet # import modul
    # key generation
    key = Fernet.generate_key()
    # read string kunci
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    # pakai kunci
    fernet = Fernet(key)
    # buka file csv
    with open('D:/Coding/SKD/File/file_csv.csv', 'rb') as file:
        original = file.read()
    # enkripsi csv
    encrypted = fernet.encrypt(original)
    # simpan file enkripsi
    with open('D:/Coding/SKD/File/file_csv_encrypted.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    #DEKRIPSI
    # pakai kunci yang tadi
    fernet = Fernet(key)
    # buka file hasil enkrpisi
    with open('D:/Coding/SKD/File/file_csv_encrypted.csv', 'rb') as enc_file:
        encrypted = enc_file.read()
    # langsung di dekripsi 
    decrypted = fernet.decrypt(encrypted)
    # cek hasil dekripsi cocok apa tidak ??
    with open('D:/Coding/SKD/File/file_csv_derypted.csv', 'wb') as dec_file:
        dec_file.write(decrypted)
def encdecimg():
    import cv2
    import numpy as np

    demo = cv2.imread("D:/Coding/SKD/File/image.jpg", 0)
    r, c = demo.shape
    key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)  # Generate random key image
    cv2.imwrite("D:/Coding/SKD/File/key.jpg", key)   # Save key image

    cv2.imshow("demo", demo)  # Display original image
    cv2.imshow("key", key)  # Display key image

    encryption = cv2.bitwise_xor(demo, key)  # encryption
    cv2.imwrite("D:/Coding/SKD/File/image_encrypted.jpg", encryption)  
    # Save the encrypted image
    decryption = cv2.bitwise_xor(encryption, key)  # decrypt
    cv2.imwrite("D:/Coding/SKD/File/image_decrypted.jpg", decryption) # Save the decrypted image

    cv2.imshow("encryption", encryption)  # Display ciphertext image
    cv2.imshow("decryption", decryption)  # Displays the decrypted image

    cv2.waitKey(-1)
    cv2.destroyAllWindows()
def dekripsipdf():
    from PyPDF2 import PdfFileWriter, PdfFileReader 
    # buat objek pdf writer
    out = PdfFileWriter() 
    # buka file pdf yg terenkripsi
    file = PdfFileReader("D:/Coding/SKD/File/file_pdf_encrypted.pdf")
    # masukkan password enkripsi 
    password = "pass"
    # cek file terenkripsi atau tidak 
    if file.isEncrypted:
        # jika file terenkripsi, langsung di dekripsi pakai password 
        file.decrypt(password)
        # dekripsi dilakukan setiap halaman file pdf
        # simpan ke dalam file baru 
        for idx in range(file.numPages):
            # identifikasi halaman file 
            page = file.getPage(idx)
            # masukkan halaman yg sudah diidentifikasi dan sudah di dekripsi ke file baru 
            out.addPage(page)
        # buka file baru "file_pdf_decrypted.pdf"
        with open("D:/Coding/SKD/File/file_pdf_decrypted.pdf", "wb") as f:
            # simpan file baru 
            out.write(f)
        print("File decrypted Successfully.")
    else:
        print("File already decrypted.")

menu()    
pilih = input('masukkan pilihan : ')

if pilih == ('1'):
    enkripsipdf()
elif pilih == ('2'):
    encdeccsv()
elif pilih == ('3'):
    encdecimg()
elif pilih == ('4'):
    dekripsipdf()
else :
    print ('Erorr')


