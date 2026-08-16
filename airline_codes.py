# airline_codes.py
# IATA (2-character) to ICAO (3-character) airline code lookup table.
# Source: ICAO Doc 8585, cross-referenced with OurAirports and OpenFlights databases.
# Import with: from airline_codes import IATA_TO_ICAO

IATA_TO_ICAO = {
    "0B": "BMS",  # Blue Air
    "0J": "BON",  # Overland Airways
    "0V": "VFC",  # VASCO
    "1T": "ICE",  # Icelandair (legacy)
    "2B": "ARD",  # Severstal Air Company
    "2D": "ESF",  # Eastern Air Express
    "2F": "EFL",  # Frontier Flying Service
    "2G": "HYR",  # Angara Airlines
    "2I": "SRR",  # Star Peru
    "2J": "VBW",  # Air Burkina
    "2K": "GLG",  # Aerolineas Galapagos (Aerogal)
    "2L": "OAW",  # Helvetic Airways
    "2M": "MDA",  # Maya Island Air
    "2N": "NTJ",  # Nextjet
    "2O": "RCF",  # Island Air (Hawaii, defunct)
    "2P": "GAP",  # PAL Express
    "2Q": "SNC",  # Air Somalia
    "2R": "VRA",  # Via Rail (codeshare)
    "2S": "SKZ",  # Island Air (defunct)
    "2T": "TBF",  # Tikehau Air
    "2U": "SAT",  # Sud Aviation Transport
    "2V": "AMT",  # Amtrak (codeshare)
    "2W": "WLC",  # Welcome Air
    "2Y": "AMW",  # My Indo Airlines
    "3C": "RSK",  # Air Chathams
    "3E": "MON",  # Air Choice One
    "3F": "PPM",  # Pacific Air (Peru)
    "3G": "AUR",  # Aurigny Air Services
    "3H": "AIE",  # Air Inuit
    "3J": "BJT",  # Vueling (legacy)
    "3K": "JSA",  # Jetstar Asia
    "3L": "PLC",  # Intersky
    "3M": "GJS",  # SkyWest (United Express)
    "3O": "MAC",  # Air Arabia Maroc
    "3P": "TWN",  # TANair
    "3Q": "CYH",  # Yunnan Hongtu Airlines
    "3R": "GER",  # Goulet Air
    "3S": "SSY",  # Aeronaves TSM
    "3T": "KRN",  # Turan Air
    "3U": "CSC",  # Sichuan Airlines
    "3V": "TAY",  # TNT Airways
    "3W": "MMQ",  # Malawi Airlines
    "3X": "JEA",  # Japan Air Commuter
    "3Y": "EMY",  # European Air Express
    "4B": "BUT",  # Boutique Air
    "4C": "ARE",  # LAN Colombia (LATAM Colombia)
    "4D": "ASD",  # Air Sinai
    "4E": "SHX",  # Skywork Airlines
    "4F": "AKT",  # Air Flamenco
    "4G": "GKS",  # Gazpromavia
    "4H": "HHN",  # HiSky
    "4J": "SNB",  # Somon Air
    "4K": "AKA",  # Kalitta Charters
    "4L": "GEO",  # Georgian Airways
    "4M": "DSM",  # LATAM Argentina
    "4N": "ANT",  # Air North
    "4O": "ANK",  # Air Astana (legacy)
    "4P": "LGP",  # Regional Air (Poland)
    "4Q": "SFW",  # Safi Airways
    "4R": "RRR",  # Renfe (rail codeshare)
    "4S": "SKP",  # Sky Express (Greece)
    "4T": "BMM",  # Belair Airlines
    "4U": "GWI",  # Germanwings
    "4V": "BVT",  # Fly Vista
    "4W": "WDL",  # WDL Aviation
    "4X": "BCI",  # Regional Express (Rex)
    "4Y": "SCF",  # Explore Air
    "5C": "ICL",  # CAL Cargo Airlines
    "5D": "SLI",  # Aerolitoral
    "5E": "BSF",  # SkyEurope (defunct)
    "5F": "AFE",  # Arctic Circle Air
    "5G": "HLF",  # Fly540
    "5H": "FFV",  # Five Forty Aviation
    "5J": "CEB",  # Cebu Pacific
    "5K": "HFY",  # Hi Fly
    "5L": "LNK",  # Aerosur
    "5M": "MNJ",  # Mango Airlines
    "5N": "AUL",  # Nordavia
    "5O": "FPO",  # ASL Airlines France
    "5P": "SHF",  # SkyHigh Maldives
    "5Q": "BAF",  # BelleAir
    "5R": "RPB",  # Rutaca Airlines
    "5S": "SCQ",  # Servicios Aereos de los Andes
    "5T": "LAC",  # Canadian North
    "5U": "LGN",  # Lugansk Airlines
    "5V": "VGN",  # Lviv Airlines
    "5W": "AEW",  # Wizz Air Abu Dhabi
    "5X": "UPS",  # UPS Airlines
    "5Y": "ATN",  # Atlas Air
    "5Z": "CND",  # Bismillah Airlines
    "6B": "TBL",  # TUIfly Nordic
    "6C": "SOO",  # Sunrise Airways
    "6D": "LIE",  # Pelita Air Service
    "6E": "IGO",  # IndiGo
    "6F": "FRK",  # Fly Romania
    "6G": "EXS",  # Jet2
    "6H": "ISR",  # Israir
    "6I": "MNO",  # Airline
    "6J": "SOL",  # Solaseed Air
    "6K": "SKK",  # Asian Spirit
    "6L": "ERN",  # Aklak Air
    "6M": "MKA",  # Macedonian Airlines
    "6N": "NYX",  # Niger Airlines
    "6O": "OFT",  # Orbest
    "6P": "PGX",  # PG Air
    "6Q": "CRN",  # Cham Wings Airlines
    "6R": "ADV",  # Alrosa Mirny Air Enterprise
    "6S": "SXD",  # Saudi Gulf Airlines
    "6T": "UTN",  # Air Mandalay
    "6U": "UTC",  # Air Ukraine
    "6V": "VVC",  # VECA Airlines
    "6W": "SVM",  # Saratov Airlines
    "6X": "MER",  # Mora Air Service
    "6Y": "SGO",  # SmartLynx Airlines
    "7C": "JJA",  # Jeju Air
    "7E": "ESC",  # Sylt Air
    "7F": "ERF",  # First Air
    "7G": "SFJ",  # StarFlyer
    "7H": "ERH",  # Era Alaska
    "7I": "SDR",  # Insel Air
    "7J": "ERJ",  # Tajik Air
    "7K": "KGL",  # Kogalymavia
    "7L": "ERL",  # Aerocaribbean
    "7M": "MXL",  # Maxair
    "7N": "ERN",  # Pawa Dominicana
    "7O": "OAG",  # Galaxy Air
    "7P": "PGO",  # Avia Traffic Company
    "7Q": "MlW",  # Malawi Airlines
    "7R": "BRK",  # Rusline
    "7S": "WRC",  # Ryan Air Services
    "7T": "TOW",  # Tobruk Air
    "7U": "RUS",  # Aviaenergo
    "7V": "FVL",  # Federal Airlines
    "7W": "REL",  # Wind Rose Aviation
    "7X": "BZH",  # Aero Benin
    "7Y": "MED",  # Mid Airlines
    "8B": "TIB",  # Caribbean Star Airlines
    "8C": "ATZ",  # Shanxi Airlines
    "8D": "PRB",  # Perimeter Aviation
    "8E": "BRW",  # Bering Air
    "8F": "SFT",  # STP Airways
    "8G": "HSG",  # Air Service
    "8H": "HAV",  # Hellas Jet
    "8I": "IBB",  # Iberia Regional
    "8J": "EFW",  # Eco Jet
    "8K": "KHB",  # Khabur Airlines
    "8L": "LKE",  # Lucky Air
    "8M": "MMA",  # Myanmar Airways International
    "8N": "RDN",  # Regional Air (Tanzania)
    "8O": "OHI",  # West Coast Air
    "8P": "PCO",  # Pacific Coastal Airlines
    "8Q": "DHS",  # Onur Air
    "8R": "TAI",  # TRIP Linhas Aereas
    "8S": "SRN",  # Sounds Air
    "8T": "ATR",  # Air Tindi
    "8U": "AAW",  # Afriqiyah Airways
    "8V": "WRF",  # Wright Air Service
    "8W": "FBW",  # Fly Baldwin
    "8X": "LEV",  # Bul Air
    "8Y": "CMV",  # Carpatair
    "9A": "CNW",  # Coms Air
    "9B": "UBD",  # AccesRail
    "9C": "DKH",  # Shenzhen Airlines
    "9D": "TVS",  # Toumai Air Tchad
    "9E": "FLG",  # Endeavor Air (Delta Connection)
    "9F": "EUX",  # Eurostar (rail codeshare)
    "9G": "PAG",  # Pro Air
    "9H": "CAH",  # Chang An Airlines
    "9I": "LAL",  # Thai Lion Air
    "9J": "EAX",  # Dana Airlines
    "9K": "KAP",  # Cape Air
    "9L": "CLU",  # Colgan Air
    "9M": "CNM",  # Central Mountain Air
    "9N": "TGX",  # Tropic Air
    "9O": "TXW",  # Trans Maldivian Airways
    "9P": "PVV",  # Pegas Fly
    "9Q": "PEM",  # PB Air
    "9R": "PGP",  # Phuket Air
    "9S": "SRQ",  # Spring Airlines
    "9T": "RUN",  # ATRAN Cargo Airlines
    "9U": "MLD",  # Air Moldova
    "9V": "SVA",  # Avior Airlines
    "9W": "JAI",  # Jet Airways
    "9X": "NVR",  # Southern Airways Express
    "9Y": "AYE",  # Air Kazakstan
    "AA": "AAL",  # American Airlines
    "AB": "BER",  # Air Berlin (defunct)
    "AC": "ACA",  # Air Canada
    "AD": "AZU",  # Azul Brazilian Airlines
    "AE": "MDA",  # Mandarin Airlines
    "AF": "AFR",  # Air France
    "AG": "AAB",  # Aruba Airlines
    "AH": "DAH",  # Air Algerie
    "AI": "AIC",  # Air India
    "AJ": "AAF",  # Aero Contractors
    "AK": "AXM",  # AirAsia (Malaysia)
    "AL": "AAH",  # Skywagon Airlines
    "AM": "AMX",  # Aeromexico
    "AN": "ANZ",  # Air New Zealand (legacy)
    "AO": "OCA",  # Avianova
    "AP": "ADC",  # Alba Star
    "AQ": "AAQ",  # Aloha Airlines (defunct)
    "AR": "ARG",  # Aerolineas Argentinas
    "AS": "ASA",  # Alaska Airlines
    "AT": "RAM",  # Royal Air Maroc
    "AU": "AUT",  # Austral Lineas Aereas
    "AV": "AVA",  # Avianca
    "AW": "THY",  # Africa World Airlines
    "AX": "LOF",  # Trans States Airlines
    "AY": "FIN",  # Finnair
    "AZ": "AZA",  # ITA Airways (formerly Alitalia)
    "B2": "BRU",  # Belavia
    "B3": "BGL",  # Bhutan Airlines
    "B4": "BCB",  # ZanAir
    "B6": "JBU",  # JetBlue Airways
    "B7": "UIA",  # Uni Air
    "B8": "ERT",  # Eritrean Airlines
    "B9": "IRB",  # Iran Airtour
    "BA": "BAW",  # British Airways
    "BB": "BBD",  # Seaborne Airlines
    "BC": "SKY",  # Skymark Airlines
    "BD": "BMA",  # bmi British Midland (defunct)
    "BE": "BEE",  # Flybe
    "BF": "FBF",  # French Bee
    "BG": "BBC",  # Biman Bangladesh Airlines
    "BH": "BHT",  # Hawkair
    "BI": "RBA",  # Royal Brunei Airlines
    "BJ": "LBT",  # Nouvelair
    "BK": "OKS",  # Okay Airways
    "BL": "PIC",  # Pacific Airlines
    "BM": "BMR",  # bmi Regional
    "BN": "BNL",  # Luxair (legacy)
    "BO": "BBN",  # Bouraq Airlines (defunct)
    "BP": "BOT",  # Air Botswana
    "BQ": "BRQ",  # Aeromar
    "BR": "EVA",  # EVA Air
    "BS": "BAB",  # British International Helicopters
    "BT": "BTI",  # airBaltic
    "BU": "BUC",  # Badr Airlines
    "BV": "BPA",  # Blue Panorama Airlines
    "BW": "BWA",  # Caribbean Airlines
    "BX": "ABL",  # Air Busan
    "BY": "TOM",  # TUI Airways
    "BZ": "BSK",  # Blue Sky Aviation
    "C2": "CWC",  # Champagne Airlines
    "C3": "IBB",  # Contact Air
    "C4": "LCO",  # LionAir (defunct)
    "C5": "UCA",  # CommutAir
    "C6": "BRB",  # CanJet
    "C7": "RLE",  # Corse-Mediterranee
    "C8": "CXA",  # Cronos Airlines
    "C9": "RUS",  # Cirrus Airlines
    "CA": "CCA",  # Air China
    "CB": "SWT",  # ScotAirways
    "CC": "ABD",  # CM Airlines
    "CD": "CDK",  # Corendon Dutch Airlines
    "CE": "CMC",  # Chalair Aviation
    "CF": "SHQ",  # City Airline
    "CG": "TOK",  # Airlines PNG
    "CH": "BMJ",  # Bemidji Airlines
    "CI": "CAL",  # China Airlines
    "CJ": "CFE",  # BA CityFlyer
    "CK": "CKK",  # China Cargo Airlines
    "CL": "CLH",  # Lufthansa CityLine
    "CM": "CMP",  # Copa Airlines
    "CN": "GCR",  # Grand China Air
    "CO": "COA",  # Continental Airlines (now United)
    "CP": "CPZ",  # Compass Airlines
    "CQ": "RSO",  # Coastal Aviation
    "CR": "CRX",  # OAG (defunct)
    "CS": "CMI",  # Continental Micronesia
    "CT": "CTN",  # Civil Air Transport
    "CU": "CUB",  # Cubana de Aviacion
    "CV": "CLX",  # Cargolux
    "CW": "CWN",  # Air Marshall Islands
    "CX": "CPA",  # Cathay Pacific
    "CY": "CYP",  # Cyprus Airways
    "CZ": "CSN",  # China Southern Airlines
    "D2": "SBG",  # Severstal Air
    "D3": "DAO",  # Daallo Airlines
    "D7": "XAX",  # AirAsia X
    "D8": "IBK",  # Norwegian Air International
    "D9": "DNV",  # Aeroflot-Don (defunct)
    "DA": "GFA",  # Air Georgia
    "DB": "BZH",  # Brit Air
    "DC": "BRX",  # Braathens Regional Aviation
    "DD": "NOK",  # Nok Air
    "DE": "CFG",  # Condor
    "DF": "SRR",  # Condor Berlin (defunct)
    "DG": "RPC",  # Cebgo
    "DH": "DHK",  # DHL Air
    "DI": "DBA",  # dba (defunct)
    "DJ": "VOZ",  # Virgin Australia (domestic)
    "DK": "DKR",  # Eastland Air
    "DL": "DAL",  # Delta Air Lines
    "DM": "LSD",  # Maersk Air (defunct)
    "DN": "NMB",  # Norwegian Air Argentina
    "DO": "DOA",  # Dominicana de Aviacion
    "DP": "PBD",  # Pobeda Airlines
    "DQ": "CRQ",  # Coastal Air Transport
    "DS": "DSR",  # EasyJet Switzerland
    "DT": "DTA",  # TAAG Angola Airlines
    "DU": "HKE",  # Hemus Air
    "DV": "VSV",  # SCAT Airlines
    "DW": "CWA",  # Aero-Charter Ukraine
    "DX": "DTR",  # Danish Air Transport
    "DY": "NAX",  # Norwegian Air Shuttle
    "DZ": "QNC",  # Donghai Airlines
    "E2": "EXY",  # Eurowings Discover
    "E3": "EVX",  # Domodedovo Airlines
    "E4": "MWM",  # Aero Asia
    "E5": "ENB",  # Air Arabia Egypt
    "E6": "ECV",  # Bringer Air Cargo
    "E7": "EUR",  # Equaflight Service
    "E8": "TGS",  # Alada
    "E9": "BOS",  # Boston-Maine Airways
    "EA": "EAL",  # Eastern Airlines
    "EB": "EBA",  # Wamos Air
    "EC": "ECA",  # Avialeasing Aviation Company
    "ED": "ELD",  # AirExplore
    "EE": "ERR",  # Aero Airlines
    "EF": "EFL",  # Far Eastern Air Transport
    "EG": "EGX",  # Japan Asia Airways
    "EH": "EHE",  # SAETA (defunct)
    "EI": "EIN",  # Aer Lingus
    "EJ": "NJS",  # New England Airlines
    "EK": "UAE",  # Emirates
    "EL": "ELI",  # Air Lingus (legacy)
    "EM": "EML",  # Empire Airlines
    "EN": "ENI",  # Air Dolomiti
    "EO": "HEA",  # Hewa Bora Airways
    "EP": "IRC",  # Iran Aseman Airlines
    "EQ": "TYA",  # TAME
    "ER": "ERA",  # Astar Air Cargo
    "ES": "ESK",  # DHL International
    "ET": "ETH",  # Ethiopian Airlines
    "EU": "EAE",  # Ecuatoriana (defunct)
    "EV": "EAB",  # ExpressJet Airlines
    "EW": "EWG",  # Eurowings
    "EX": "FXX",  # Air Santo Domingo
    "EY": "ETD",  # Etihad Airways
    "EZ": "SUS",  # Sun Air of Scandinavia
    "F2": "FRF",  # Safarilink Aviation
    "F3": "FSA",  # Flyadeal
    "F4": "SFK",  # Albawings
    "F5": "FFM",  # Flyr
    "F6": "FFB",  # China Postal Airlines
    "F7": "FLY",  # Fly Jamaica
    "F8": "SFJ",  # Flair Airlines
    "F9": "FFT",  # Frontier Airlines
    "FA": "FSC",  # Safair
    "FB": "LZB",  # Bulgaria Air
    "FC": "FRO",  # Finncomm Airlines
    "FD": "AIQ",  # Thai AirAsia
    "FE": "FEA",  # Far Eastern Air Transport
    "FF": "TOM",  # TUIfly
    "FG": "AFG",  # Ariana Afghan Airlines
    "FH": "FHY",  # Freebird Airlines
    "FI": "ICE",  # Icelandair
    "FJ": "FJI",  # Fiji Airways
    "FK": "FKA",  # Africa West
    "FL": "TRS",  # AirTran Airways (defunct)
    "FM": "CSH",  # Shanghai Airlines
    "FN": "RYR",  # Ryanair (subsidiary)
    "FO": "FOM",  # Felix Airways
    "FP": "FAP",  # Pelican Air Services
    "FQ": "FQA",  # Thomas Cook Airlines Scandinavia
    "FR": "RYR",  # Ryanair
    "FS": "SXX",  # Severstal Air
    "FT": "FTH",  # Siem Reap Airways
    "FU": "FZA",  # Fuzhou Airlines
    "FV": "SDM",  # Rossiya Airlines
    "FW": "IWD",  # ICAO Air
    "FX": "FDX",  # FedEx Express
    "FY": "FFM",  # Firefly
    "FZ": "FDB",  # flydubai
    "G2": "GGN",  # Avirex
    "G3": "GLO",  # Gol Transportes Aereos
    "G4": "AAY",  # Allegiant Air
    "G5": "HXA",  # China Express Airlines
    "G6": "GNR",  # Guine Bissaur Airlines
    "G7": "GJS",  # GoJet Airlines
    "G8": "GOW",  # Go Air
    "G9": "ABY",  # Air Arabia
    "GA": "GIA",  # Garuda Indonesia
    "GB": "GBK",  # Encore (formerly Quebecair)
    "GC": "LGC",  # Lina Congo
    "GD": "GDN",  # Aero Gabon
    "GE": "TNA",  # TransAsia Airways (defunct)
    "GF": "GFA",  # Gulf Air
    "GG": "GGG",  # Air Guyane
    "GH": "GHB",  # Globus Airlines
    "GI": "GIN",  # Itek Air
    "GJ": "CRJ",  # Loong Air
    "GK": "JJP",  # Jetstar Japan
    "GL": "GRL",  # Air Greenland
    "GM": "GMI",  # Germania (defunct)
    "GN": "GAN",  # Air Gabon
    "GO": "GOE",  # Go2Sky
    "GP": "GPH",  # APG Airlines
    "GQ": "GBJ",  # Sky Express (Russia)
    "GR": "GBL",  # Aurigny Air Services
    "GS": "GCR",  # Tianjin Airlines
    "GT": "GTA",  # Air Guilin
    "GU": "GUG",  # Aviateca
    "GV": "GVA",  # Grant Aviation
    "GW": "GBW",  # Kuban Airlines
    "GX": "CBG",  # GX Airlines
    "GY": "GUY",  # Guyana Airways
    "GZ": "GZP",  # Air Rarotonga
    "H1": "HLF",  # Hahn Air
    "H2": "SKU",  # Sky Airline
    "H3": "HMQ",  # Harbour Air
    "H4": "HHL",  # HiSky Europe
    "H6": "HBH",  # Hageland Aviation Services
    "H7": "HLX",  # Helvetic airways
    "H8": "HFN",  # Heli Air Monaco
    "H9": "HIM",  # Himalaya Airlines
    "HA": "HAL",  # Hawaiian Airlines
    "HB": "MMD",  # Harbor Airlines
    "HC": "HCB",  # Aero Tropics Air Services
    "HD": "ADO",  # Air Do
    "HE": "LGW",  # LGW Luftfahrtgesellschaft Walter
    "HF": "HFR",  # Hapagfly (TUIfly)
    "HG": "NLY",  # Niki (defunct)
    "HH": "HHN",  # Heavylift Cargo Airlines
    "HI": "HAJ",  # Papillon Grand Canyon Helicopters
    "HJ": "HJT",  # Hellas Jet
    "HK": "HRZ",  # Yangon Airways
    "HL": "NGX",  # Hill Aviation
    "HM": "SEY",  # Air Seychelles
    "HN": "NHK",  # Afghan Jet International
    "HO": "DKH",  # Juneyao Airlines
    "HP": "AWE",  # America West Airlines (now American)
    "HQ": "BLC",  # Thomas Cook Belgium
    "HR": "HHN",  # Hahn Air
    "HS": "OHO",  # Heli Air Services
    "HT": "HTG",  # Hellenic Imperial Airways
    "HU": "CHH",  # Hainan Airlines
    "HV": "TRA",  # Transavia
    "HW": "NWS",  # North-Wright Airways
    "HX": "CRK",  # Hong Kong Airlines
    "HY": "UZB",  # Uzbekistan Airways
    "HZ": "SAZ",  # Sakhalinskie Aviatrassy
    "I2": "IBS",  # Iberia Express
    "I3": "NIA",  # Ikar Airlines
    "I4": "HLO",  # Interjet
    "I5": "IAD",  # AirAsia India
    "I6": "IAE",  # Air Comet
    "I7": "INN",  # Paramount Airways
    "I8": "IRK",  # Izhavia
    "I9": "IAW",  # Iraqi Airways
    "IB": "IBE",  # Iberia
    "IC": "IAC",  # Air India (regional)
    "ID": "BTK",  # Batik Air (Indonesia)
    "IE": "SOL",  # Solomon Airlines
    "IF": "IRF",  # Islandsflug
    "IG": "ISS",  # Meridiana (defunct)
    "IH": "IHY",  # Falcon Air Express
    "II": "IIN",  # IBC Airways
    "IJ": "TAE",  # Spring Airlines Japan
    "IK": "IKA",  # Imair Airline
    "IL": "ILL",  # Skypower Express Airways
    "IM": "IMX",  # Mahan Air
    "IN": "NAO",  # Nam Air
    "IO": "INX",  # IrAero
    "IQ": "IQA",  # Qazaq Air
    "IR": "IRA",  # Iran Air
    "IS": "IST",  # Island Airlines
    "IT": "TTW",  # Tigerair Taiwan
    "IU": "IUT",  # Air Ivoire
    "IV": "IVJ",  # Wind Jet (defunct)
    "IW": "WIS",  # Wings Air
    "IX": "AXB",  # Air India Express
    "IY": "IYE",  # Yemenia
    "IZ": "AIZ",  # Arkia Israeli Airlines
    "J1": "JON",  # JetBlue (legacy code)
    "J2": "AHY",  # Azerbaijan Airlines
    "J3": "PLR",  # Northwestern Air
    "J4": "BCI",  # Buffalo Airways
    "J5": "ALK",  # Alaska Seaplanes
    "J6": "LRC",  # LAC Colombia
    "J7": "VLG",  # Vueling (legacy)
    "J8": "EXF",  # Berjaya Air
    "J9": "JZR",  # Jazeera Airways
    "JA": "JNA",  # JetBlue (legacy)
    "JB": "HBA",  # Helijet
    "JC": "JCG",  # JAL Express
    "JD": "CAO",  # Beijing Capital Airlines
    "JE": "MMZ",  # Mango Airlines (legacy)
    "JF": "LAT",  # Jet4you
    "JG": "GCY",  # JetGo Australia
    "JH": "NAH",  # Fuji Dream Airlines
    "JI": "EJM",  # Jade Cargo International
    "JJ": "TAM",  # LATAM Brasil
    "JK": "JKK",  # Spanair (defunct)
    "JL": "JAL",  # Japan Airlines
    "JM": "AJM",  # Air Jamaica (defunct)
    "JN": "OMT",  # Excel Airways
    "JO": "JAF",  # JALways
    "JP": "ADR",  # Adria Airways (defunct)
    "JQ": "JST",  # Jetstar Airways
    "JR": "ARO",  # Aero California
    "JS": "KOR",  # Air Koryo
    "JT": "LNI",  # Lion Air
    "JU": "JAT",  # Air Serbia
    "JV": "BLS",  # Bearskin Airlines
    "JW": "VAN",  # Vanilla Air
    "JX": "HJJ",  # Starlux Airlines
    "JY": "EJA",  # NetJets
    "JZ": "SWU",  # Skyways Express
    "K2": "KMV",  # Eurolot
    "K3": "TKN",  # Taquan Air
    "K4": "KSM",  # Kalitta Air
    "K5": "SQH",  # SeaPort Airlines
    "K6": "KHV",  # Cambodia Angkor Air
    "K7": "AKL",  # Air KBZ
    "K8": "KRZ",  # Kan Air
    "K9": "KAJ",  # KrasAvia
    "KA": "HDA",  # Cathay Dragon (defunct)
    "KB": "DRK",  # Drukair
    "KC": "KZR",  # Air Astana
    "KD": "KND",  # KD Avia
    "KE": "KAL",  # Korean Air
    "KF": "BLF",  # Blue1 (defunct)
    "KG": "KGA",  # Aerogaviota
    "KH": "AKL",  # Kyrgyz Airlines
    "KI": "KIS",  # Time Air (defunct)
    "KJ": "KJA",  # British Mediterranean Airways
    "KK": "KKK",  # AtlasGlobal (defunct)
    "KL": "KLM",  # KLM Royal Dutch Airlines
    "KM": "AMC",  # Air Malta
    "KN": "CUA",  # China United Airlines
    "KO": "AER",  # Komiaviatrans
    "KP": "SKK",  # ASKY Airlines
    "KQ": "KQA",  # Kenya Airways
    "KR": "KRE",  # Kam Air
    "KS": "PEN",  # Peninsula Airways
    "KT": "VKT",  # Kolavia
    "KU": "KAC",  # Kuwait Airways
    "KV": "KVA",  # Kavminvodyavia
    "KW": "KWA",  # Carnival Air Lines (defunct)
    "KX": "CAY",  # Cayman Airways
    "KY": "KYE",  # Kunming Airlines
    "KZ": "NCA",  # Nippon Cargo Airlines
    "L1": "LNE",  # LANCO
    "L2": "LBH",  # Labrador Airways
    "L3": "LTM",  # LAN Express
    "L6": "LNM",  # Mauritanian Airlines
    "L7": "LBC",  # Lugansk Airlines
    "L8": "LGX",  # Line Blue
    "LA": "LAN",  # LATAM Airlines (Chile)
    "LB": "BOL",  # Boliviana de Aviacion
    "LC": "LCR",  # Varig Log
    "LD": "AHK",  # Air Hong Kong
    "LE": "LEA",  # Norwegian Long Haul
    "LF": "LFA",  # FlyNordic
    "LG": "LGL",  # Luxair
    "LH": "DLH",  # Lufthansa
    "LI": "LIA",  # LIAT
    "LJ": "JNA",  # Jin Air
    "LK": "RLK",  # Lao Skyway
    "LL": "SAY",  # Miami Air International
    "LM": "GLA",  # Loganair
    "LN": "LAA",  # Libyan Airlines
    "LO": "LOT",  # LOT Polish Airlines
    "LP": "LPE",  # LATAM Peru
    "LQ": "LNQ",  # Lanmei Airlines
    "LR": "LRC",  # Avianca Costa Rica
    "LS": "EXS",  # Jet2 (legacy)
    "LT": "LTU",  # LTU International (defunct)
    "LU": "LXR",  # LATAM Express
    "LV": "LVP",  # Albanian Airlines
    "LW": "NMD",  # Pacific Wings
    "LX": "LXS",  # Swiss International Air Lines
    "LY": "ELY",  # El Al Israel Airlines
    "LZ": "LBG",  # Bellair
    "M1": "MSA",  # MasAir
    "M2": "MNH",  # MHS Aviation
    "M3": "MWM",  # LATAM Cargo Colombia
    "M4": "MLD",  # Mistral Air
    "M5": "MJT",  # Kenmore Air
    "M6": "AMG",  # Amerijet International
    "M7": "MXA",  # Aerohonduras
    "M8": "MKX",  # Skyjet Airlines
    "M9": "MSM",  # Motor Sich Airlines
    "MA": "MAH",  # Malev Hungarian Airlines (defunct)
    "MB": "MLD",  # MNG Airlines
    "MC": "MCC",  # Air Mobility Command
    "MD": "MDG",  # Air Madagascar
    "ME": "MEA",  # Middle East Airlines
    "MF": "CXA",  # Xiamen Airlines
    "MG": "MJV",  # Egyptair Express
    "MH": "MAS",  # Malaysia Airlines
    "MI": "SLK",  # SilkAir (now Singapore Airlines)
    "MJ": "LAP",  # LATAM Paraguay
    "MK": "MAU",  # Air Mauritius
    "ML": "MLW",  # Midway Airlines (defunct)
    "MM": "APJ",  # Peach Aviation
    "MN": "CAW",  # Comair
    "MO": "CAV",  # Calm Air
    "MP": "MPH",  # Martinair
    "MQ": "ENY",  # Envoy Air (American Eagle)
    "MR": "MRT",  # Hunnu Air
    "MS": "MSR",  # EgyptAir
    "MT": "TCX",  # Thomas Cook Airlines
    "MU": "CES",  # China Eastern Airlines
    "MV": "MVA",  # Air Mediterranean
    "MW": "MWL",  # Maya Airways
    "MX": "MXE",  # Mexicana (defunct)
    "MY": "MYA",  # MASwings
    "MZ": "MYD",  # Merpati Nusantara Airlines (defunct)
    "N3": "HLX",  # Holiway
    "N4": "NWD",  # Nord Wind
    "N5": "NVS",  # Nolinor Aviation
    "N6": "NRI",  # Nomad Aviation
    "N7": "NRN",  # Nordic Regional Airlines
    "N8": "NCR",  # National Air Cargo
    "N9": "NAV",  # Nova Air
    "NA": "NAX",  # North American Airlines
    "NB": "SWT",  # Sterling Airlines (defunct)
    "NC": "NCA",  # National Jet Systems
    "ND": "ENA",  # Astral Aviation
    "NE": "NAE",  # Nesma Airlines
    "NF": "AVN",  # Air Vanuatu
    "NG": "LDA",  # Lauda Air (defunct)
    "NH": "ANA",  # All Nippon Airways
    "NI": "PGA",  # Portugalia Airlines
    "NJ": "NJE",  # NetJets Europe
    "NK": "NKS",  # Spirit Airlines
    "NL": "NLS",  # Shaheen Air
    "NM": "NMS",  # Mount Cook Airline
    "NN": "MOV",  # VIM Airlines
    "NO": "NOS",  # Neos
    "NP": "NIA",  # Nile Air
    "NQ": "AJX",  # Air Japan
    "NR": "NRD",  # Pamir Air
    "NS": "OAL",  # Caucasus Airlines
    "NT": "BCN",  # Binter Canarias
    "NU": "JTA",  # Japan Transocean Air
    "NV": "NVA",  # Northwest Airlines (defunct)
    "NW": "NWA",  # Northwest Airlines (now Delta)
    "NX": "AMU",  # Air Macau
    "NY": "NYR",  # Air Iceland Connect
    "NZ": "ANZ",  # Air New Zealand
    "O2": "OLT",  # Overland Airways
    "O3": "OAG",  # SF Airlines
    "O4": "OAB",  # Antrak Air
    "O6": "ONA",  # Avianca Brazil
    "O7": "OZJ",  # Ozjet Airlines
    "OA": "OAL",  # Olympic Air
    "OB": "BOV",  # Boliviana de Aviacion (legacy)
    "OC": "OCA",  # Oriental Air Bridge
    "OD": "MXD",  # Malindo Air (Batik Air Malaysia)
    "OE": "OEA",  # Asia Pacific Airlines
    "OF": "OFM",  # Air Finland
    "OG": "OGE",  # LATAM Airlines (legacy)
    "OH": "COM",  # Comair
    "OI": "OIA",  # Hinterland Aviation
    "OJ": "OJA",  # Fly Jamaica
    "OK": "CSA",  # Czech Airlines
    "OL": "OLT",  # OLT Express
    "OM": "MNG",  # MIAT Mongolian Airlines
    "ON": "RON",  # Air Nauru
    "OO": "SKW",  # SkyWest Airlines
    "OP": "CAP",  # Chalk's Ocean Airways (defunct)
    "OQ": "OQA",  # Chongqing Airlines
    "OR": "TFL",  # TUI Airlines Netherlands
    "OS": "AUA",  # Austrian Airlines
    "OT": "OTB",  # Aeropelican
    "OU": "CTN",  # Croatia Airlines
    "OV": "SVS",  # SAS Connect
    "OW": "OWA",  # Skyward Express
    "OX": "OXF",  # Orient Thai Airlines
    "OY": "OYA",  # Andes Lineas Aereas
    "OZ": "AAR",  # Asiana Airlines
    "P0": "PVD",  # Proflight Zambia
    "P1": "PAT",  # Public Charters
    "P2": "PAA",  # Airkenya Express
    "P3": "PAN",  # Passaredo Transportes Aereos
    "P4": "PRS",  # Aero Lineas Sosa
    "P5": "RPB",  # Wingo (Copa Holdings)
    "P6": "PCV",  # Pascan Aviation
    "P7": "SPR",  # Small Planet Airlines
    "P8": "PFR",  # Pantanal Linhas Aereas
    "P9": "PGP",  # Peruvian Airlines
    "PB": "PBN",  # Air Burkina (legacy)
    "PC": "PGT",  # Pegasus Airlines
    "PD": "POE",  # Porter Airlines
    "PE": "PEV",  # People's Viennaline
    "PF": "PFA",  # Palestinian Airlines
    "PG": "BKP",  # Bangkok Airways
    "PH": "PHW",  # Polynesian Blue
    "PI": "PFB",  # Polar Air Cargo
    "PJ": "SPM",  # Air Saint-Pierre
    "PK": "PIA",  # Pakistan International Airlines
    "PL": "SAP",  # Aeroperu (defunct)
    "PM": "PML",  # Canarias Regional Air
    "PN": "CHB",  # West Air China
    "PO": "PCK",  # Polar Airlines
    "PP": "PPA",  # Jet Aviation
    "PQ": "PQA",  # Airphil Express
    "PR": "PAL",  # Philippine Airlines
    "PS": "AUI",  # Ukraine International Airlines
    "PT": "NMS",  # West Air Sweden
    "PU": "PUA",  # PLUNA (defunct)
    "PV": "LAP",  # St Barth Commuter
    "PW": "PRF",  # Precision Air
    "PX": "ANG",  # Air Niugini
    "PY": "SLM",  # Surinam Airways
    "PZ": "LAP",  # LATAM Paraguay (legacy)
    "Q2": "DQA",  # Maldivian
    "Q3": "MQL",  # Zambia Skyways
    "Q4": "SQS",  # Starbow Airlines
    "Q5": "MLA",  # 40-Mile Air
    "Q6": "COB",  # Aero Condor
    "Q7": "SIF",  # SkyBahamas
    "Q8": "KWT",  # Trans Air Congo
    "Q9": "QFA",  # Frontier Airlines (legacy)
    "QB": "QBA",  # Georgian National Airlines
    "QC": "CRQ",  # Camair-Co
    "QD": "QDA",  # Dobrolet
    "QE": "QEA",  # Crossair (defunct)
    "QF": "QFA",  # Qantas
    "QG": "CTV",  # Citilink
    "QH": "QHA",  # Bamboo Airways
    "QI": "CIM",  # Cimber Air
    "QJ": "LTE",  # LTE International Airways
    "QK": "JZA",  # Jazz Aviation (Air Canada Express)
    "QL": "EAL",  # Aer Lingus UK
    "QM": "MLC",  # Air Malawi
    "QN": "RUK",  # Quantum Air
    "QO": "QOA",  # Origin Pacific Airways
    "QP": "QPA",  # Airkenya
    "QR": "QTR",  # Qatar Airways
    "QS": "TVS",  # SmartWings
    "QT": "RPK",  # TAMPA Cargo
    "QU": "UTA",  # UTair Aviation
    "QV": "LAO",  # Lao Airlines
    "QW": "QWA",  # Blue Wings
    "QX": "QXE",  # Horizon Air
    "QY": "SQC",  # Red Jet Andes
    "QZ": "AWQ",  # AirAsia Indonesia
    "R2": "CRB",  # Orenburg Airlines
    "R3": "SYL",  # Yakutia Airlines
    "R4": "RRV",  # Real Tonga
    "R5": "JAV",  # Jordan Aviation
    "R6": "DNU",  # DOT LT
    "R7": "OCA",  # Aserca Airlines
    "R8": "RKA",  # Kamaka Air
    "R9": "CRJ",  # Camai Air
    "RA": "RNA",  # Nepal Airlines
    "RB": "SYR",  # Syrian Arab Airlines
    "RC": "FLI",  # Atlantic Airways
    "RD": "RDA",  # Ryan Air (not Ryanair)
    "RE": "REA",  # Aer Arann (Aer Lingus Regional)
    "RF": "VDA",  # Aeroflot Cargo
    "RG": "VRG",  # Varig (defunct)
    "RH": "RHN",  # Rob's Heli Charter
    "RI": "RIN",  # Mandala Airlines
    "RJ": "RJA",  # Royal Jordanian
    "RK": "RKA",  # Air Afrique (defunct)
    "RL": "ABG",  # Royal Falcon
    "RM": "RMV",  # Muk Air
    "RN": "RNV",  # Runs Air
    "RO": "ROT",  # TAROM
    "RP": "SDT",  # Chautauqua Airlines
    "RQ": "RQA",  # Kam Air
    "RR": "RRR",  # Royal Air Force
    "RS": "SHR",  # Sky Regional Airlines
    "RT": "RTA",  # RUTACA Airlines
    "RU": "CFG",  # TUIfly (legacy)
    "RV": "RVE",  # Air Canada Rouge
    "RW": "RPA",  # Republic Airways
    "RX": "RXA",  # Regent Airways
    "RY": "JAB",  # Jiangxi Air
    "RZ": "RZA",  # Sansa Airlines
    "S0": "SRQ",  # Aerolineas Sosa
    "S1": "SNA",  # Surinam Airways (legacy)
    "S2": "SAG",  # SpiceJet
    "S3": "BRS",  # Santa Barbara Airlines
    "S4": "RZO",  # SATA International
    "S5": "SJY",  # Shuttle America
    "S6": "AZS",  # Sunrise Airlines
    "S7": "SBI",  # S7 Airlines (Siberia)
    "S8": "SRK",  # Subtropica
    "S9": "SHY",  # Starbow Airlines
    "SA": "SAA",  # South African Airways
    "SB": "ACI",  # Aircalin
    "SC": "CDG",  # Shandong Airlines
    "SD": "SUD",  # Sudan Airways
    "SE": "SEH",  # XL Airways France
    "SF": "SFR",  # Tassili Airlines
    "SG": "SEJ",  # SpiceJet (legacy)
    "SH": "SHA",  # Sharp Airlines
    "SI": "SIL",  # Skynet Airlines
    "SJ": "SJM",  # Sriwijaya Air
    "SK": "SAS",  # Scandinavian Airlines
    "SL": "THA",  # Thai Lion Air (legacy)
    "SM": "SMS",  # Air Cairo
    "SN": "DAT",  # Brussels Airlines
    "SO": "SOO",  # Salsa d'Haiti
    "SP": "SAT",  # SATA Air Acores
    "SQ": "SIA",  # Singapore Airlines
    "SR": "SWR",  # Swiss Air (defunct)
    "SS": "CRL",  # Corsair International
    "ST": "GMI",  # Germania (legacy)
    "SU": "AFL",  # Aeroflot
    "SV": "SVA",  # Saudi Arabian Airlines (Saudia)
    "SW": "NMB",  # Air Namibia (defunct)
    "SX": "SXD",  # SkyWork Airlines
    "SY": "SCX",  # Sun Country Airlines
    "SZ": "CQH",  # Sichuan Airlines (legacy)
    "T0": "TNO",  # TACA Peru
    "T2": "TLR",  # Thai Air Cargo
    "T3": "TRE",  # Eastern Airways
    "T4": "TPA",  # TRIP Linhas Aereas
    "T5": "TUA",  # Turkmenistan Airlines
    "T6": "TMK",  # Aircompany Tomsk Avia
    "T7": "TJT",  # Twin Jet
    "T8": "TKF",  # STP Airways (legacy)
    "T9": "TNT",  # Valan Air Cargo
    "TA": "TAI",  # Taca International Airlines (Avianca)
    "TB": "TUI",  # TUI fly Belgium
    "TC": "ATC",  # Air Tanzania
    "TD": "SDR",  # Atlantis European Airways
    "TE": "FIN",  # FlyLAL (defunct)
    "TF": "SCW",  # Braathens Regional (Malmo Aviation)
    "TG": "THA",  # Thai Airways International
    "TH": "THA",  # Transmile Air Services
    "TI": "TIB",  # Tailwind Airlines
    "TJ": "TOJ",  # Tradewind Aviation
    "TK": "THY",  # Turkish Airlines
    "TL": "ANO",  # Airnorth
    "TM": "LAM",  # LAM Mozambique Airlines
    "TN": "TAH",  # Air Tahiti Nui
    "TO": "TVF",  # Transavia France
    "TP": "TAP",  # TAP Air Portugal
    "TQ": "TQL",  # Tandem Aero
    "TR": "TGW",  # Scoot
    "TS": "TSC",  # Air Transat
    "TT": "TGW",  # TigerAir Australia (defunct)
    "TU": "TAR",  # Tunisair
    "TV": "HHN",  # TV Globo (defunct)
    "TW": "TWB",  # T'way Air
    "TX": "FWI",  # Air Caraibes
    "TY": "TPC",  # Air Caledonie
    "TZ": "AWE",  # ATA Airlines (defunct)
    "U2": "EZY",  # easyJet
    "U3": "UKA",  # Avies
    "U4": "UKR",  # Progress Multitrade
    "U5": "FSL",  # USA 3000 Airlines (defunct)
    "U6": "SVR",  # Ural Airlines
    "U7": "UPA",  # USA Jet Airlines
    "U8": "RKT",  # Armavia (defunct)
    "U9": "TAK",  # Tatarstan Airlines
    "UA": "UAL",  # United Airlines
    "UB": "UBA",  # Myanma Airways
    "UC": "LCO",  # LAN Cargo
    "UD": "UDA",  # Hex'Air
    "UE": "UEA",  # United Eagle Airlines
    "UF": "UKM",  # UM Airlines
    "UG": "TUX",  # Sevenair
    "UH": "USB",  # AtlasJet Ukraine
    "UI": "UIA",  # Eurocypria (defunct)
    "UJ": "JAV",  # AlMasria Universal Airlines
    "UK": "VTI",  # Vistara
    "UL": "ALK",  # SriLankan Airlines
    "UM": "UZA",  # Air Zimbabwe
    "UN": "TSO",  # Transaero (defunct)
    "UO": "HKE",  # Hong Kong Express
    "UP": "BHS",  # Bahamasair
    "UQ": "UQA",  # Urumqi Air
    "UR": "URC",  # Ukraine Cargo Airways
    "US": "USA",  # US Airways (now American)
    "UT": "UTA",  # UTair Aviation (legacy)
    "UU": "REU",  # Air Austral
    "UV": "UVA",  # El Aguila Airlines
    "UW": "UWA",  # Perimeter Airlines
    "UX": "AEA",  # Air Europa
    "UY": "UYC",  # Cameroon Airlines
    "UZ": "BRQ",  # Buraq Air
    "V0": "VCV",  # Conviasa
    "V2": "VDA",  # Aero VIP
    "V3": "KRP",  # Carpatair (legacy)
    "V4": "VRE",  # Vensecar Internacional
    "V5": "VDA",  # Aerovias DAP
    "V6": "VEC",  # ViajerosCharter
    "V7": "VMT",  # Volotea
    "V8": "VRE",  # ATRAN Cargo (legacy)
    "V9": "VKO",  # Avia Traffic
    "VA": "VOZ",  # Virgin Australia
    "VB": "VIV",  # VivaAerobus
    "VC": "VCA",  # Voyageur Airways
    "VD": "VDA",  # Air Liberte
    "VE": "VLE",  # Venezuelana
    "VF": "VFR",  # Valuair (defunct)
    "VG": "VLM",  # VLM Airlines
    "VH": "VHA",  # Aeropostal Alas de Venezuela
    "VI": "VIA",  # Volga-Dnepr Airlines (passenger)
    "VJ": "VJC",  # VietJet Air
    "VK": "VKB",  # Air Tungaru
    "VL": "VLR",  # Med-View Airline
    "VM": "VMA",  # Vistamar Airlines
    "VN": "HVN",  # Vietnam Airlines
    "VO": "TYR",  # Tyrolean Airways (defunct)
    "VP": "VPA",  # VASP (defunct)
    "VQ": "VQA",  # Novoair
    "VR": "TCV",  # TACV Cabo Verde Airlines
    "VS": "VIR",  # Virgin Atlantic
    "VT": "VTA",  # Air Tahiti
    "VU": "VUA",  # Vuela Cuba
    "VV": "AEW",  # Aerosvit Airlines (defunct)
    "VW": "TAO",  # Aeromar
    "VX": "VRD",  # Virgin America (now Alaska)
    "VY": "VLG",  # Vueling Airlines
    "VZ": "THD",  # Thai Vietjet Air
    "W2": "WTA",  # Flexflight
    "W3": "WRA",  # Arik Air
    "W4": "WLX",  # LC Peru
    "W5": "IRM",  # Mahan Air
    "W6": "WZZ",  # Wizz Air
    "W7": "WSW",  # Wings of Lebanon
    "W8": "WCA",  # Cargojet Airways
    "W9": "WEA",  # Wizz Air UK
    "WA": "KLC",  # KLM Cityhopper
    "WB": "RWD",  # RwandAir
    "WC": "INL",  # Islena De Inversiones
    "WD": "AWD",  # Amsterdam Airlines
    "WE": "THD",  # Thai Smile
    "WF": "WIF",  # Wideroe
    "WG": "SWG",  # Sunwing Airlines
    "WH": "CRH",  # China Northwest Airlines (defunct)
    "WI": "WAI",  # White Airways
    "WJ": "LAL",  # Air Labrador
    "WK": "WDR",  # Edelweiss Air
    "WL": "WLA",  # Aeroperlas
    "WM": "WIA",  # Winair
    "WN": "SWA",  # Southwest Airlines
    "WO": "WOA",  # World Airways (defunct)
    "WP": "MKU",  # Island Air (Hawaii, defunct)
    "WQ": "WQA",  # Romavia
    "WR": "WRA",  # WestJet Encore
    "WS": "WJA",  # WestJet
    "WT": "NIG",  # Wasaya Airways
    "WU": "WUA",  # Wuhan Airlines
    "WV": "WVA",  # Swe-Fly
    "WW": "BMI",  # bmi (legacy)
    "WX": "BCY",  # CityJet
    "WY": "OMA",  # Oman Air
    "WZ": "RWZ",  # Red Wings Airlines
    "X2": "XAA",  # Airarabia Egypt (legacy)
    "X3": "TUI",  # TUI fly Deutschland
    "X4": "XAB",  # Air Excursions
    "X5": "XFR",  # Afric Aviation
    "X7": "XSB",  # Sun Air (South Africa)
    "X8": "XEL",  # Shanxi Airlines (legacy)
    "X9": "XSB",  # Flexflight
    "XC": "CAI",  # Corendon Airlines
    "XE": "CHQ",  # Expressjet (legacy)
    "XF": "VLK",  # Vladivostok Air
    "XG": "SHG",  # Sunexpress Germany
    "XJ": "TAX",  # Thai AirAsia X
    "XK": "CCM",  # Air Corsica
    "XL": "LNE",  # LATAM Ecuador
    "XM": "XMA",  # Alitalia Express (defunct)
    "XN": "XNE",  # Xpressair
    "XO": "XOA",  # Servicios Ejecutivos Continentales
    "XP": "CXP",  # Xtra Airways
    "XQ": "SXS",  # SunExpress
    "XR": "CXR",  # Condor (legacy)
    "XS": "XSA",  # SITA (defunct)
    "XT": "XTA",  # Indonesia AirAsia Extra
    "XU": "XUA",  # African Express Airways
    "XV": "XVA",  # BVI Airways
    "XW": "NXS",  # NokScoot
    "XY": "KNE",  # flynas
    "XZ": "SZA",  # Congo Airways
    "Y2": "YEA",  # Yangtze River Express
    "Y4": "VOI",  # Volaris
    "Y5": "GHE",  # Golden Myanmar Airlines
    "Y6": "YGA",  # Yanair
    "Y7": "TYA",  # NordStar Airlines
    "Y8": "YZR",  # Pascan Aviation (legacy)
    "Y9": "IRK",  # Kish Air
    "YC": "FRK",  # Yamal Airlines
    "YD": "YDA",  # Mauritania Airlines International
    "YE": "YEA",  # Yan Air
    "YI": "YIA",  # Yellow Air Taxi
    "YJ": "YJA",  # Asian Wings Airways
    "YK": "CAY",  # Avia Traffic Company (legacy)
    "YL": "LLM",  # Yamal Airlines (legacy)
    "YM": "MGX",  # Montenegro Airlines (defunct)
    "YN": "CRQ",  # Air Creebec
    "YO": "HMR",  # Heli Air Monaco (legacy)
    "YP": "YPA",  # Airstars
    "YQ": "TAY",  # TAY Airlines
    "YR": "SYR",  # SYRIANAIR (legacy)
    "YS": "RGN",  # Régional
    "YT": "YTA",  # Yeti Airlines
    "YU": "MMZ",  # EuroAtlantic Airways
    "YV": "MES",  # Mesa Airlines
    "YW": "ANE",  # Air Nostrum
    "YX": "RPA",  # Republic Airways (United Express)
    "YZ": "YZA",  # Alas Uruguay
    "Z2": "PAL",  # Philippines AirAsia
    "Z3": "ZAA",  # Promech Air
    "Z4": "ZAB",  # Zoom Airlines (defunct)
    "Z5": "GMG",  # GMG Airlines
    "Z6": "ZAC",  # Dniproavia
    "Z7": "ADZ",  # Amaszonas Uruguay
    "Z8": "AZN",  # Amaszonas
    "Z9": "ZAF",  # Bek Air
    "ZA": "ZAA",  # AccessRail
    "ZB": "MON",  # Monarch Airlines (defunct)
    "ZC": "ZCA",  # Korongo Airlines
    "ZD": "ZDA",  # EWA Air
    "ZE": "ZEA",  # Arcus-Air
    "ZF": "ZFA",  # Zhejiang Loong Airlines
    "ZG": "ZGA",  # Viva Air Colombia
    "ZH": "CSZ",  # Shenzhen Airlines
    "ZI": "AAF",  # Aigle Azur (defunct)
    "ZJ": "ZJA",  # Zambezi Airlines
    "ZK": "GLA",  # Great Lakes Airlines (defunct)
    "ZL": "RXA",  # Regional Express (Rex)
    "ZM": "ZMA",  # Air Manas
    "ZN": "ZNA",  # Naysa
    "ZO": "ZOA",  # Zagros Airlines
    "ZP": "ZPA",  # Silk Way West Airlines
    "ZQ": "LOC",  # German Wings (defunct)
    "ZR": "MKA",  # Muk Air (legacy)
    "ZS": "AZS",  # Azzurra Air
    "ZT": "ZTA",  # Titan Airways
    "ZV": "ZVA",  # V Air
    "ZW": "AWI",  # Air Wisconsin
    "ZX": "ZXA",  # Air Georgian
    "ZY": "ZYA",  # Ada Air
}

# Maps regional/operating carrier ICAO -> marketing carrier ICAO
# Used when ADS-B callsign doesn't match MSP departure table directly
OPERATING_TO_MARKETING = {
    "SKW": "DAL",  # SkyWest -> Delta, United, American, Alaska
    "FLG": "DAL",  # Endeavor Air -> Delta
    "RPA": "UAL",  # Republic Airways -> United, American
    "GJS": "UAL",  # GoJet -> United
    "UCA": "UAL",  # CommutAir -> United
    "MES": "UAL",  # Mesa Airlines -> United, American
    "AWI": "AAL",  # Air Wisconsin -> American
    "ENY": "AAL",  # Envoy Air -> American
    "CPZ": "UAL",  # Compass Airlines -> United (defunct but may still appear)
    "QXE": "ASA",  # Horizon Air -> Alaska
    "JZA": "ACA",  # Jazz Aviation -> Air Canada
}
