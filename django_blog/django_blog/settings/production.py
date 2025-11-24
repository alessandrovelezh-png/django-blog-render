# django_blog/settings/production.py

import os
import dj_database_url

# Importa explícitamente la variable DATABASES de base.py
from .base import *
from .base import DATABASES
# Aunque el wildcard importa, re-importar la variable la define de forma más robusta.

# Lee la clave secreta del entorno de Render
SECRET_KEY = os.environ.get('SECRET_KEY', 'default-safe-key-if-not-found')

# Nota: Si el valor de tu SECRET_KEY en base.py era un valor hardcodeado,
# esta línea SOBREESCRIBIRÁ el valor en el entorno de Render.

# ----------------------- 1. CONFIGURACIÓN BÁSICA ------------------------

# IMPORTANTE: Desactivar DEBUG para producción
DEBUG = False 

# Permite que la configuración de ALLOWED_HOSTS de base.py sea modificada
# Render inyecta la variable RENDER_EXTERNAL_HOSTNAME
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME) # ALLOWED_HOSTS ya viene de base.py
    
# ----------------------- 2. ARCHIVOS ESTÁTICOS (WHITENOISE) -----------------------

# Asegúrate de que Django/WhiteNoise use el storage correcto
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --------------------------- 3. BASE DE DATOS (POSTGRES) --------------------------

# Sobrescribe la configuración de la base de datos para usar la URL de Render
# NOTA: La variable DATABASES ya está definida gracias a la importación explícita de arriba.
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600,
        ssl_require=True, # <--- ¡Asegura que SSL sea requerido!
        conn_health_checks=True,
    )