import streamlit as st
import view
import time

class AtualizarContaUI:
    @staticmethod
    def main():
        st.header("Atualizar dados da conta")

        senha = st.text_input("Insere tua senha", type="password")

        if st.button("Confirmar senha"):
            cli = view.cliente_listar_id(st.session_state["conta_id"])
            a = view.cliente_autenticar(cli.get_email(), senha)
            if a == None: st.error("Senha incorreta")
            else:
                nome = st.text_input("Informa o novo nome", cli.get_nome())
                email = st.text_input("Informa o novo e-mail", cli.get_email())
                fone = st.text_input("Informa o novo fone", cli.get_fone())
                senhanova = st.text_input("Informa a nova senha", cli.get_senha(), type="password")
                confirmacao = st.text_input("confirmação da nova senha", type="password")
                
                if st.button("Atualizar conta"):
                    if email != "": e = True
                    else: e = False
                    for c in view.cliente_listar():
                        if c.email == email: 
                            if c.id != cli.get_id(): e = False
                    if e:
                        if len(senhanova) >= 3:
                            if senhanova == confirmacao:
                                view.cliente_atualizar(cli.get_id(), nome, email, fone, senhanova)
                                st.success("Conta atualizada com sucesso.")
                                time.sleep(2)

                            else: st.error("A senha e sua confirmação devem ser iguais.")
                        else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
                    else: st.error("Insere um email válido que não esteja em uso.")