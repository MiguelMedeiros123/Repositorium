import streamlit as st
import pandas as pd
from funcao import Funcao

class UI:
    @staticmethod
    def main():
        st.header("Função quadrática")
        st.write("Função do tipo f(x) = ax^2 + bx + c")
        
        a = st.text_input("Valor do coeficiente a")
        b = st.text_input("Valor do coeficiente b")
        c = st.text_input("Valor do coeficiente c")
        if st.button("Calcular"):
            y = Funcao(float(a), float(b), float(c))
            st.write(y)
            st.write(f"Vértice = ({y.xv()}, {y.yv()})")
            st.write(f"Raízes: x1 = {y.x1()}  ;  x2 = {y.x2()}")

            px = []
            py = []
            min = y.xv() - 5
            max = y.xv() + 5
            n = 200
            dx = (max - min)/n
            x = min
            while x < max:
                dy = y.f(x)
                py.append(dy)
                px.append(x)
                x += dx
            
            dic = {"x": px, "y": py}
            chart_data = pd.DataFrame(dic)
            st.line_chart(chart_data, x = "x", y = "y")