# Fungsi untuk mengenkripsi teks menggunakan Vigenere Cipher
def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        char = plain_text[i]
        key_char = key[i % key_length]
        encrypted_char = chr(((ord(char) + ord(key_char)) % 26) + ord('A'))
        encrypted_text += encrypted_char
    return encrypted_text

# Fungsi untuk mendekripsi teks yang telah dienkripsi dengan Vigenere Cipher
def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        key_char = key[i % key_length]
        decrypted_char = chr(((ord(char) - ord(key_char)) % 26) + ord('A'))
        decrypted_text += decrypted_char
    return decrypted_text

# Database pengguna (contoh sederhana)
user_database = {
    "user1": "KLMOPQR",
    "user2": "WXYZABC"
}

# Input username dan password
username = input("Masukkan username: ")
password = input("Masukkan password: ")

# Periksa apakah pengguna ada dalam database
if username in user_database:
    stored_encrypted_password = user_database[username]
    # Mendekripsi password yang ada dalam database
    decrypted_password = vigenere_decrypt(stored_encrypted_password, "SECRETKEY")
    if password == decrypted_password:
        print("Login berhasil!")
    else:
        print("Login gagal. Password salah.")
else:
    print("Login gagal. Username tidak ditemukan.")