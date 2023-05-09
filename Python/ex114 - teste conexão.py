import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Esse site não está acessível o momento.')
else:
    print('Tudo OK')
    print(site.read())