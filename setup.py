from setuptools import setup, find_packages

setup(
    name="edu_pad",
    version="0.0.1",
    author="Juan Diego UG",
    author_email="juan.urrego@est.iudigital.edu.co",
    description="Curso programación para analisis de datos 2025-1",
    py_modules=["actividad1","actividad2"],
    install_requires=[
        "pandas",
        "requests",
        "BeautifulSoup",
        "streamlit",
        "datetime",
        "openpyxl"

    ]


)
