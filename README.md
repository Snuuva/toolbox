
# Verktygslåda för nätverks- och krypteringsverktyg

Detta projekt innehåller en samling Python-baserade verktyg för nätverksskanning, IP-kontroll och kryptering. Ett huvudskript (`main_tool.py`) tillhandahåller en interaktiv meny där du kan välja verktyg och följa instruktioner för att köra varje verktyg.

## Verktyg i projektet

1. **Nmap-skanner** - Skanna en IP-adress med olika inställningar.
2. **Kryptera/Dekryptera fil** - Kryptera eller dekryptera en fil med en nyckel.
3. **Kontrollera webbsida på IP-adress** - Se om en webbsida svarar på en IP-adress (HTTP/HTTPS).
4. **Hitta IP-adressens ursprungsland** - Hämta information om vilket land en IP-adress tillhör.

## Installation

1. Klona detta repository.
2. Installera beroenden från `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Kör huvudskriptet:
   ```bash
   python main_tool.py
   ```

## Användning

Kör `main_tool.py` för att få en interaktiv meny där du kan välja vilket verktyg du vill köra:

- **Nmap-skanner**: Skanna en IP-adress med olika djup.
- **Kryptera/Dekryptera**: Kryptera eller dekryptera en fil med en angiven nyckel.
- **Kontrollera webbsida på IP-adress**: Kontrollera om en server svarar på HTTP/HTTPS på en viss IP.
- **Hitta IP-adressens ursprungsland**: Hämta ursprungsland för en IP-adress.

### Kör verktygen separat

Varje verktyg kan också köras separat från sin egen mapp. Använd `-h` som argument för att se hur respektive verktyg ska användas. Till exempel:

```bash
python tools/nmap_scanner/nmap_scanner.py -h
```

## Projektstruktur

```plaintext
.
├── main_tool.py                # Huvudskript för interaktiv meny
├── tools/                       # Verktygsmapp
│   ├── nmap_scanner/
│   │   └── nmap_scanner.py      # Nmap-skanningsverktyg
│   ├── crypto_tool/
│   │   └── crypto_tool.py       # Krypterings- och dekrypteringsverktyg
│   │   └── generate_key.py      # Nyckelgenerering för crypto_tool
│   ├── checkhttp/
│   │   └── checkhttp.py         # HTTP-statuskontroll på IP
│   └── checkcountry/
│       └── checkcountry.py      # IP-ursprungslandskontroll
├── requirements.txt             # Lista över projektberoenden
└── .gitignore                   # Ignorerade filer i versionering
```

## Beroenden

Alla nödvändiga beroenden finns listade i `requirements.txt`. De inkluderar:

- `requests`
- `cryptography`
- `python-nmap`
- `ipaddress`

## .gitignore

Projektet använder `.gitignore` för att utesluta tillfälliga filer och nyckelfiler från versionskontroll.
