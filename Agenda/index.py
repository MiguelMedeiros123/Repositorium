from ui.cliente_ui import ManterClienteUI
from ui.horario_ui import ManterHorarioUI
from ui.servico_ui import ManterServicoUI
from ui.agenda_ui import AbrirAgendaUI
from ui.conta_ui import AbrirContaUI
from ui.login_ui import LoginUI
from ui.listar_horario_ui import ListarHorarioUI
from ui.atualizar_conta import AtualizarContaUI

import view

import streamlit as st

class IndexUI:
    @staticmethod
    def main():
        view.cliente_admin()
        IndexUI.sidebar()

    def sidebar():
        if "conta_id" not in st.session_state:
            IndexUI.menu_visitantes()
        else:
            nome = st.session_state["conta_nome"]
            st.sidebar.write(f"Bem vindo(a), {nome}.")
            if nome == "admin": IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            IndexUI.sair()

    def menu_visitantes():
        op = st.sidebar.selectbox("Menu", ("Entrar no sistema", "Abrir conta"))
        if op == "Entrar no sistema": LoginUI.main()
        if op == "Abrir conta": AbrirContaUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ("Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Abrir Agenda do Dia"))
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()      
        if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ("Horários Disponíveis", "Atualizar conta"))
        if op == "Horários Disponíveis": ListarHorarioUI.main()
        if op == "Atualizar conta": AtualizarContaUI.main()

    def sair():
        if st.sidebar.button("Sair do sistema"):
            del st.session_state["conta_id"]
            del st.session_state["conta_nome"]
            st.rerun()



IndexUI.main()