from ui.cliente_ui import ManterClienteUI
from ui.horario_ui import ManterHorarioUI
from ui.servico_ui import ManterServicoUI
from ui.profissional_ui import ManterProfissionalUI
from ui.perfil_ui import ManterPerfilUI
from ui.agenda_ui import AbrirAgendaUI
from ui.conta_ui import AbrirContaUI
from ui.login_ui import LoginUI
from ui.listar_horario_ui import ListarHorarioUI
from ui.atualizar_conta import AtualizarContaUI
from ui.pro_agenda import VisualizarAgendaUI

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
            if st.session_state["conta_tipo"] == "cliente":
                if nome == "admin": IndexUI.menu_admin()
                else: IndexUI.menu_cliente()
            elif st.session_state["conta_tipo"] == "profissional":
                IndexUI.menu_profissional()
            IndexUI.sair()

    def menu_visitantes():
        op = st.sidebar.selectbox("Menu", ("Entrar no sistema", "Abrir conta"))
        if op == "Entrar no sistema": LoginUI.main()
        if op == "Abrir conta": AbrirContaUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ("Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Cadastro de Profissionais", "Cadastro de Perfis", "Abrir Agenda do Dia", "Atualizar conta"))
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Cadastro de Perfis": ManterPerfilUI.main()
        if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
        if op == "Atualizar conta": AtualizarContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ("Horários Disponíveis", "Atualizar conta"))
        if op == "Horários Disponíveis": ListarHorarioUI.main()
        if op == "Atualizar conta": AtualizarContaUI.main()
    
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ("Visualizar agenda", "Atualizar conta"))
        if op == "Visualizar agenda": VisualizarAgendaUI.main()
        if op == "Atualizar conta": AtualizarContaUI.main()

    def sair():
        if st.sidebar.button("Sair do sistema"):
            del st.session_state["conta_id"]
            del st.session_state["conta_nome"]
            del st.session_state["conta_tipo"]
            st.rerun()



IndexUI.main()