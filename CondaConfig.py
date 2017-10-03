#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Script: Creation Conda Config
Updated:     20171003, almeidalz
Copyright:   Luiz Almeida 
Contact: almeidalz@hotmail.com
Licence: <free version v.1.1, for Python>
--------------------------------------------------------------------------
Use (US): The purpose of this script is to create the proxy configuration file 
     for the Conda Python interpreter. Free use, please quote the source.
     The script can be compiled directly in the anaconda prompt or in the 
     interpreter, it will create in the user directory the file ".condarc",
     it is enough that you inform in the variables "UserName"; "Password";
     "ProxyName" and "Porta" your proxy settings. Execute as administrator.
     
Uso (PT):  O objetivo deste script é criar o arquivo de configuração do proxy
      Para o interpretador Conda Python. Uso gratuito, por favor cite a fonte.
      O script pode ser compilado diretamente no prompt do anaconda ou no
      Interpretador, criará no diretório do usuário o arquivo ".condarc",
      Basta que você informe nas variáveis "UserName"; "Senha";
      "ProxyName" e "Port" suas configurações de proxy. Execute como admin.
'''
#Inserir o nome de usuário proxy
UserName = 'username@servidor.com' 
#Inserir a senha de usuário do proxy
Password = '1234' 
#Inserir nome do proxy local
ProxyName = 'proxy.servidor.com'
#Porta de acesso do servidor de proxy 
Port = '8080'

def Conda_Config(UserName, Password, ProxyName, Port):

    #importa a biblioteca os
    import os
    #muda o diretório de trabalho para o diretório do usuário 
    os.chdir(os.path.expanduser("~"))
    #mostra o novo diretório
    print os.getcwd()
    
    #Verifica a existência do arquivo de configuração, se não existir cria.
    if not os.path.exists('.condarc'):
        
        with open('.condarc','a')  as ArqConfig:
            #Configurações do arquivo .condarc para o servidor de proxy
            ArqConfig.write(('proxy_servers:')+"\r\n")
            ArqConfig.write(('   http: http://' + UserName + ':' + Password + '@' + ProxyName + ':' + Port)+"\r\n")
            ArqConfig.write(('   https: https://' + UserName + ':' + Password + '@' + ProxyName + ':' + Port)+"\r\n")
            ArqConfig.close()
        
    else:
        #Caso o arquivo de configuração já exista ele mostrará onde esta localizado.
        print 'Arquivo de configuração existente em: ', os.getcwd()
    
Conda_Config(UserName, Password, ProxyName, Port)
