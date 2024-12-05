import streamlit as st
import pandas as pd
import view
import time

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
                lid.append(s.get_id())
                ldescricao.append(s.get_descricao())
                lvalor.append(s.get_valor())
                lduracao.append(s.get_duracao()) 
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
            time.sleep(2)
            st.rerun()

    @staticmethod
    def Atualizar():
        servicos = view.servico_listar()
        if servicos == []:
            st.write("Não há serviço cadastrado.")
        else:
            s = st.selectbox("Serviço a atualizar", servicos)
            descricao = st.text_input("Informa a nova descrição", s.get_descricao())
            valor = st.text_input("Informa o novo valor", s.get_valor())
            duracao = st.text_input("Informa a nova duração", s.get_duracao())
            if st.button("Atualizar"):
                view.servico_atualizar(s.get_id(), descricao, float(valor), int(duracao))
                st.success("Serviço atualizado.")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def Excluir():
        servicos = view.servico_listar()
        if servicos == []:
            st.write("Não há serviço cadastrado.")
        else:
            s = st.selectbox("Serviço a excluir", servicos)
            if st.button("Excluir"):
                view.servico_excluir(s.get_id())
                st.success("Serviço excluído.")
                time.sleep(2)
                st.rerun()
