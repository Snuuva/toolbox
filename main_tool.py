import os
import sys
import subprocess

def run_nmap_scanner():
     # Begär IP-adress och skanningstyp från användaren
    ip_address = input("Ange IP-adressen du vill skanna: ")
    scan_type = input("Välj skanningstyp:\n1=Snabb\n2=Alla portar\n3=Snabb med scripts\n4=Alla portar med scripts\nDitt val: ")
    save_result = input("Vill du spara resultatet till en fil? (j/n): ").strip().lower()

    # Skapa kommandot för att anropa nmap_scanner.py med IP-adress och skanningstyp
    command = ["python3", "tools/nmap_scanner/nmap_scanner.py", ip_address, scan_type]
    
    # Lägg till "-s" flaggan om man valt att spara resultatet
    if save_result == 'j':
        command.append("-s")
    
    # Kör kommandot
    subprocess.run(command)

def run_crypto_tool():
    # Begär sökväg till filen och åtgärd (kryptera eller dekryptera) från användaren
    file_path = input("Ange sökvägen till filen du vill kryptera/dekryptera: ")
    action = input("Välj funktion:\n1=Kryptera\n2=Dekryptera\nDitt val: ")
    encrypt_flag = "-e" if action == "1" else "-d"  # Välj flagga baserat på användarens val

    # Skapa kommandot för att anropa crypto_tool.py med krypterings-/dekrypteringsflagga och filväg
    command = ["python3", "tools/crypto_tool/crypto_tool.py", encrypt_flag, "-f", file_path]
    subprocess.run(command)

def run_checkhttp():
    # Begär IP-adress för att kontrollera HTTP/HTTPS-status
    ip_address = input("Ange IP-adress för att kontrollera om en webbsida körs (HTTP och HTTPS): ")
    
    # Skapa kommandot för att anropa checkhttp.py med IP-adressen
    command = ["python3", "tools/checkhttp/checkhttp.py", ip_address]
    subprocess.run(command)

def run_checkcountry():
    # Begär IP-adress för att hitta ursprungsland
    ip_address = input("Ange IP-adress för att hitta ursprungsland: ")

    # Skapa kommandot för att anropa checkcountry.py med IP-adressen
    command = ["python3", "tools/checkcountry/checkcountry.py", ip_address]
    subprocess.run(command)

def main_menu():
    # Huvudmeny som loopar tills användaren väljer att avsluta
    while True:
        print("\n--- Verktygsmeny ---")
        print("1: Nmap-skanner")
        print("2: Kryptera/Dekryptera fil")
        print("3: Kontrollera om en webbsida körs på en IP-adress")
        print("4: Hitta ursprungsland för en IP-adress")
        print("5: Avsluta")

        choice = input("Välj ett alternativ (1-5): ")
        # Kör motsvarande funktion baserat på användarens val
        if choice == "1":
            run_nmap_scanner()
        elif choice == "2":
            run_crypto_tool()
        elif choice == "3":
            run_checkhttp()
        elif choice == "4":
            run_checkcountry()
        elif choice == "5":
            print("Avslutar...")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main_menu()
