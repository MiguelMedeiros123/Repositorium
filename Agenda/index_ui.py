from ui.cliente_ui import *
from ui.horario_ui import *
from ui.servico_ui import *
from ui.agenda_ui import *

class IndexUI:
    @staticmethod
    def main():
        menu = st.sidebar.selectbox("Menu", ("Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Abrir Agenda do Dia"))

        if menu == "Cadastro de Clientes":
            ManterClienteUI.main()

        if menu == "Cadastro de Horários":
            ManterHorarioUI.main()

        if menu == "Cadastro de Serviços":
            ManterServicoUI.main()
        
        if menu == "Abrir Agenda do Dia":
            AbrirAgendaUI.main()