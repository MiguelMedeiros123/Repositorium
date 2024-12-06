import streamlit as st
import pandas as pd
import view
import time

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
            lperfil = []
            for c in clientes:
                lid.append(c.get_id())
                lnome.append(c.get_nome())
                lemail.append(c.get_email())
                lfone.append(c.get_fone())

                bp = False
                for p in view.perfil_listar():
                    if p.get_id() == c.get_idPerfil():
                        lperfil.append(p.get_nome())
                        bp = True
                        break
                if bp == False: lperfil.append("Nenhum")

            dic = {"id": lid, "nome" : lnome, "email": lemail, "fone": lfone, "perfil": lperfil}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "email": "E-Mail", "fone": "Telefone", "perfil": "Perfil"}, hide_index=True)

    @staticmethod
    def Inserir():
        nome = st.text_input("Informa o nome")
        email = st.text_input("Informa o e-mail")
        fone = st.text_input("Informa o fone")
        
        lp = view.perfil_listar()
        lp.insert(0, "Nenhum")
        p = st.selectbox("Informa o perfil", lp)
        if p == "Nenhum": idPerfil = 0
        else: idPerfil = p.get_id()

        senha = st.text_input("Informa a senha", type="password")
        confirm = st.text_input("Confirmação da senha", type="password")
        if st.button("Inserir"):
            try:
                if len(senha) >= 3:
                    if senha == confirm:
                        view.cliente_inserir(nome, email, fone, senha, idPerfil)
                        st.success("Cliente inserido com sucesso.")
                        time.sleep(2)
                        st.rerun()
                    else: st.error("A senha e sua confirmação devem ser iguais.")
                else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
            except Exception as erro:
                st.error(erro)

    @staticmethod
    def Atualizar():
        clientes = view.cliente_listar()
        if clientes == []:
            st.write("Não há cliente cadastrado.")
        else:
            c = st.selectbox("Cliente a atualizar", clientes)
            nome = st.text_input("Informa o novo nome", c.get_nome())
            email = st.text_input("Informa o novo e-mail", c.get_email())
            fone = st.text_input("Informa o novo fone", c.get_fone())

            lp = view.perfil_listar()
            inp = 0
            for p in lp:
                if p.get_id() == c.get_idPerfil(): inp = lp.index(p) + 1
            lp.insert(0, "Nenhum")
            p = st.selectbox("Informa o novo perfil", lp, inp)
            if p == "Nenhum": idPerfil = 0
            else: idPerfil = p.get_id()
            
            senha = st.text_input("Informa a nova senha", c.get_senha(), type="password")
            confirm = st.text_input("Confirmação da nova senha", type="password")
            if st.button("Atualizar"):
                try:
                    if len(senha) >= 3:
                        if senha == confirm:
                            view.cliente_atualizar(c.get_id(), nome, email, fone, senha, idPerfil)
                            st.success("Cliente atualizado com sucesso.")
                            time.sleep(2)
                            st.rerun()
                        else: st.error("A senha e sua confirmação devem ser iguais.")
                    else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
                except Exception as erro:
                    st.error(erro)

    @staticmethod
    def Excluir():
        clientes = view.cliente_listar()
        if clientes == []:
            st.write("Não há cliente cadastrado.")
        else:
            c = st.selectbox("Cliente a excluir", clientes)
            if st.button("Excluir"):
                try:
                    view.cliente_excluir(c.get_id())
                    st.success("Cliente excluído.")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)