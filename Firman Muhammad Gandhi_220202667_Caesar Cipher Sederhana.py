def caesar_encrypt(text, shift):
    result = ""
    # Loop untuk setiap karakter dalam teks
    for i in range(len(text)):
        char = text[i]
        # Enkripsi huruf besar (A-Z)
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Enkripsi huruf kecil (a-z)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Jika bukan huruf, biarkan seperti apa adanya
        else:
            result += char
    return result

def caesar_decrypt(cipher, shift):
    result = ""
    # Loop untuk setiap karakter dalam teks
    for i in range(len(cipher)):
        char = cipher[i]
        # Dekripsi huruf besar (A-Z)
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Dekripsi huruf kecil (a-z)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        # Jika bukan huruf, biarkan seperti apa adanya
        else:
            result += char
    return result

# Menu untuk memilih enkripsi atau dekripsi
while True:
    print("\nPilihan:")
    print("1. Enkripsi teks")
    print("2. Dekripsi teks")
    print("3. Keluar")
    choice = input("Masukkan pilihan Anda (1/2/3): ")

    if choice == '1':
        # Input untuk enkripsi
        plain_text = input("Masukkan teks yang ingin dienkripsi: ")
        shift_value = int(input("Masukkan nilai pergeseran (shift): "))
        cipher_text = caesar_encrypt(plain_text, shift_value)
        print("Teks terenkripsi:", cipher_text)

    elif choice == '2':
        # Input untuk dekripsi
        cipher_text = input("Masukkan teks yang ingin didekripsi: ")
        shift_value = int(input("Masukkan nilai pergeseran (shift): "))
        decrypted_text = caesar_decrypt(cipher_text, shift_value)
        print("Teks terdekripsi:", decrypted_text)

    elif choice == '3':
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
