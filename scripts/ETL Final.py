
# ===========================================
# ETL Final - Proyecto BI Farmacéutico
# Autor: Luis Mario Ayala Castellanos
# Fecha: Noviembre 2025
# Descripción:
#   Pipeline ETL reproducible para el dataset
#   de transacciones farmacéuticas (30,000+ filas).
#   Incluye: carga, limpieza, transformación,
#   verificación de calidad de datos y exportación.
# ===========================================

import pandas as pd
import os

# ========================
# 1. EXTRACT
# ========================
def load_data(path):
    """
    Carga el archivo Excel con los datos RAW.
    
    Parámetros:
        path (str): Ruta al archivo Excel sin procesar.
    Retorna:
        DataFrame con los datos cargados.
    """
    print(">> Cargando archivo RAW...")
    df = pd.read_excel(path)
    print(">> Archivo cargado correctamente.")
    print(f">> Filas leídas: {len(df)}")
    return df


# ========================
# 2. TRANSFORM
# ========================
def transform_data(df):
    """
    Realiza limpieza, corrección de tipos y cálculos derivados.
    
    Operaciones:
      - Limpieza de nombres de columnas
      - Conversión de fechas
      - Conversión de numéricos
      - Cálculo de TotalVenta
      - Validación básica de calidad de datos
    """
    print("\n>> Iniciando transformaciones...")

    # ---- Limpieza de nombres de columnas ----
    df.columns = df.columns.str.strip()

    # ---- Corrección de fechas ----
    df["FechaCompra"] = pd.to_datetime(df["FechaCompra"], errors="coerce")

    # ---- Manejo de numéricos ----
    df["Cantidad"] = pd.to_numeric(df["Cantidad"], errors="coerce")
    df["PrecioUnitario"] = pd.to_numeric(df["PrecioUnitario"], errors="coerce")

    # ---- Cálculo de TotalVenta ----
    df["TotalVenta"] = (df["Cantidad"] * df["PrecioUnitario"]).round(2)

    print(">> Transformación realizada correctamente.")

    return df


# ========================
# 3. DATA QUALITY REPORT
# ========================
def data_quality_report(df):
    """
    Genera un reporte de calidad de datos con:
      - Nulos por columna
      - Número de duplicados
      - Estadísticas básicas para detectar outliers
    """

    print("\n>> Verificando calidad de los datos...")

    nulos = df.isnull().sum()
    duplicados = df.duplicated().sum()
    estadisticas = df.describe(include='all')

    print("\n--- MÉTRICAS DE CALIDAD DE DATOS ---")
    print("Nulos por columna:")
    print(nulos)

    print(f"\nDuplicados totales: {duplicados}")

    print("\nEstadísticas básicas (detección de valores fuera de rango):")
    print(estadisticas)

    print("\n>> Calidad de datos revisada.\n")

    # También devolvemos los valores para documentarlos en el reporte final
    return nulos, duplicados, estadisticas


# ========================
# 4. LOAD
# ========================
def save_processed_data(df, output_path):
    """
    Exporta el dataFrame procesado como csv limpio y reproducible
    """
    df.to_csv(output_path, index=False, encoding="utf-8", float_format="%.2f")
    print(f">> Archivo procesado guardado en:\n   {output_path}")


# ========================
# 5. PIPELINE PRINCIPAL
# ========================
if __name__ == "__main__":
    
    # Ruta RAW completa
    raw_path = "C:\\Users\\luism\\OneDrive\\Documentos\\A. 9no Semestre\\Temas 2\\Procesamiento de datos\\datosCompletos.xlsx"

    # Ruta de salida
    output_path = "C:\\Users\\luism\\OneDrive\\Documentos\\A. 9no Semestre\\Temas 2\\Procesamiento de datos\\datosCompletosProcesados4.csv"

    # Ejecutar pipeline
    df_raw = load_data(raw_path)
    df_transformed = transform_data(df_raw)
    dq_nulos, dq_duplicados, dq_stats = data_quality_report(df_transformed)
    save_processed_data(df_transformed, output_path)

    print("\n>> ETL finalizado correctamente")
    print(">> Listo para analisis en notebook")
