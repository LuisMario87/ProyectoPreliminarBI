# ETL farma 
import pandas as pd

def load_data(path="C:\\Users\\luism\\OneDrive\\Documentos\\A. 9no Semestre\\Temas 2\\Procesamiento de datos\\datosFarmaceuticos30k.xlsx"):
    df = pd.read_excel(path)
    df.columns = df.columns.str.strip()
    df["FechaCompra"] = pd.to_datetime(df.get("FechaCompra"), errors="coerce")
    df["Cantidad"] = pd.to_numeric(df.get("Cantidad"), errors="coerce")
    df["PrecioUnitario"] = pd.to_numeric(df.get("PrecioUnitario"), errors="coerce")
    df["TotalVenta"] = df["Cantidad"] * df["PrecioUnitario"]
    return df

if __name__ == "__main__":
    df = load_data("C:\\Users\\luism\\OneDrive\\Documentos\\A. 9no Semestre\\Temas 2\\Reprocesamiento de datos por acentos\\demoDatosRaw.xlsx")
    print("Filas cargadas:", len(df))
     # Guardar
    output_path = "C:\\Users\\luism\\OneDrive\\Documentos\\A. 9no Semestre\\Temas 2\\Procesamiento de datos\\datosFarmaceuticos30k.csv"
    df.to_csv(output_path, index=False, encoding="utf-8")
    print("Archivo procesado guardado en:", output_path)