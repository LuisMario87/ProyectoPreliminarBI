#Dashboard en Streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# config del dashboard
st.set_page_config(
    page_title="Dashboard Farmacia BI",
    page_icon="",
    layout="wide"
)

st.title("Dashboard Interactivo - Farmacia")
st.markdown("---")


# carga de los datos

@st.cache_data
def load_data():
    df = pd.read_csv("C:\\Users\\luism\\OneDrive\\Documentos\\A. 9no Semestre\\Temas 2\\Procesamiento de datos\\datosCompletosProcesados.csv")
    df["FechaCompra"] = pd.to_datetime(df["FechaCompra"])
    df["Dia"] = df["FechaCompra"].dt.day
    df["Mes"] = df["FechaCompra"].dt.month
    return df

df = load_data()

# Filtros interactivos
st.sidebar.header(" Filtros del Dashboard")

# Filtro 1: Rango de fechas
min_date = df["FechaCompra"].min()
max_date = df["FechaCompra"].max()

fecha_seleccion = st.sidebar.date_input(
    "Rango de Fechas",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

df = df[(df["FechaCompra"] >= pd.to_datetime(fecha_seleccion[0])) &
        (df["FechaCompra"] <= pd.to_datetime(fecha_seleccion[1]))]

# Filtro 2: Categoría
categorias = df["CategoríaProducto"].unique()
categoria_sel = st.sidebar.multiselect(
    "Categoría de Producto",
    categorias,
    default=categorias
)

df = df[df["CategoríaProducto"].isin(categoria_sel)]

# Filtro 3: Selección para Top N productos
top_n = st.sidebar.slider("Top N Productos Más Vendidos", 5, 20, 5)

st.sidebar.markdown("---")

# KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(" Ventas Totales", f"${df['TotalVenta'].sum():,.2f}")

with col2:
    st.metric(" Transacciones", f"{len(df):,}")

with col3:
    st.metric(" Clientes Únicos", df["ClienteID"].nunique())

with col4:
    ticket = df["TotalVenta"].mean()
    st.metric(" Ticket Promedio", f"${ticket:,.2f}")

st.markdown("---")

# graficas

#1. Ventas por categoría
st.subheader(" Ventas por Categoría")

ventas_categoria = df.groupby("CategoríaProducto")["TotalVenta"].sum().sort_values()

fig1, ax1 = plt.subplots(figsize=(8,4))
ventas_categoria.plot(kind="barh", ax=ax1, color="royalblue")
ax1.set_xlabel("Ventas Totales")
ax1.set_ylabel("Categoría")
st.pyplot(fig1)

#2. Ventas en el tiempo (selector de periodicidad)
st.subheader("Ventas en el Tiempo")

periodo = st.selectbox("Selecciona periodicidad:", ["Semanal", "Mensual", "Diaria"])

if periodo == "Semanal":
    df_periodo = df.set_index("FechaCompra").resample("W")["TotalVenta"].sum()
elif periodo == "Mensual":
    df_periodo = df.set_index("FechaCompra").resample("M")["TotalVenta"].sum()
else:
    df_periodo = df.set_index("FechaCompra")["TotalVenta"]

fig2, ax2 = plt.subplots(figsize=(10,4))
df_periodo.plot(ax=ax2, color="darkgreen")
ax2.set_ylabel(f"Ventas ({periodo})")
ax2.set_xlabel("Fecha")
st.pyplot(fig2)

#3. Top N productos interactivo
st.subheader(f" op {top_n} Productos Más Vendidos")

top_products = df.groupby("NombreProducto")["TotalVenta"].sum().nlargest(top_n)

fig3, ax3 = plt.subplots(figsize=(8,4))
top_products.plot(kind="bar", ax=ax3, color="darkred")
ax3.set_ylabel("Ventas Totales")
ax3.set_xlabel("Producto")
plt.xticks(rotation=45)
st.pyplot(fig3)

#4. Heatmap
st.subheader("Heatmap de Ventas por Dia y Mes")

pivot = df.pivot_table(values="TotalVenta", index="Mes", columns="Dia", aggfunc="sum")

fig4, ax4 = plt.subplots(figsize=(12,4))
sns.heatmap(pivot, cmap="inferno", ax=ax4)
st.pyplot(fig4)

st.markdown("---")
st.success("Dashboard Interactivo generado correctamente ")

#Correr en terminal con -> [streamlit run dashboard.py]
