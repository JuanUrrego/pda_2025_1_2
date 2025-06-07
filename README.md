# pda_2025_1_2

# 🏆 Workflow de Scraping de Premios Nobel con GitHub Actions y Docker

Este proyecto implementa un flujo automatizado de extracción de datos sobre mujeres ganadoras del Premio Nobel, utilizando GitHub Actions para CI/CD, contenerización con Docker y gestión segura de secretos.

---

## ⚙️ Estructura del Flujo de Trabajo

El proceso se gestiona mediante un único workflow en GitHub Actions: `accionables.yml`, que realiza los siguientes pasos:

### 1. Preparación del Entorno
- Ejecuta el flujo en un entorno Linux (`ubuntu-latest`).
- Configura Python 3.9 y sus dependencias con `setup.py`.

### 2. Login y Contenerización con Docker
- Inicia sesión en Docker Hub usando los secretos `DOCKER_USERNAME` y `DOCKER_TOKEN`.
- Construye una imagen Docker (`python-hello`) que incluye el script de scraping.
- Ejecuta la imagen para generar automáticamente el archivo CSV con los datos extraídos.

### 3. Commit Automático
- Si hay cambios generados por el scraping, estos se versionan automáticamente en el repositorio mediante `git-auto-commit-action`.

---

## 🔒 Requisitos para la Configuración

Debes configurar los siguientes **secretos** en GitHub para habilitar el workflow:

- `DOCKER_USERNAME`: Usuario de Docker Hub.
- `DOCKER_TOKEN`: Token de acceso a Docker Hub.

---

## 🗂️ Estructura del Proyecto

```
pda_2025_1_2/
├── .github/
│   └── workflows/
│       └── accionables.yml
├── src/
│   └── edu_pad/
│       └── static/
│           └── main.py
├── setup.py
├── Dockerfile
└── README.md
```

---

## 🚀 Instalación y Ejecución

1. Clona este repositorio:  
   `git clone https://github.com/JuanUrrego/pda_2025_1_2.git`

2. Configura los secretos necesarios en GitHub.

3. El flujo `accionables.yml` se ejecutará automáticamente al hacer push al branch `main` o de forma manual desde la interfaz de GitHub Actions.

---

## 🌟 Características Principales

- **Automatizado**: El scraping, versionado y despliegue se ejecutan sin intervención manual.
- **Contenerizado**: El proceso corre dentro de una imagen Docker reproducible.
- **Seguro**: Gestión de credenciales mediante secretos de GitHub.
- **Trazable**: Cada ejecución queda registrada y versionada automáticamente.

---

## 🛠️ Personalización

- Puedes modificar `main.py` si deseas extraer más columnas u otras fuentes.
- Ajusta el `Dockerfile` si necesitas nuevas dependencias o rutas de ejecución.
- Cambia la frecuencia o condiciones del flujo editando `accionables.yml`.
