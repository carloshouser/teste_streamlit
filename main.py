# python.exe -m pip install --upgrade pip
# pip install streamlit-cookies-manager
# Caso o .gitignore não esteja sendo respeitado,
# significa que o arquivo já foi rastreado pelo git
# Para remover o arquivo do rastreamento, use:
# git rm --cached -r vm bkp
# git commit -m "Removendo arquivos rastreados para respeitar o .gitignore"


# Importações
import os
import xml.etree.ElementTree as ET
from utilitarios import parametros
from utilitarios import nomes_validos
from utilitarios import converter_data

import pandas as pd
import streamlit as st
import plotly.express as px
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

def get_xml_servico():

    def _listar_arquivos_xml():
        path_xml = parametros['path']
        lista_xml = [f for f in os.listdir(path_xml) if f.endswith('.xml')]
        for xml in lista_xml:
            if not _validar_xml(xml):
                return
        return lista_xml
    
    def _validar_xml(caminho_arquivo: str) -> bool:
        """
        ET.parse garante que o XML esteja bem formado (senão lança ParseError).
        root.tag valida o nó raiz.
        find permite verificar a existência de nós obrigatórios (Settings, LanguageCode).
        Retorna True se tudo estiver correto, ou False com mensagens explicativas.
        """
        try:
            # Tenta carregar e parsear o XML
            tree = ET.parse(caminho_arquivo)
            root = tree.getroot()

            # Verifica se o nó raiz é MeetingWorkBook
            if root.tag != "MeetingWorkBook":
                print(f"Nó raiz inválido: esperado 'MeetingWorkBook', encontrado '{root.tag}'")
                return False

            # Verifica se existe o nó <Settings>
            settings = root.find("Settings")
            if settings is None:
                print("Nó <Settings> não encontrado.")
                return False

            # Verifica se existe o nó <LanguageCode> dentro de <Settings>
            lang = settings.find("LanguageCode")
            if lang is None or not lang.text:
                print("Nó <LanguageCode> não encontrado ou vazio.")
                return False

            # Se passou por todas as verificações
            print("XML válido.")
            return True

        except ET.ParseError as e:
            print(f"Erro de parsing: XML malformado. Detalhes: {e}")
            return False
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return False
    
    _lista_de_xml = _listar_arquivos_xml()

    if not _lista_de_xml:
        return 
    
    # Inicialize a lista de participantes
    lst_designacoes = []

    for arquivo in _lista_de_xml:
        caminho_xml = os.path.join(arquivo)
        tree = ET.parse(caminho_xml)
        root = tree.getroot()

        # Iterar sobre cada "Meeting" para capturar suas informações
        for meeting in root.findall(".//Meeting"):
            
            reuniao = {}

            # Capturar a data específica do Meeting
            data_atributo = meeting.find("Date").attrib.get("ThisWeek")

            # Formatar para DD/MM/AAAA
            data_formatada = f"{data_atributo[7:9]}/{data_atributo[5:7]}/{data_atributo[3:5]}"

            reuniao["data"] = data_formatada

            # Capturar informações principais do Meeting
            chairman = meeting.find("Chairman").text if meeting.find(
                "Chairman") is not None else ""

            prayer_open = meeting.find("PrayerOpen").text if meeting.find(
                "PrayerOpen") is not None else ""                                

            prayer_end = meeting.find(
                ".//PrayerEnd").text if meeting.find(".//PrayerEnd") is not None else ""                
            
            # Atualizar informações no dicionário de designações
            if chairman in nomes_validos:
                reuniao["presidencia"] = chairman
            else:
                print(f'Participante {chairman} não permitido' )
                return
            
            if prayer_open in nomes_validos:
                reuniao["oracao_inicial"] = prayer_open
            else:
                print(f'Participante {prayer_open} não permitido' )
                return

            if prayer_end in nomes_validos:
                reuniao["oracao_final"] = prayer_end
            else:
                print(f'Participante {prayer_end} não permitido' )
                return

            # Capturar informações do TFGW
            tfgw_items = meeting.findall(".//TFGWItem")
            for tfgw_item in tfgw_items:
                index = tfgw_item.attrib.get("Index")
                name = tfgw_item.find("Name").text if tfgw_item.find(
                    "Name") is not None else ""
                if name:
                    if name in nomes_validos:
                        if index == '1':
                            reuniao["Tesouros"] = name
                        elif index == '2':
                            reuniao["Joias"] = name
                    else:
                        print(f'Participante {name} não permitido')
                        return


            # Capturar informações do LAC
            lac_items = meeting.findall(".//LACItem")
            discurso_lac = 1
            for lac_item in lac_items:
                name = lac_item.find("Name").text if lac_item.find(
                    "Name") is not None else ""
                if name:
                    if name in nomes_validos:
                        if discurso_lac == 1:
                            reuniao["discurso1"] = name
                        if discurso_lac == 2:
                            reuniao["discurso2"] = name
                        if discurso_lac == 3:
                            reuniao["discurso3"] = name
                    else:
                        print(f'Participante {name} não permitido')
                        return

            # Capturar informações do CongregationBibleStudy
            cbs = meeting.find(".//CongregationBibleStudy")

            # conductor = cbs.find("Conductor").text if cbs and cbs.find("Conductor") is not None else ""
            conductor = cbs.find("Conductor").text if cbs is not None and cbs.find(
                "Conductor") is not None else ""
            
            # reader = cbs.find("Reader").text if cbs and cbs.find("Reader") is not None else ""
            reader = cbs.find("Reader").text if cbs is not None and cbs.find(
                "Reader") is not None else ""                
            
            if conductor:
                if conductor in nomes_validos:
                    reuniao["estudo"] = conductor
                else:
                    print(f'Participante {conductor} não permitido')
                    return

            if reader:
                if reader in nomes_validos:
                    reuniao['leitor'] = reader
                else:
                    print(f'Participante {reader} não permitido')
                    return

            lst_designacoes.append(reuniao)
                
    return lst_designacoes

