import time
import xbmc
import os
import xbmcgui
import urllib2
import webbrowser


def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
		function3,
		function4,
		function5,
		function6,
		function7,
		function8,
		function9,
		function10,
		function11
		)
        
    call = dialog.select('[COLOR=darkred]KelTecMP Builds & Downloads[/COLOR]', [
	'[COLOR=crimson]  **** Downloads para instalacao manual AQUI **** [/COLOR]',
	'[COLOR=lime]  **** Ajudar Projeto ****[/COLOR]',
	'[COLOR=lime]  **** Ajuda Por Dados de Conta OBS: Nao Obrigatorio ****[/COLOR]',
	'[COLOR=red]  **** YouTube Deixe Seu Like e Inscreva-se ****  [/COLOR]',
	'[COLOR=cyan]  **** Facebook Group **** [/COLOR]',
	'[COLOR=yellow]  ************************ >>>KTMP<<< *********************** [/COLOR]',
	'[COLOR=lime]  **** Baixar Alicativo Premium **** [/COLOR]',
	'[COLOR=lime]  **** Gerar Usuario e Senha **** [/COLOR]',
	'[COLOR=lime]  **** Site Para Mais Detalhes **** [/COLOR]',
    '[COLOR=lime]  **** Whatsapp Suporte Premium **** [/COLOR]',
	'[COLOR=crimson]  ************************ >>>SAIR<<< *********************** [/COLOR]',])
	
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 1:
            return
        func = funcs[call-11]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

myplatform = platform()

def function1():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://keltecmp.ga' ) )
    else:
        opensite = webbrowser . open('http://keltecmp.ga')

def function2():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://bit.ly/Ajudar-projeto-KelTecMP' ) )
    else:
        opensite = webbrowser . open('http://bit.ly/Ajudar-projeto-KelTecMP')

def function3(): 
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://bit.ly/DOAR-XML' ) )
    else:
        opensite = webbrowser . open('http://bit.ly/DOAR-XML')		

def function4():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.youtube.com/c/KeltecMPIPTV' ) )
    else:
        opensite = webbrowser . open('https://www.youtube.com/c/KeltecMPIPTV')	

def function5():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.facebook.com/groups/KELTEC.MP' ) )
    else:
        opensite = webbrowser . open('https://www.facebook.com/groups/KELTEC.MP')

def function6(): 0
		
def function7():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://iptv.starbr.in/StarBR.apk' ) )
    else:
        opensite = webbrowser . open('http://iptv.starbr.in/StarBR.apk')	
		
def function8():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://bit.ly/2KAei7K' ) )
    else:
        opensite = webbrowser . open('http://bit.ly/2KAei7K')	
		
def function9(): 
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://keltecmp-iptv.tk' ) )
    else:
        opensite = webbrowser . open('http://keltecmp-iptv.tk')	

def function10(): 
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://bit.ly/kel-WhatsApp' ) )
    else:
        opensite = webbrowser . open('http://bit.ly/kel-WhatsApp')

def function11(): 0
		
menuoptions()