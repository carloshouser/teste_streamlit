# python.exe -m pip install --upgrade pip
# pip install streamlit-cookies-manager
# Caso o .gitignore não esteja sendo respeitado,
# significa que o arquivo já foi rastreado pelo git
# Para remover o arquivo do rastreamento, use:
# git rm --cached -r vm bkp
# git commit -m "Removendo arquivos rastreados para respeitar o .gitignore"


# Importações
import streamlit as st
import json
import base64
from constantes import usuarios, estilo, quadros
from streamlit_cookies_manager import EncryptedCookieManager

# Configuração dos Cookies
cookies = EncryptedCookieManager(
    prefix="flamboyant_",
    password="segredo_super_secreto"  # Coloque uma senha forte aqui
)

if not cookies.ready():
    st.stop()

# Funções Auxiliares


def add_css():
    """
    Adiciona o CSS para personalizar o layout do aplicativo.
    """
    st.markdown(estilo, unsafe_allow_html=True)


def load_json(file_path):
    """
    Carrega dados de um arquivo JSON.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def render_header():
    """
    Renderiza o cabeçalho do aplicativo com uma imagem.
    """
    st.image("Salao.png", use_container_width=True)


def autenticar_usuario(usuario, senha):
    """
    Verifica se o usuário e a senha são válidos.
    """
    return usuario in usuarios and usuarios[usuario]["senha"] == senha


def reset_sessao():
    """
    Reseta a sessão do Streamlit e remove cookies.
    Faz logout: limpa cookies e volta para tela de login.
    """
    cookies['usuario'] = ''
    cookies['senha'] = ''
    st.session_state["logado"] = False
    st.session_state["pagina"] = "login"
    st.rerun()

# Renderizações


def render_login():
    """
    Renderiza a tela de login.
    """
    st.title("Flamboyant - Quadro de Anúncios")
    usuario = st.text_input("Usuário").strip()
    senha = st.text_input("Senha", type="password").strip()

    if st.button("Entrar"):
        if autenticar_usuario(usuario, senha):
            # Atualiza sessão
            st.session_state.update({
                "logado": True,
                "usuario": usuario,
                "pagina": "home"
            })
            # Salva login nos cookies
            cookies['usuario'] = usuario
            cookies['senha'] = senha
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")


def nome_fantasia(dic_usuario, nome):
    if dic_usuario['sexo'] == 'M':
        return f"irmão {nome}"
    else:
        return f"irmã {nome}"


def render_home():
    """
    Renderiza a página principal com os quadros de anúncios.
    """
    st.title("Flamboyant - Quadro de Anúncios")
    usuario = st.session_state["usuario"]
    permissoes = usuarios[usuario]["permissoes"]
    if usuarios[usuario]["sexo"] == "M":
        st.write(
            f"### Saudações {nome_fantasia(usuarios[usuario], usuario)}, seja bem-vindo!!")
    else:
        st.write(
            f"### Saudações {nome_fantasia(usuarios[usuario], usuario)}, seja bem-vinda!!")

    st.divider()
    col1, col2 = st.columns(2)

    def render_quadros(chaves, coluna):
        for chave in chaves:
            if chave in permissoes:
                quadro = quadros[chave]
                if coluna.button(quadro["titulo"], key=f"abrir_{chave}"):
                    st.session_state.update({
                        "pagina": "visualizar",
                        "quadro_atual": chave
                    })
                    st.rerun()

    render_quadros(["a", "b", "c"], col1)
    render_quadros(["d", "e", "f", "g"], col2)

    st.divider()
    st.write('### Designações')
    st.markdown(
        '### <a href="https://www.dropbox.com/scl/fo/6qexumfrgxtbvq9ykp2fp/AH49M3K9i0wGlCu-tRRCBrc?rlkey=40k34tbbkly0qq3x7v7z5nkbx&st=dgibbww7&dl=0" target="_blank" style="margin-top: 20px;">📂 Acessar Designações</a>',
        unsafe_allow_html=True
    )
    st.write(
        f'##### {nome_fantasia(usuarios[usuario], usuario).title()}, consulte as designações de sua congregação de forma rápida e simples.')

    st.divider()
    st.write('### Territórios')
    st.markdown(
        '### <a href="https://www.dropbox.com/scl/fo/cvzev6g0ktlwqqd9sbkcz/AKxNxYXYDq2OgFYSj8szZdw?rlkey=oy5r89ijmjrzrlguf5l0fy8qx&dl=0" target="_blank" style="margin-top: 20px;">📂 Territórios</a>',
        unsafe_allow_html=True
    )
    st.write(
        f'##### {nome_fantasia(usuarios[usuario], usuario).title()}, acesse os territórios de sua congregação de forma bem objetiva.')

    st.divider()

    if st.button("Sair"):
        reset_sessao()


def render_visualizar():
    """
    Renderiza a página de visualização de um quadro.
    """
    chave = st.session_state["quadro_atual"]
    quadro = quadros[chave]

    st.title(quadro["titulo"])

    with open(quadro["arquivo"], "rb") as file:
        if quadro["arquivo"].endswith(".png"):
            st.image(
                file.read(), caption=quadro["titulo"], use_container_width=True)
        elif quadro["arquivo"].endswith(".pdf"):
            pdf_base64 = base64.b64encode(file.read()).decode('utf-8')
            st.markdown(
                f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="100%" height="1000px"></iframe>',
                unsafe_allow_html=True
            )
        elif quadro["arquivo"].endswith(".html"):
            html_content = file.read().decode("utf-8")
            st.components.v1.html(html_content, height=1000)

    if st.button("Voltar"):
        st.session_state["pagina"] = "home"
        st.rerun()


def render_eventos(events):
    """
    Renderiza a aba de eventos.
    """
    st.subheader("Próximos Eventos")
    for event in events:
        if event['link']:
            st.markdown(f"""
            ### 📅 {event['date']}
            #### [**{event['event']}**]({event['link']})
            """)

        else:
            st.markdown(f"""
            ### 📅 {event['date']}
            #### **{event['event']}**
            """)
        st.divider()

    if st.button("Fechar"):
        reset_sessao()

# Configuração Principal


add_css()
render_header()
events = load_json('events.json')

# Inicializar a sessão
if "logado" not in st.session_state:
    st.session_state["logado"] = False
    st.session_state["pagina"] = "login"

# Verificar se já tem login salvo nos cookies
if not st.session_state["logado"]:
    usuario_cookie = cookies.get("usuario")
    senha_cookie = cookies.get("senha")
    if usuario_cookie and senha_cookie:
        if autenticar_usuario(usuario_cookie, senha_cookie):
            st.session_state.update({
                "logado": True,
                "usuario": usuario_cookie,
                "pagina": "home"
            })
            st.rerun()

# Decidir o que mostrar
if not st.session_state["logado"]:
    render_login()
else:
    tab1, tab2 = st.tabs(["Quadro", "Eventos"])

    with tab1:
        if st.session_state.get("pagina") == "home":
            render_home()
        elif st.session_state.get("pagina") == "visualizar":
            render_visualizar()

    with tab2:
        render_eventos(events)
