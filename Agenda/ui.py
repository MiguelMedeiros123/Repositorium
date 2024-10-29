import streamlit as st
import pandas as pd
import view
import datetime as dt

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



class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de clientes")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with listar: ManterClienteUI.Listar()
        with inserir: ManterClienteUI.Inserir()
        with atualizar: ManterClienteUI.Atualizar()
        with excluir: ManterClienteUI.Excluir()
    
    @staticmethod
    def Listar():
        clientes = view.cliente_listar()
        if clientes == []:
            st.write("Não há cliente cadastrado.")
        else:
            lid = []
            lnome = []
            lemail = []
            lfone = []
            for c in clientes:
                lid.append(c.id)
                lnome.append(c.nome)
                lemail.append(c.email)
                lfone.append(c.fone) 
            dic = {"id": lid, "nome" : lnome, "email": lemail, "fone": lfone}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "email": "E-Mail", "fone": "Telefone"}, hide_index=True)

    @staticmethod
    def Inserir():
        nome = st.text_input("Informa o nome")
        email = st.text_input("Informa o e-mail")
        fone = st.text_input("Informa o fone")
        if st.button("Inserir"):
            view.cliente_inserir(nome, email, fone)
            st.success("Cliente inserido.")
            st.rerun()

    @staticmethod
    def Atualizar():
        clientes = view.cliente_listar()
        if clientes == []:
            st.write("Não há cliente cadastrado.")
        else:
            c = st.selectbox("Cliente a atualizar", clientes)
            nome = st.text_input("Informa o novo nome", c.nome)
            email = st.text_input("Informa o novo e-mail", c.email)
            fone = st.text_input("Informa o novo fone", c.fone)
            if st.button("Atualizar"):
                view.cliente_atualizar(c.id, nome, email, fone)
                st.success("Cliente atualizado.")
                st.rerun()

    @staticmethod
    def Excluir():
        clientes = view.cliente_listar()
        if clientes == []:
            st.write("Não há cliente cadastrado.")
        else:
            c = st.selectbox("Cliente a excluir", clientes)
            if st.button("Excluir"):
                view.cliente_excluir(c.id)
                st.success("Cliente excluído.")
                st.rerun()



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
            lidCliente = []
            lidServico = []
            for h in horarios:
                lid.append(h.id)
                ldata.append(h.data)
                lconfirmado.append(h.confirmado)
                lidCliente.append(h.idCliente)
                lidServico.append(h.idServico)
            dic = {"id": lid, "Data" : ldata, "confirmado": lconfirmado, "idCliente": lidCliente, "idServico": lidServico}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "data": "data", "confirmado": "Confirmado", "idCliente": "ID do Cliente", "idServico": "ID do Serviço"}, hide_index=True)

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
                st.rerun()




class ManterServicoUI:
    def main():
        st.header("Cadastro de serviços")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with listar: ManterServicoUI.Listar()
        with inserir: ManterServicoUI.Inserir()
        with atualizar: ManterServicoUI.Atualizar()
        with excluir: ManterServicoUI.Excluir()
    
    @staticmethod
    def Listar():
        servicos = view.servico_listar()
        if servicos == []:
            st.write("Não há serviço cadastrado.")
        else:
            lid = []
            ldescricao = []
            lvalor = []
            lduracao = []
            for s in servicos:
                lid.append(s.id)
                ldescricao.append(s.descricao)
                lvalor.append(s.valor)
                lduracao.append(s.duracao) 
            dic = {"id": lid, "descricao" : ldescricao, "valor": lvalor, "duracao": lduracao}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "descricao": "Descrição", "valor": "Valor", "duracao": "Duração"}, hide_index=True)

    @staticmethod
    def Inserir():
        descricao = st.text_input("Informa a descrição")
        valor = st.text_input("Informa o valor")
        duracao = st.text_input("Informa a duração, em _min_")
        if st.button("Inserir"):
            view.servico_inserir(descricao, float(valor), int(duracao))
            st.success("Serviço inserido.")
            st.rerun()

    @staticmethod
    def Atualizar():
        servicos = view.servico_listar()
        if servicos == []:
            st.write("Não há serviço cadastrado.")
        else:
            s = st.selectbox("Serviço a atualizar", servicos)
            descricao = st.text_input("Informa a nova descrição", s.descricao)
            valor = st.text_input("Informa o novo valor", s.valor)
            duracao = st.text_input("Informa a nova duração", s.duracao)
            if st.button("Atualizar"):
                view.servico_atualizar(s.id, descricao, float(valor), int(duracao))
                st.success("Serviço atualizado.")
                st.rerun()

    @staticmethod
    def Excluir():
        servicos = view.servico_listar()
        if servicos == []:
            st.write("Não há serviço cadastrado.")
        else:
            s = st.selectbox("Serviço a excluir", servicos)
            if st.button("Excluir"):
                view.servico_excluir(s.id)
                st.success("Serviço excluído.")
                st.rerun()




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