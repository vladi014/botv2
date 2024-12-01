
from crawler.tenis_bet import ThreadBet
from crawler.tenis_codere import ThreadCodere
from crawler.tenis_betFair import ThreadBetFair
from stats.estadistica import comprobar_cotizaciones
import queue

def main():
    cola1 = queue.Queue()
    cola2 = queue.Queue()
    cola3 = queue.Queue()
    cola4 = queue.Queue()
    cola5 = queue.Queue()

    # Example initialization for testing
    betFair = ThreadBetFair(cola1, cola2, username="user_betfair", password="password_betfair")
    codere = ThreadCodere(cola1, cola2, cola5, cola4, username="user_codere", password="password_codere")

    betFair.start()
    codere.start()

    # Process loop (example)
    while True:
        try:
            data_betfair = cola3.get()
            data_codere = cola5.get()
            results = comprobar_cotizaciones(data_betfair, data_codere, maximo=100)
            print(f"Results: {results}")
        except KeyboardInterrupt:
            print("Stopping threads...")
            betFair.seguir = False
            codere.seguir = False
            break

if __name__ == "__main__":
    main()
