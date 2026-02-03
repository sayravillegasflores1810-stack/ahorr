import streamlit as st
import pandas as pd

st.title("🔋 Calculadora de Eficiencia Energética (VFD)")
st.write("### Ingeniería Industrial - UPN")

# Entradas
potencia = st.number_input("Potencia Motor (kW)", value=10.0)
horas = st.number_input("Horas/Año", value=4000)
costo = st.number_input("Costo $/kWh", value=0.15)
velocidad = st.slider("Velocidad con VFD (%)", 10, 100, 80) / 100

# Cálculos (Leyes de Afinidad)
base = potencia * horas
con_vfd = potencia * (velocidad**3) * horas
ahorro_kwh = base - con_vfd
ahorro_dinero = ahorro_kwh * costo

# Mostrar resultados
st.success(f"Ahorro Anual: {ahorro_kwh:,.2f} kWh")
st.success(f"Ahorro Económico: ${ahorro_dinero:,.2f}")

# Tabla para el informe
df = pd.DataFrame({
    "Escenario": ["Sin VFD", "Con VFD", "Total Ahorro"],
    "Consumo (kWh)": [base, con_vfd, ahorro_kwh],
    "Gasto ($)": [base*costo, con_vfd*costo, ahorro_dinero]
})
st.table(df)
