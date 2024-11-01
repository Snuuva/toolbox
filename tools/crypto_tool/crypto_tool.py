import argparse
import os
from cryptography.fernet import Fernet, InvalidToken
from generate_key import generate_key, save_key  # Importera nyckelfunktioner från generate_key.py

def load_key(key_file):
     # Ladda nyckel från en .key-fil, hantera fel om filen saknas
    try:
        with open(key_file, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Nyckelfilen {key_file} hittades inte.")
        return None

def encrypt_file(file_path):
    # Läs in filens innehåll i binärt läge, hantera fel om filen saknas
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Filen {file_path} hittades inte.")
        return

    # Generera en nyckel genom att använda generate_key från generate_key.py
    key = generate_key()
    key_file_path = f"{file_path}.key"
    save_key(key, key_file_path)

    # Kryptera filens innehåll
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    # Spara krypterad data till en ny fil
    encrypted_file_path = f"{file_path}.crypt"
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)
    print(f"Fil krypterad: {encrypted_file_path} (nyckel sparad i {key_file_path})")

def decrypt_file(file_path):
    # Kontrollera om filen är krypterad (.crypt)
    if file_path.endswith(".crypt"):
        original_file = file_path.replace(".crypt", "")  # Återställ ursprungligt filnamn
        key_file = original_file + ".key"
    else:
        print(f"Filen {file_path} verkar inte vara en krypterad fil (.crypt).")
        return

    # Ladda nyckeln från nyckelfilen
    print(f"Laddar nyckelfilen: {key_file}")
    key = load_key(key_file)
    
    if key is None:
        print("Nyckel saknas eller kunde inte laddas.")
        return

    try:
        fernet = Fernet(key)
    except ValueError:
        print("Ogiltig nyckel.")
        return

    # Läs in den krypterade filen
    print(f"Läser in krypterad fil: {file_path}")
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
    except FileNotFoundError:
        print(f"Krypterade filen {file_path} hittades inte.")
        return

    # Försök att dekryptera filen
    try:
        print("Försöker dekryptera...")
        decrypted_data = fernet.decrypt(encrypted_data)
        print("Dekryptering lyckades!")
    except InvalidToken:
        print("Fel vid dekryptering. Ogiltig nyckel.")
        return

    # Dekrypterad data sparas till fil
    try:
        with open(original_file, 'wb') as f:
            f.write(decrypted_data)
        print(f"Fil dekrypterad och sparad som: {original_file}")
    except Exception as e:
        print(f"Fel vid sparandet av den dekrypterade filen: {e}")

def main():
    # Hanterar kommandoradsargument för kryptering/dekryptering
    parser = argparse.ArgumentParser(description="Kryptera och dekryptera filer med Fernet-kryptering.")
    parser.add_argument("-e", "--encrypt", help="Kryptera en fil", action="store_true")
    parser.add_argument("-d", "--decrypt", help="Dekryptera en fil", action="store_true")
    parser.add_argument("-f", "--file", help="Filen som ska krypteras/dekrypteras", required=True)
    args = parser.parse_args()

    # Kontrollera att endast en operation utförs åt gången
    if args.encrypt and args.decrypt:
        print("Du kan inte både kryptera och dekryptera samtidigt.")
        return

    if args.encrypt:
        encrypt_file(args.file)
    elif args.decrypt:
        decrypt_file(args.file)
    else:
        print("Ange antingen -e för att kryptera eller -d för att dekryptera.")

if __name__ == "__main__":
    main()
