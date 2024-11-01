import argparse
import nmap
import datetime
import ipaddress

def is_valid_ip(ip):
    try:
        # Försöker skapa en ip-adress objekt för att verifiera formatet
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        # Om ValueError uppstår är det inte en giltig IP-adress
        return False

def is_internal_ip(ip):
    # Använder ipaddress för att avgöra om IP är i ett privat nätverk
    ip_obj = ipaddress.ip_address(ip)
    return ip_obj.is_private

def perform_scan(ip, scan_type):
    nm = nmap.PortScanner()

    # Välj skanningstyp baserat på argumentet
    if scan_type == '1':
        print(f"Utför snabb skanning på {ip}...")
        nm.scan(ip, arguments='-sV')
    elif scan_type == '2':
        print(f"Utför långsam skanning på {ip} (alla portar)...")
        nm.scan(ip, arguments='-p- -sV')
    elif scan_type == '3':
        print(f"Utför snabb skanning med scripts på {ip}...")
        nm.scan(ip, arguments='-sC -sV')
    elif scan_type == '4':
        print(f"Utför långsam skanning med scripts på {ip}...")
        nm.scan(ip, arguments='-p- -sC -sV')
    
    return nm

def format_scan_results(nm, ip):
    if ip not in nm.all_hosts():
        return "Inga resultat hittades för denna IP."

    result = [f"\nSkanningsresultat för {ip}:"]
    for proto in nm[ip].all_protocols():
        result.append(f"\nProtokoll: {proto}")
        for port in sorted(nm[ip][proto].keys()):
            state = nm[ip][proto][port]['state']
            name = nm[ip][proto][port].get('name', 'okänd tjänst')
            version = nm[ip][proto][port].get('version', 'ingen version')
            product = nm[ip][proto][port].get('product', '')
            extrainfo = nm[ip][proto][port].get('extrainfo', '')

            result.append(f"  Port: {port} | Status: {state} | Tjänst: {name} | Version: {version} {product} {extrainfo}")

    return "\n".join(result)

def save_to_file(scan_result):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"nmap_scan_{timestamp}.txt"
    with open(filename, 'w') as file:
        file.write(scan_result)
    print(f"Resultatet har sparats till {filename}")

def main():
    parser = argparse.ArgumentParser(description="Enkel Nmap-skanner med olika skanningstyper.")
    parser.add_argument("ip", help="IP-adressen du vill skanna")
    parser.add_argument("scan_type", choices=['1', '2', '3', '4'], help="Välj skanningstyp: 1=snabb, 2=alla portar, 3=snabb m. scripts, 4=alla portar m. scripts")
    parser.add_argument("-s", "--save", action="store_true", help="Spara resultatet till en textfil")
    args = parser.parse_args()

    # Kontrollera om inmatningen är en giltig IP-adress
    if not is_valid_ip(args.ip):
        print("Fel: Ange en giltig IP-adress.")
        return

    # Kontrollera om IP är extern och visa varning
    if not is_internal_ip(args.ip):
        confirm = input("VARNING: Du försöker skanna en extern IP-adress. Se till att du har tillstånd. Skriv 'ok' för att fortsätta eller avsluta med 'Nej': ").strip().lower()
        if confirm != "ok":
            print("Skanningen avbröts.")
            return
    
    # Utför skanning
    nm = perform_scan(args.ip, args.scan_type)
    scan_result = format_scan_results(nm, args.ip)

    print("\n--- Skanningsresultat ---")
    print(scan_result)
    
    if args.save:
        save_to_file(scan_result)

if __name__ == "__main__":
    main()
