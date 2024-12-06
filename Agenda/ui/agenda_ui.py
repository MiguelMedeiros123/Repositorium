import streamlit as st
import view
import time

class AbrirAgendaUI:
    def main():
        st.header("Abrir Agenda do Dia")
        AbrirAgendaUI.AbrirAgenda()
    
    def AbrirAgenda():
        dia = st.text_input("Informa o dia no formato _dd/mm/aaaa_")
        horain = st.text_input("Informa a hora de início no formato _HH:MM_")
        horafim = st.text_input("Informa o início do último horário no formato _HH:MM_")
        intervalo = st.text_input("Informa o intervalo entre os horários em _min_")
        if st.button("Inserir horários"):
            try:
                view.horario_abrir_agenda(dia, horain, horafim, int(intervalo))
                st.success("Horário(s) inseridos.")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)