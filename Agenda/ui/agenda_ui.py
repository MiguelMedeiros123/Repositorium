import streamlit as st
import view
import datetime as dt

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
            hora = dt.datetime.strptime(f"{dia} {horain}", "%d/%m/%Y %H:%M")
            delta = dt.timedelta(minutes=int(intervalo))
            horamax = dt.datetime.strptime(f"{dia} {horafim}", "%d/%m/%Y %H:%M")
            while hora < horamax:
                view.horario_inserir(hora, False, 0, 0)
                hora += delta
            view.horario_inserir(horamax, False, 0, 0)
            st.success("Horários inseridos.")
            st.rerun()