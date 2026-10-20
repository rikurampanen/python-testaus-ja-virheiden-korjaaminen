from pelitoiminnot import vahingoita, paranna, lisaa_pisteet


def main():
    terveys = 100
    pisteet = 10

    print("Pelin alussa")
    print("Terveys:", terveys)
    print("Pisteet:", pisteet)

    terveys = vahingoita(terveys, 25)
    terveys = paranna(terveys, 10)
    pisteet = lisaa_pisteet(pisteet, 5)

    print("\nToimintojen jälkeen")
    print("Terveys:", terveys)
    print("Pisteet:", pisteet)


if __name__ == "__main__":
    main()