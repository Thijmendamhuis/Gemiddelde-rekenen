def bereken_minimaal_cijfer():
  # Vraag de gebruiker om het aantal cijfers in te voeren
  aantal_cijfers = int(input("Voer het aantal cijfers in: "))

  totaal_punten = 0
  totaal_weging = 0

  # Loop door alle cijfers en wegingen
  for i in range(aantal_cijfers):
      # Vraag de gebruiker om het cijfer in te voeren
      cijfer = float(input(f"Voer cijfer {i + 1} in: "))

      # Vraag de gebruiker om de weging in te voeren
      weging = float(input(f"Voer weging voor cijfer {i + 1} in: "))

      # Bereken de punten en weging
      totaal_punten += cijfer * weging
      totaal_weging += weging

  # Vraag de gebruiker om de weging van de eerstvolgende toets in te voeren
  weging_volgende_toets = float(input("Voer de weging van de eerstvolgende toets in: "))

  # Bereken het minimaal benodigde cijfer om een voldoende te (blijven) staan
  minimaal_cijfer = (5.5 * (totaal_weging + weging_volgende_toets) - totaal_punten) / weging_volgende_toets

  # Geef het minimaal benodigde cijfer weer aan de gebruiker
  print(f"Je moet minimaal een {minimaal_cijfer} halen om voldoende te (blijven) staan.")

# Roep de functie aan om het programma uit te voeren
bereken_minimaal_cijfer()
