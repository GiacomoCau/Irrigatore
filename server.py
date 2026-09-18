import os, sys
print() # indispensabile per segnalare la fine dell'header e l'inizio del corpo
metodo = os.environ.get("REQUEST_METHOD", "get").lower()
match metodo:
    case 'get':
        print(open('config.py', 'r').read())
    case 'post':
        post = sys.stdin.read(int(os.environ.get("CONTENT_LENGTH", "0")))
        open('config.py', 'w').write(post)
        print("saved!")
    case _:
        print('metodo ' + metodo + ' non supportato')
