import requests
import argparse
import ipaddress

def get_country(ip_address):
    # Kollar ursprungsland för en given IP-adress genom att göra en förfrågan till ipinfo.io API
    try:
        # Skickar GET-förfrågan till API:et med IP-adressen, med timeout på 5 sekunder
        response = requests.get(f"http://ipinfo.io/{ip_address}/json", timeout=5)
        # Kontrollerar om svaret från API:et är lyckat (statuskod 200)
        if response.status_code == 200:
            # Om lyckat svar, extrahera och visa landinformation från svaret
            data = response.json()
            print(f"IP: {ip_address}, Land: {data.get('country')}")
        else:
            # Hanterar misslyckad API-förfrågan
            print(f"Kunde inte hämta data för IP: {ip_address}")
    except requests.exceptions.Timeout:
        # Hanterar timeout-fel vid förfrågan till API:et
        print("Timeout uppnådd vid anrop till API")
    except requests.exceptions.RequestException as e:
        # Hanterar andra fel som kan uppstå
        print(f"Ett fel uppstod: {e}")

def main():
    # Skapar en parser för att ta emot en IP-adress från kommandoraden
    parser = argparse.ArgumentParser(description="Sök upp ursprungslandet för en given IP-adress.")
    parser.add_argument("ip_address", type=str, help="Ange en IP-adress för att få information om ursprungsland.")
    args = parser.parse_args()

    # Validerar att inmatad IP-adress har korrekt format, annars visas felmeddelande
    try:
        ipaddress.ip_address(args.ip_address)
    except ValueError:
        # Skriver ut ett felmeddelande och avslutar programmet om IP-adressen är ogiltig
        print("Fel: Ogiltig IP-adress. Vänligen ange en korrekt IP-adress.")
        return

    # Anropar funktionen som hämtar ursprungslandet för IP-adressen
    get_country(args.ip_address)

if __name__ == "__main__":
    main()