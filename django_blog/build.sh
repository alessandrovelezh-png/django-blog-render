#!/usr/bin/env bash
# Ejecuta el build y migraciones en el servidor de Render
set -o errexit

# Recopilar archivos estáticos
python manage.py collectstatic --no-input

# Aplicar migraciones de la base de datos
python manage.py migrate