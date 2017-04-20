# m2m modem
Scripts python per comunicar dades SERIAL via modems m2m amb targeta SIM via GPRS

## Objectiu:
Connectar ordinador (aparell 1) i un comptador intel·ligent d'electricitat (aparell 2)

## Estat
En desenvolupament

## Esquema
```
Passem de:
+-----------+                 +-----------+
| aparell 1 |---cable-RS232---| aparell 2 |
+-----------+                 +-----------+

A:
+-----------+      +----------+          +-----------+                 +-----------+
| aparell 1 |------| internet |~~~GPRS~~~| modem m2m |---cable-RS232---| aparell 2 |
+-----------+      +----------+          +-----------+                 +-----------+
```
