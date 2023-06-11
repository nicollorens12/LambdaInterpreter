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
