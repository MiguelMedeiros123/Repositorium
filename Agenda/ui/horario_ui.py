import streamlit as st
import pandas as pd
import view
import datetime as dt
import time

class ManterHorarioUI:
    def main():
        st.header("Cadastro de horários")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with listar: ManterHorarioUI.Listar()
        with inserir: ManterHorarioUI.Inserir()
        with atualizar: ManterHorarioUI.Atualizar()
        with excluir: ManterHorarioUI.Excluir()
    
    @staticmethod
    def Listar():
        horarios = view.horario_listar()
        if horarios == []:
            st.write("Não há horário cadastrado.")
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

                bc = False
                for c in view.cliente_listar():
                    if c.id == h.idCliente:
                        lCliente.append(c.nome)
                        bc = True
                        break
                if bc == False: lCliente.append("Nenhum")

                bs = False
                for s in view.servico_listar():
                    if s.id == h.idServico:
                        lServico.append(s.descricao)
                        bs = True
                        break
                if bs == False: lServico.append("Nenhum")
                
            dic = {"id": lid, "data" : ldata, "confirmado": lconfirmado, "cliente": lCliente, "servico": lServico}
            graph = pd.DataFrame(dic)
            st.data_editor(graph, column_config = {"id": "ID", "data": "Data", "confirmado": "Confirmado", "cliente": "Cliente", "servico": "Serviço"}, hide_index=True, disabled=("id", "data", "cliente", "servico"))

    @staticmethod
    def Inserir():
        dia = st.text_input("Informa o dia no formato _dd/mm/aaaa_")
        hora = st.text_input("Informa a hora no formato _HH:MM_")

        op = st.selectbox("Confirmar horário?", ["Não confirmar", "Sim, confirmar"])
        if op == "Não confirmar": confirmado = False
        else: confirmado = True

        lc = view.cliente_listar()
        lc.insert(0, "Nenhum")
        c = st.selectbox("Cliente do horário", lc)
        if c == "Nenhum": idCliente = 0
        else: idCliente = c.id

        ls = view.servico_listar()
        ls.insert(0, "Nenhum")
        s = st.selectbox("Servico do horário", ls)
        if s == "Nenhum": idServico = 0
        else: idServico = s.id

        if st.button("Inserir"):
            data = dt.datetime.strptime(f"{dia} {hora}", "%d/%m/%Y %H:%M")
            view.horario_inserir(data, confirmado, idCliente, idServico)
            st.success("Horário inserido.")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def Atualizar():
        horarios = view.horario_listar()
        if horarios == []:
            st.write("Não há horário cadastrado.")
        else:
            h = st.selectbox("Horário a atualizar", horarios)

            dia = st.text_input("Informa o novo dia no formato _dd/mm/aaaa_", dt.datetime.strftime(h.data, "%d/%m/%Y"))
            hora = st.text_input("Informa a nova hora no formato _HH:MM_", dt.datetime.strftime(h.data, "%H:%M"))

            if h.confirmado == True: t = 1
            else: t = 0
            op = st.selectbox("Atualizar confirmação de horário?", ["Não confirmar", "Sim, confirmar"], t)
            if op == "Não confirmar": confirmado = False
            else: confirmado = True

            lc = view.cliente_listar()
            inc = 0
            for c in lc:
                if c.id == h.idCliente: inc = lc.index(c) + 1
            lc.insert(0, "Nenhum")
            c = st.selectbox("Novo cliente do horário", lc, inc)
            if c == "Nenhum": idCliente = 0
            else: idCliente = c.id

            ls = view.servico_listar()
            ins = 0
            for s in ls:
                if s.id == h.idServico: ins = ls.index(s) + 1
            ls.insert(0, "Nenhum")
            s = st.selectbox("Novo serviço do horário", ls, ins)
            if s == "Nenhum": idServico = 0
            else: idServico = s.id

            if st.button("Atualizar"):
                data = dt.datetime.strptime(f"{dia} {hora}", "%d/%m/%Y %H:%M")
                view.horario_atualizar(h.id, data, confirmado, idCliente, idServico)
                st.success("Horário atualizado.")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def Excluir():
        horarios = view.horario_listar()
        if horarios == []:
            st.write("Não há horário cadastrado.")
        else:
            h = st.selectbox("Horário a excluir", horarios)
            if st.button("Excluir"):
                view.horario_excluir(h.id)
                st.success("Horário excluído.")
                time.sleep
                st.rerun()
