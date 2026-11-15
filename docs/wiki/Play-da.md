[English](Play) · **Dansk** · [Bahasa Melayu](Play-ms)

# Spil

## Start spillet

Kør en af kommandoerne, mens det virtuelle miljø er aktivt:

```bash
python -m rock_paper_scissors
```

```bash
rock-paper-scissors
```

## Regler

Skriv `0` for sten, `1` for papir eller `2` for saks.

| Du | Computeren | Resultat |
| --- | --- | --- |
| Sten | Saks | Du vinder |
| Saks | Papir | Du vinder |
| Papir | Sten | Du vinder |
| Samme valg | Samme valg | Uafgjort |

Alt andet input (for eksempel `3` eller `rock`) udskriver en besked og afslutter runden med et nederlag; spillet går aldrig ned på forkert input.

## Farve

Titlen er farvet, når uddata er en terminal. Sæt miljøvariablen `NO_COLOR` for at slå farve fra.

Se også [Installation](Install-da) og [Arkitektur](Architecture-da).
