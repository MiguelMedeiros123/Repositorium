from ui.conta_ui import AbrirContaUI
from ui.login_ui import LoginUI
from ui.funcionario_ui import ManterFuncionarioUI
from ui.setor_ui import ManterSetorUI
from ui.empresa_ui import ManterEmpresaUI
from ui.ver_empresa_ui import VerEmpresaUI

import view

import streamlit as st

class IndexUI:
    @staticmethod
    def main():
        view.in_admin()
        IndexUI.sidebar()

    def sidebar():
        if "conta_id" not in st.session_state:
            IndexUI.menu_visitantes()
        else:
            nome = st.session_state["conta_nome"]
            st.sidebar.write(f"Bem vindo(a), {nome}.")
            if nome == "admin": IndexUI.menu_admin()
            else: IndexUI.menu_funcionario()
            IndexUI.logout()
    
    def menu_visitantes():
        op = st.sidebar.selectbox("Menu", ("Entrar no sistema", "Abrir conta"))
        if op == "Entrar no sistema": LoginUI.main()
        if op == "Abrir conta": AbrirContaUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ("Gerir empresa", "Cadastro de funcionários", "Cadastro de setores", "Cadastro de empresas"))
        if op == "Gerir empresa": VerEmpresaUI.main()
        if op == "Cadastro de funcionários": ManterFuncionarioUI.main()
        if op == "Cadastro de setores": ManterSetorUI.main()
        if op == "Cadastro de empresas": ManterEmpresaUI.main()

    def menu_funcionario():
        op = st.sidebar.selectbox("Menu", ("Ver empresa"))
        if op == "Ver empresa": VerEmpresaUI.main()
    
    def logout():
        if st.sidebar.button("Sair do sistema"):
            del st.session_state["conta_id"]
            del st.session_state["conta_nome"]
            if "empresa_id" in st.session_state: del st.session_state["empresa_id"]
            st.rerun()



IndexUI.main()