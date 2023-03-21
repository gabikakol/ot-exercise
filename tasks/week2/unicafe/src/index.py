from maksukortti import Maksukortti
from kassapaate import Kassapaate


def main():
    unicafe_exactum = Kassapaate()
    kortti = Maksukortti(10000)

    unicafe_exactum.eat_cheap_card(kortti)

    print(unicafe_exactum.cheap)
    print(kortti)


if __name__ == "__main__":
    main()
