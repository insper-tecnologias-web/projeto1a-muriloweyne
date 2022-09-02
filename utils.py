import json


def extract_route(req):
    route = req.split(" ")[1][1:]
    return route    

def read_file(path):
    with open(path,'rb') as f:
        return f.read()

def load_data(file):
    with open('data/' + file,'r') as f:
        return json.loads(f.read())

def load_template(file):
    with open('templates/' + file, 'r') as f:
        return f.read()

def add_note(dic):
    file_data = load_data('notes.json')
    file_data.append(dic)
    with open('data/notes.json','w',encoding="UTF-8") as fi:
        json.dump(file_data,fi,indent=4,ensure_ascii=False)

def build_response(body='', code=200, reason='OK', headers=''):
    val = ('HTTP/1.1 ' + str(code) + ' ' + reason + '\n' + headers + '\n\n' + body).encode() if (headers != '') else ('HTTP/1.1 ' + str(code) + ' ' + reason + '\n\n' + body).encode()
    return val 


