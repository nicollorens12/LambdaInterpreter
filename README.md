# LambdaInterpreter

Practica LP Q2 2022-2023
Nicolas Llorens Somalo 

## Com executar l'interpretador?
Per executar la pràctica només cal executar aquesta comanda:
```
python3 achurch.py
```
## Particulartiats del interpretador
Seguint la sintaxi de les primeres tasques, els prompts s'han de fer amb un ? abans de la expressió.

La gramàtica no permet en el mateix prompt la concatenació de macros amb notació infixa, es a dir, no esta contemplat per exemple mes de dos macros:
```
? N2 + N3 + N2
```
En canvi es contempla la notació infixa d'aquesta forma:
```
? N2 + N3
```
Si està contemplat en canvi la concatenació de macros com:
```
? NOT NOT NOT NOT NOT TRUE
```

## Com utilizar el bot @NicoLambda_bot (LambdaInterpreter)

Un cop achurch.py estigui en execució hauriem de començar la conversa amb el bot amb la comanda /start.

Això prepara el bot per una nova conversa. En el cas de voler començar la conversa de nou també es pot utilitzar aquesta comanda per buidar totes les macros existents i restablir el estat inicial.

El bot enten aquestes entrades (mostrades al fer /help):
/start - Prepara al bot per una nova conversa.
/help - Mostra com utilitzar el bot.
/author - Mostra el autor de la pràctica.
/macros - Mostra las macros que te guardades el sistema.
? Expressió - Donada una expressió fara les reduccions i conversions pertinets mostrants els grafics en cada pa.