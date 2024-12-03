import streamlit as st
import pandas as pd
import view
import time

class ListarHorarioUI:
    def main():
        st.header("Horários disponíveis")
        ListarHorarioUI.listar()
    
    def listar():
        horarios = view.horario_disponivel_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário dispoível.")
        else:
            lid = []
            ldata = []
            lconfirmado = []
            for h in horarios:
                lid.append(h.id)
                ldata.append(h.data)
                lconfirmado.append(h.confirmado)     
            dic = {"id": lid, "Data" : ldata, "confirmado": lconfirmado}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "data": "data", "confirmado": "Confirmado", "cliente": "Cliente", "servico": "Serviço"}, hide_index=True)

            if st.session_state["conta_nome"] != "admin":
                hor = st.selectbox("Escolhe um horário para agendar", horarios)
                ser = st.selectbox("Escolhe o serviço desejado", view.servico_listar())
                if st.button("Agendar"):
                    view.horario_atualizar(hor.id, hor.data, hor.confirmado, st.session_state["conta_id"], ser.id)
                    st.success("Horário agendado.")
                    time.sleep(2)
                    st.rerun()