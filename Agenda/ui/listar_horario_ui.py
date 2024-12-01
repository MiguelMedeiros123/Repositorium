import streamlit as st
import pandas as pd
import view

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
            lCliente = []
            lServico = []
            for h in horarios:
                lid.append(h.id)
                ldata.append(h.data)
                lconfirmado.append(h.confirmado)
                lCliente.append("Nenhum")
                lServico.append("Nenhum")      
            dic = {"id": lid, "Data" : ldata, "confirmado": lconfirmado, "cliente": lCliente, "servico": lServico}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "data": "data", "confirmado": "Confirmado", "cliente": "Cliente", "servico": "Serviço"}, hide_index=True)