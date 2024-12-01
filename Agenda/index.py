from ui.cliente_ui import ManterClienteUI
from ui.horario_ui import ManterHorarioUI
from ui.servico_ui import ManterServicoUI
from ui.agenda_ui import AbrirAgendaUI
from ui.conta_ui import AbrirContaUI

import view

import streamlit as st

class IndexUI:
    @staticmethod
    def main():
        view.cliente_admin()

        menu = st.sidebar.selectbox("Menu", ("Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Abrir Agenda do Dia", "Abrir Conta"))

        if menu == "Cadastro de Clientes":
            ManterClienteUI.main()

        if menu == "Cadastro de Horários":
            ManterHorarioUI.main()

        if menu == "Cadastro de Serviços":
            ManterServicoUI.main()
        
        if menu == "Abrir Agenda do Dia":
            AbrirAgendaUI.main()
        
        if menu == "Abrir Conta":
            AbrirContaUI.main()



IndexUI.main()