#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Script: Creation Conda Config
Updated:     20171217, almeidalz
Copyright:   Luiz Almeida 
Contact: almeidalz@hotmail.com
Licence: <free version v.1.2, for Python>
--------------------------------------------------------------------------
Use (US): Purpose of this script is to create the proxy configuration file 
     for the Conda Python interpreter. Free use, please quote the source.
     The script can be compiled directly in the anaconda prompt or in the 
     interpreter, it will create in the user directory the file ".condarc",
     it is enough inform in the variables "UserName"; "Password";
     "ProxyName" and "Porta" your proxy settings. Execute as administrator.
'''

#Inserir o nome de usuário proxy
UserName = 'username@servidor.com' 
#Inserir a senha de usuário do proxy
Password = '1234' 
#Inserir nome do proxy local
ProxyName = 'proxy.servidor.com'
#Porta de acesso do servidor de proxy 
Port = '8080'

def create(UserName, Password, ProxyName, Port):
    
    with open('.condarc','a')  as ArqConfig:
        #Configurações do arquivo .condarc para o servidor de proxy
        ArqConfig.write(('proxy_servers:')+"\r\n")
        ArqConfig.write(('   http: http://' + UserName + ':' + Password + '@' + ProxyName + ':' + Port)+"\r\n")
        ArqConfig.write(('   https: https://' + UserName + ':' + Password + '@' + ProxyName + ':' + Port)+"\r\n")
        ArqConfig.close()


#importa a biblioteca os
import os
#muda o diretório de trabalho para o diretório do usuário.
os.chdir(os.path.expanduser("~"))

#Verifica a existência do arquivo de configuração.
if not os.path.exists('.condarc'):
    
    create(UserName, Password, ProxyName, Port)
        
else:
    
    #Caso o arquivo de configuração já exista ele mostrará onde esta localizado.
    print('.condarc existente em: ', os.getcwd())
    dialog = raw_input('Deseja substituir o arquivo existente ? [y/n]:')
    
    if dialog == 'y':
        
        create(UserName, Password, ProxyName, Port)
        print('.condarc substituido')
        
    else:
        
        pass
