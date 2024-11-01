import requests
import argparse
import ipaddress

def check_website_status(ip_address):
    # Försöker ansluta till webbsidor via både HTTP och HTTPS för att kontrollera statuskoder
    urls = [
        f'http://{ip_address}',     # URL för HTTP-protokoll
        f'https://{ip_address}'     # URL för HTTPS-protokoll
    ]

    for url in urls:
        try:
            # Skickar GET-förfrågan med en timeout på 5 sekunder
            response = requests.get(url, timeout=5)
            print(f"URL: {url}, Statuskod: {response.status_code}") # Skriver ut URL och HTTP-statuskod
        except requests.ConnectionError:
            # Hanterar anslutningsfel
            print(f"Kunde inte ansluta till {url}. Ingen anslutning.")
        except requests.Timeout:
            # Hanterar timeoutfel om förfrågan tar längre än 5 sekunder
            print(f"Timeout när försökte ansluta till {url}.")
        except requests.RequestException as e:
            # Hanterar andra typer av fel som kan uppstå
            print(f"Kunde inte ansluta till {url}. Fel: {e}")

def main():
    # Skapar en parser för att ta emot en IP-adress från kommandoraden
    parser = argparse.ArgumentParser(description="Kontrollera om en webbsida körs på en angiven IP-adress.")
    parser.add_argument("ip_address", type=str, help="Ange en IP-adress för att kontrollera status på HTTP och HTTPS.")
    args = parser.parse_args()

    
    # Validerar att inmatad IP-adress har korrekt format, annars visas felmeddelande
    try:
        ipaddress.ip_address(args.ip_address)
    except ValueError:
        # Skriver ut ett felmeddelande och avslutar programmet om IP-adressen är ogiltig
        print("Fel: Ogiltig IP-adress. Vänligen ange en korrekt IP-adress.")
        return

    # Anropar funktionen som hämtar ursprungslandet för IP-adressen
    check_website_status(args.ip_address)

if __name__ == "__main__":
    main()