def xml_servico_to_csv():

    minha_lista_de_dicionarios = get_xml_servico()
    linhas_formatadas = []

    for d in minha_lista_de_dicionarios:
        
        linhas_formatadas.append({
            "Data": d["data"],                     # já está no formato dd/mm/yyyy
            "Presidencia": d["presidencia"],
            "Oracao Inicial": d["oracao_inicial"],
            "Tesouros": d["Tesouros"],
            "Joias": d["Joias"],
            "Discurso1": d["discurso1"],
            "Discurso2": "",                        # campo vazio
            "Estudo": d["estudo"],
            "Leitor": d["leitor"],
            "Oracao Final": d["oracao_final"]
        })

    df = pd.DataFrame(linhas_formatadas)

    # Salvando o CSV com separador ";"
    df.to_csv("analise.csv", sep=";", index=False, encoding="latin1")
    print("Arquivo 'saida.csv' gerado com sucesso!")
    

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

# xxx
def mostrar_frequencia():
    xml_servico_to_csv()
    st.markdown("## 📊 Frequência de Participações")
    #caminho_csv = r'C://docarlos//quadro_flamboyant_teste//teste_streamlit//analise.csv'
    caminho_csv = 'analise.csv'

    try:
        df = pd.read_csv(caminho_csv, sep=';', encoding='latin1')
        df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%y')
    except Exception as e:
        st.error(f"Erro ao carregar o CSV: {e}")
        return

    # Filtro por data inicial
    data_minima = df['Data'].min().date()
    data_maxima = df['Data'].max().date()
    data_inicial = st.date_input(
        "Mostrar participações a partir de:",
        value=data_minima,
        min_value=data_minima,
        max_value=data_maxima,
        format="DD/MM/YYYY"
    )
    
    if data_inicial is not None:
        # Aplica o filtro apenas se a data for válida
        df = df[df['Data'] >= pd.to_datetime(data_inicial)]

        # Exibe a data no formato dd/mm/yyyy
        st.markdown(f"📆 **Data selecionada:** '{data_inicial.strftime('%d/%m/%Y')}'")    
    else:
        st.warning("Por favor, selecione uma data válida.")

    # Formato longo
    df_long = df.melt(id_vars=['Data'], var_name='Modalidade', value_name='nome')
    df_long = df_long.dropna()
    df_long['nome'] = df_long['nome'].str.strip()

    # Contagem
    df_participacoes = df_long.groupby(['nome', 'Modalidade']).size().reset_index(name='qtd')
    df_participacoes['qtd'] = df_participacoes['qtd'].astype(int)

    # Filtros
    nomes = st.multiselect("🔍 Filtrar por nome(s):", sorted(df_participacoes['nome'].unique()))
    modalidades = st.multiselect("🎤 Filtrar por modalidade:", sorted(df_participacoes['Modalidade'].unique()))

    df_filtrado = df_participacoes.copy()
    if nomes:
        df_filtrado = df_filtrado[df_filtrado['nome'].isin(nomes)]
    if modalidades:
        df_filtrado = df_filtrado[df_filtrado['Modalidade'].isin(modalidades)]

    # Gráfico
    fig = px.bar(
        df_filtrado.sort_values(by='nome'),
        x='qtd',
        y='nome',
        color='Modalidade',
        orientation='h',
        title='Participações por Pessoa e Modalidade',
        labels={'qtd': 'Qtd. Participações', 'nome': 'Participante'},
        height=600
    )

    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=1  # força inteiros no eixo X
        ),
        yaxis=dict(
            categoryorder='category descending'  # ordena nomes alfabeticamente
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    if st.button("Início"):
        st.session_state["pagina"] = "home"
        st.rerun()

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

    #xxx
    if "frequencia" in permissoes:
        if st.button("📊 Frequência de Participações"):
            st.session_state["pagina"] = "frequencia"
            st.rerun()

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
# if not st.session_state["logado"]:
#     usuario_cookie = cookies.get("usuario")
#     senha_cookie = cookies.get("senha")
#     if usuario_cookie and senha_cookie:
#         if autenticar_usuario(usuario_cookie, senha_cookie):
#             st.session_state.update({
#                 "logado": True,
#                 "usuario": usuario_cookie,
#                 "pagina": "home"
#             })
#             st.rerun()

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
        # xxx            
        elif st.session_state.get("pagina") == "frequencia":
            mostrar_frequencia()

    with tab2:
        render_eventos(events)

print('Teste')
get_xml_servico()        
