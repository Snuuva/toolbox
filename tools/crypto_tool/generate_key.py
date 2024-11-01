from cryptography.fernet import Fernet

def generate_key():
    # Genererar och returnerar en Fernet-nyckel.
    return Fernet.generate_key()

def save_key(key, filename):
    # Sparar nyckeln i en .key-fil.
    with open(filename, 'wb') as key_file:
        key_file.write(key)

if __name__ == "__main__":
    key = generate_key()
    key_filename = input("Ange namnet på nyckelfilen (utan tillägg): ") + ".key"
    save_key(key, key_filename)
    print(f"Nyckel sparad som {key_filename}")
