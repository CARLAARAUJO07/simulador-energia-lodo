import streamlit as st
import numpy as np

st.set_page_config(page_title="Simulador de Energia a partir do Lodo", layout="wide")

st.title("⚡ Simulador de Geração de Energia a partir do Lodo da Indústria de Celulose")

st.sidebar.header("🔧 Parâmetros de Entrada")

massa_lp = st.sidebar.number_input("Massa de Lodo Primário (kg/dia)", value=1000.0, step=100.0)
umidade_lp = st.sidebar.slider("Umidade do Lodo Primário (%)", min_value=0, max_value=100, value=70)
pci_lp = st.sidebar.number_input("PCI do Lodo Primário (MJ/kg)", value=12.0, step=0.5)

massa_ls = st.sidebar.number_input("Massa de Lodo Secundário (kg/dia)", value=1000.0, step=100.0)
umidade_ls = st.sidebar.slider("Umidade do Lodo Secundário (%)", min_value=0, max_value=100, value=80)
pci_ls = st.sidebar.number_input("PCI do Lodo Secundário (MJ/kg)", value=10.0, step=0.5)

eficiencia = st.sidebar.slider("Eficiência da Conversão (%)", min_value=0, max_value=100, value=25)

ms_lp = massa_lp * (1 - umidade_lp / 100)
ms_ls = massa_ls * (1 - umidade_ls / 100)

energia_mj = (ms_lp * pci_lp + ms_ls * pci_ls) * (eficiencia / 100)
energia_kwh = energia_mj / 3.6

consumo_residencial_dia = 16.37
residencias = energia_kwh / consumo_residencial_dia

st.subheader("🔋 Resultados da Simulação")
st.metric("Energia Gerada (kWh/dia)", f"{energia_kwh:.2f}")
st.metric("Residências Atendidas", f"{residencias:.0f}")

st.markdown("### Fórmula Utilizada")
st.latex(r"\text{Energia (kWh)} = \frac{(M_{\text{seca,LP}} \cdot PCI_{\text{LP}} + M_{\text{seca,LS}} \cdot PCI_{\text{LS}}) \cdot \text{Eficiência}}{3.6}")
