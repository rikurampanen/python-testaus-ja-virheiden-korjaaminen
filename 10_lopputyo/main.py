from pelitoiminnot import (
    vahingoita,
    paranna,
    lisaa_kokemusta,
    laske_taso,
)


def main():
    terveys = 100
    kokemus = 0

    print("Seikkailu alkaa!")
    print("Terveys:", terveys)
    print("Kokemus:", kokemus)
    print("Taso:", laske_taso(kokemus))

    terveys = vahingoita(terveys, 25)
    kokemus = lisaa_kokemusta(kokemus, 120)
    terveys = paranna(terveys, 10)

    print("\nSeikkailun jälkeen")
    print("Terveys:", terveys)
    print("Kokemus:", kokemus)
    print("Taso:", laske_taso(kokemus))


if __name__ == "__main__":
    main()