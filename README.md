# sensor-project
Django project op Raspberry Pi met GPIO integratie

Django Channels heeft een werkend redis-server nodig om te functioneren. 

Start project als volgt:
- Open een terminal en start redis-server
- Open een volgende terminal, ga naar de project folder en start ./runsensor // dit start een channel die via een callback script reageert op het indrukken van een sensor.
- Open een volgende terminal, ga naar de project folder en start ./runserver om de Django dev server te starten
# raspberry_django_channels
