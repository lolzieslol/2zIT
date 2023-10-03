## kopiert fra:
#https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/2-objektorientert-programmering/2b-systemutvikling/testing

verdier_inn = [32.0, 50.0, 68.0, 86.0, 104.0, 122.0]
verdier_forventet = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

def fahrenheit_til_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * (5/9)
  return celsius

for x in range(len(verdier_inn)):
  if fahrenheit_til_celsius(verdier_inn[x]) == verdier_forventet[x]:
    print(f"Funksjonen gir forventet verdi for {verdier_inn[x]} grader fahrenheit.")
  else:
    print(f"Funksjonen gir ikke forventet verdi for {verdier_inn[x]} grader fahrenheit.")
    
#TODO: se på unittest

