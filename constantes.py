# Estilização.
estilo = """
        <style>
        /* Corpo do aplicativo */
        body {
            background-color: #F5F7FA;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Títulos */
        h1 {
            color: #2C3E50;
            font-size: 32px;
            text-align: center;
            margin-bottom: 20px;
        }
        h2 {
            color: #34495E;
            font-size: 24px;
            margin-bottom: 10px;
        }

        /* Cartões */
        .card {
            background-color: #FFFFFF;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        /* Botões */
        .stButton>button {
            background-color: #3498DB;
            color: white;
            border-radius: 8px;
            border: none;
            font-size: 16px;
            font-weight: bold;
            padding: 12px;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #2980B9;
            transform: scale(1.02);
        }

        /* Links */
        a {
            color: #1ABC9C;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            color: #16A085;
        }

        /* PDFs */
        iframe {
            border: 2px solid #E0E0E0;
            border-radius: 8px;
            margin-top: 20px;
        }
        </style>
    """

# Dicionário com os quadros de anúncios
quadros = {
    "a": {"titulo": "Reuniões para o Serviço de Campo", "arquivo": "servico_campo.png"},
    "b": {"titulo": "Designações de Discurso Público", "arquivo": "discurso_publico.png"},
    "c": {"titulo": "Anúncios e Lembretes", "arquivo": "anuncios.png"},
    "d": {"titulo": "Designações Reuniões Flamboyant", "arquivo": "reunioes_flamboyant.png"},
    "e": {"titulo": "Programação da Reunião do Meio de Semana", "arquivo": "programacao_meio_semana.png"},
    "f": {"titulo": "Designações para Limpeza do Salão do Reino", "arquivo": "limpeza_salao.png"},
    "g": {"titulo": "Relatório (Basta preencher, printar e enviar)", "arquivo": "relatorio.html"},
}

# Dados de usuários e permissões
usuarios = {
    "Jerome": {"senha": "@salmo8318", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Carlos": {"senha": "123", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Elber": {"senha": "@juizes10", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Lidyane": {"senha": "@ester10", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Rosa": {"senha": "@rute2", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Aron": {"senha": "@genesis10", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Silvia": {"senha": "@exodo10", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Armando": {"senha": "@edom1", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Carlos Montesino": {"senha": "@gibeon2", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "David Affonso": {"senha": "@zion12", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Ederson": {"senha": "@hebron11", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Edson": {"senha": "@siloe21", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Felipe Carneiro": {"senha": "@tarsis5", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Francisco Lezcano": {"senha": "@mambre54", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Gilmar": {"senha": "@betel7", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Giovani": {"senha": "@jerico20", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "José Francisco": {"senha": "@galileia5", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Marcos Ribeiro": {"senha": "@tabor12", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Marcos Woicjki": {"senha": "@egito1", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Paulo Carvalho": {"senha": "@nazare22", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Paulo Franco": {"senha": "@edom33", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Raphael Madeira": {"senha": "@hermom44", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Renato": {"senha": "8318", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Sergio Santos": {"senha": "@sidom21", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Anderson Valle": {"senha": "@moabe566", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Aparecida Spina": {"senha": "@samaria56", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Arileide": {"senha": "@sarepta56", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Arlene": {"senha": "@tiberias54", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Bibiane": {"senha": "@galatia32", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Carina": {"senha": "@bereia2", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Clarice": {"senha": "@jerusalem13", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Studzuski": {"senha": "@samuel23", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Cleusa": {"senha": "@babel58", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Daiane": {"senha": "@corinto13", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Daiane Graciela": {"senha": "@juda33", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Daniele": {"senha": "@magdala6", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Daniela Rodrigues": {"senha": "@samaria411", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Davides": {"senha": "@nazir23", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Derli": {"senha": "@mara10", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Doris": {"senha": "@arao123", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Dulce": {"senha": "@rute321", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Edilene": {"senha": "@sarai123", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Eduarda": {"senha": "@dbora411", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Emilly": {"senha": "@ester235", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Erica": {"senha": "@ligia4", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Esli": {"senha": "@gade22", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Ester": {"senha": "@hama41", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Eva": {"senha": "@adao245", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Felipe Gobato": {"senha": "@jair33", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Fernanda Machado": {"senha": "@joabe12", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Fernanda Madeira": {"senha": "@moises57", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Gabriela Ribeiro": {"senha": "@levi55", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Gicelle": {"senha": "@sela54", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Gisele": {"senha": "@noga55", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Gessica": {"senha": "@sarai", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Heitor": {"senha": "@urias50", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Henrique": {"senha": "@tequel50", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Herminio": {"senha": "@aram44", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Isabela": {"senha": "@tamar22", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Jahina": {"senha": "@maom44", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "João Batista": {"senha": "@nazaro55", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Josnei": {"senha": "@rebeca57", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Jucimere": {"senha": "@sodoma57", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Ketlin": {"senha": "@egito877", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Lara": {"senha": "@judite55", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Laura": {"senha": "@ismael44", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Lucas Daniel": {"senha": "@adriel66", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Luciana": {"senha": "@mical112", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Luis Claudio": {"senha": "@salao77", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Luiz Eleutério": {"senha": "@apolo7", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Luiz Nogueira": {"senha": "@asa4", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Marcia": {"senha": "@goel21", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Maria": {"senha": "@fe23", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Maria Dione": {"senha": "@orfa98", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Marli": {"senha": "@rute44", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Millena": {"senha": "@metusala12", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Miriam": {"senha": "@eva22", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Nadir": {"senha": "@tamar14", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Natalia": {"senha": "@cain78", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Nicolas": {"senha": "@jope33", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Noemia": {"senha": "@noe54", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Rafaela": {"senha": "@tiro99", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Regina": {"senha": "@hadasa76", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Rose Coutinho": {"senha": "@daniel77", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Roseli": {"senha": "@jonas25", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Roseni": {"senha": "@debora77", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Santina": {"senha": "@rabi55", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Silmara": {"senha": "sil1734", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Silvana": {"senha": "@simao34", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Simone": {"senha": "@mara76", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Thalita": {"senha": "@palma12", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Valdir": {"senha": "@bara12", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "M"},
    "Vanda": {"senha": "@sal91", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
    "Yamilet": {"senha": "@eloim57", "permissoes": ["a", "b", "c", "d", "e", "f", "g"], "sexo": "F"},
}
