#!/bin/bash

carpetas=(
  "01 Estructuras Secuenciales"
  "02 Trabajo Colaborativo"
  "03 Estructuras Condicionales"
  "04 Estructuras Repetitivas"
  "05 Funciones"
  "06 Datos complejos"
  "07 Manejo de errores"
)

contenido="😄 ¡Bienvenid@ a Programación 1!"

for carpeta in "${carpetas[@]}"
do
  mkdir -p "$carpeta"
  echo "$contenido" > "$carpeta/README.md"
done

echo "✅ Carpetas y archivos creados con éxito."
