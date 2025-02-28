import streamlit as st
import pandas as pd
import view
import datetime as dt
import time

class VerEmpresaUI:
    def main():
        st.header("Empresa")
        empresa, listar_setor, listar_func, custos, reajustes, realocamentos = st.tabs(["Empresa", "Setores", "Funcionários", "Custos", "Reajustes", "Realocamentos"])\

        with empresa: VerEmpresaUI.empresa()
        with listar_setor: VerEmpresaUI.listar_setor()
        with listar_func: VerEmpresaUI.listar_func()
        with custos: VerEmpresaUI.custos()
        with reajustes: VerEmpresaUI.reajustes()
        with realocamentos: VerEmpresaUI.realocamentos()

    def empresa():
        if st.session_state["conta_nome"] == "admin":
            em = st.selectbox("Escolhe a empresa", view.empresa_listar())
            if st.button("Escolher"):
                st.session_state["empresa_id"] = em.get_id()
                st.rerun()

        if "empresa_id" not in st.session_state: pass
        else:
            e = view.empresa_listar_id(st.session_state["empresa_id"])
            if e == None:
                st.subheader("Indisponível")
                st.write("O administrador deve inserir-te no sistema da empresa.")
            else:
                st.subheader(e.get_nome())
                st.write(f"Dono: {e.get_dono()}")

    def listar_setor():
        pass

    def listar_func():
        pass

    def custos():
        pass
    
    def reajustes():
        pass

    def realocamentos():
        pass