import streamlit as st
import pandas as pd
import view
import time

class VisualizarAgendaUI:
    def main():
        st.header("Agenda pessoal")
        

        st.subheader("Horários marcados")
        horarios = view.horario_profissional_listar(st.session_state["conta_id"])
        if len(horarios) == 0:
            st.write("Nenhum horário marcado.")
        else:
            lid = []
            ldata = []
            lconfirmado = []
            lcliente = []
            lservico = []
            for h in horarios:
                lid.append(h.get_id())
                ldata.append(h.get_data())
                lconfirmado.append(h.get_confirmado()) 
                
                bc = False
                for c in view.cliente_listar():
                    if c.get_id() == h.get_idCliente():
                        lcliente.append(c.get_nome())
                        bc = True
                        break
                if bc == False: lcliente.append("Nenhum")

                bs = False
                for s in view.servico_listar():
                    if s.get_id() == h.get_idServico():
                        lservico.append(s.get_descricao())
                        bs = True
                        break
                if bs == False: lservico.append("Nenhum")

            dic = {"id": lid, "data" : ldata, "confirmado": lconfirmado, "cliente": lcliente, "servico": lservico}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "data": "data", "confirmado": "Confirmado", "cliente": "Cliente", "servico": "Serviço"}, hide_index=True)


        st.subheader("Horários disponíveis")
        horarios = view.horario_profissional_listar(0)
        if len(horarios) == 0:
            st.write("Nenhum horário dispoível.")
        else:
            lid = []
            ldata = []
            lconfirmado = []
            for h in horarios:
                lid.append(h.get_id())
                ldata.append(h.get_data())
                lconfirmado.append(h.get_confirmado())     
            dic = {"id": lid, "data" : ldata, "confirmado": lconfirmado}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "data": "Data", "confirmado": "Confirmado"}, hide_index=True)

            hor = st.selectbox("Escolhe um horário para agendar", horarios)
            ser = st.selectbox("Escolhe o serviço desejado", view.servico_listar())
            if st.button("Agendar"):
                try:
                    view.horario_atualizar(hor.get_id(), hor.get_data(), hor.get_confirmado(), 0, ser.get_id(), st.session_state["conta_id"])
                    st.success("Horário agendado.")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)