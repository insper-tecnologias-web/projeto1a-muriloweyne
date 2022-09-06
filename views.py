from utils import load_data, load_template, add_note,build_response
from urllib.parse import unquote_plus
import database

db = database.Database("data/projeto1")
note = database.Note("")


def index(request):
    post = False
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            # AQUI É COM VOCÊ
            chave_valor = unquote_plus(chave_valor)
            vals = chave_valor.split('=')
            params[vals[0]] = vals[1]
        post = True
        if("delete" in params):
            db.delete(params["delete"])
        else:
            # Verifica se os campos não estão vazios
            if (params["titulo"] != "" and params["detalhes"] != ""):
                note = database.Note(None, params["titulo"], params["detalhes"])
                db.add(note)

    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...
    
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=dados.id, title=dados.title, details=dados.content)
        for dados in db.get_all()
    ]
    notes = '\n'.join(notes_li)
    print("notes li",notes_li)
    
    resp = build_response(body=load_template('index.html').format(notes=notes)) if not(post) else build_response(code=300, reason="See Others" ,body=load_template('index.html').format(notes=notes)) 

    return resp