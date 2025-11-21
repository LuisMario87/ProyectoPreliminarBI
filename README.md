📊 Proyecto de Business Intelligence — Análisis de Ventas Farmacéuticas

Autor: Luis Mario Ayala Castellanos
Curso: Temas Selectos en Inteligencia de Negocios (TSII)
Fecha: Noviembre 2025

📌 Descripción del Proyecto

Este repositorio contiene el desarrollo completo de un sistema de Business Intelligence orientado al análisis de ventas de una farmacia. El proyecto incluye un pipeline ETL reproducible, análisis exploratorio de datos, cálculo de KPIs estratégicos y un dashboard interactivo construido con Streamlit.

El dataset contiene 30,000 transacciones farmacéuticas, con información de clientes, productos, ciudades, fechas y montos asociados.

🎯 Objetivo General

Desarrollar un sistema de BI que permita transformar datos crudos de transacciones farmacéuticas en información estratégica para apoyar la toma de decisiones operativas, comerciales y analíticas dentro del sector farmacéutico.

🧠 Objetivos SMART

Procesar y limpiar el 100% del dataset mediante un pipeline ETL reproducible antes del 10/oct/2025.

Calcular al menos 6 KPIs operativos esenciales antes del análisis exploratorio.

Diseñar un dashboard interactivo de 4 visualizaciones clave antes del 28/nov/2025.

Documentar todo el proceso en un informe final de 15–20 páginas.

Garantizar la reproducibilidad del proceso mediante scripts y archivos configurables.

🗂️ Arquitectura del Proyecto

El proyecto se divide en cuatro componentes principales:

ETL (Extract, Transform, Load)

Limpieza de datos

Conversión de tipos

Cálculo de TotalVenta

Métricas de calidad

Exportación a CSV procesado

Notebook de Análisis

Exploración

Visualización

KPIs

Narrativa ejecutiva

Dashboard con Streamlit

Ventas por categoría

Ventas semanales

Top 5 productos

Heatmap día–mes

Documento Final

Marco teórico

Caso

KPIs

ETL

Dashboard

Recomendaciones

📁 Estructura del Repositorio
ProyectoBI_Farmacia/
│
├── data/
│   ├── README.md
│   └── datosCompletosProcesados.csv
│
├── scripts/
│   └── ETL_Final.py
│
├── notebooks/
│   └── analisis_farmaceutico.ipynb
│
├── dashboard/
│   └── dashboard_app.py
│
├── reportes/
│   └── EntregaFinal.pdf
│
└── README.md

⚙️ Cómo ejecutar el ETL

Clonar el repositorio:

git clone https://github.com/LuisMario87/ProyectoPreliminarBI.git
cd ProyectoPreliminarBI


Ejecutar el ETL:

python scripts/ETL_Final.py


El archivo limpio se guardará como:

/data/datosCompletosProcesados.csv

📊 Cómo abrir el notebook
jupyter notebook notebooks/analisis_farmaceutico.ipynb

🖥️ Cómo correr el Dashboard (Streamlit)
streamlit run dashboard/dashboard_app.py


Esto abrirá el dashboard interactivo en el navegador.

📦 Requisitos
Python 3.10+
pandas
matplotlib
seaborn
streamlit
numpy


Instalación rápida:

pip install -r requirements.txt


(opcional, si quieres crear requirements.txt mañana)

🔒 Nota sobre datos RAW

El dataset original de 30,000 registros no se incluye por privacidad/tamaño.
Sin embargo, se proporciona el archivo procesado y un archivo readme dentro de data/ con instrucciones.

👤 Autor

Luis Mario Ayala Castellanos
Estudiante de Ingeniería – UDLAP
Proyecto académico para TSII (Business Intelligence)
