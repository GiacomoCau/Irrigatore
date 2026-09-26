
print() # indispensabile per segnalare la fine dell'header e l'inizio del corpo

import sys, os
from urllib.parse import unquote

query = unquote(os.environ.get('query_string', ''))
blank = query.find(' ')
[service, args] = [query, ''] if blank == -1 else [query[:blank], query[blank+1:]]
match service:
    case 'load':
        print(open('config.py', 'r').read())
    case 'save':
        post = sys.stdin.read(int(os.environ.get('content_length', '0')))
        open('config.py', 'w').write(post)
        print("saved!")
        import psutil, subprocess
        if os.path.exists('pid'):
            try:
                process = psutil.Process(int(open('pid', 'r').read()))
            except:
                pass
            else:
                process.kill()
        process = subprocess.Popen(['python', 'irrigatore.py'])
        open('pid', 'w').write(str(process.pid))
    case 'start':
        import subprocess
        process = subprocess.Popen(['python', 'manuale.py', args])
        print(str(process.pid))
    case 'wait':
        import psutil
        pid = int(args)
        process = psutil.Process(pid)
        if process.is_running(): process.wait()
        print(args + ' ended')
    case 'stop':
        import psutil, config
        from util import stazioni, gpio
        ips = args.split()
        try:
            process = psutil.Process(int(ips[0]))
        except psutil.NoSuchProcess:
            print(args + ' not exist')
        except psutil.AccessDenied:
            print(args + ' not accessible')
        else:
            process.kill()
            if ips[1].isdigit():
                stazione = stazioni[int(ips[1])-1]
                gpio.output(stazione, gpio.LOW)            
            else:
                durate = config.progs[ips[1]][2] if len(ips) == 2 else [[s,m] for (s,m) in config.progs[ips[1]][2] if s == int(ips[2])]
                for [s,m] in durate:
                    stazione = stazioni[s-1]
                    gpio.output(stazione, gpio.LOW)
            print(args + ' stopped')
        sys.stdout.flush()
        psutil.Process(os.getpid()).kill()
    case _:
        print('servizio ' + service + ' non supportato')
