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
		function11,
		function12,
		function13,
		function14,
		function15,
	    function16
        )
        
    call = dialog.select('[COLOR=darkred]KelTecMP Builds & Downloads[/COLOR]', [
	'[COLOR=gold]  **** Downloads para instalacao manual AQUI **** [/COLOR]',
	'[COLOR=dodgerblue]  **** DOWNLOAD KODI 18.2 KelTecMP APK COM WIZARD OBS:(TEM QUE ATIVAR O ADD-ON) **** [/COLOR]', 
	'[COLOR=dodgerblue]  **** DOWNLOAD KODI 16.1 KelTecMP-CEMC APK COM WIZARD **** [/COLOR]',	
    '[COLOR=darkred]  **** Video Tutorial OBS: KODI 18.2 APK EM BREVE **** [/COLOR]',
    '[COLOR=darkred]  **** Video Tutorial OBS: KODI 16.1 APK EM BREVE **** [/COLOR]',
	'[COLOR=gold] **** Download do Repository para Atualizar a BUILD ****[/COLOR]',
    '[COLOR=darkred]  **** Video Tutorial usando ES File Explorer - Google Play **** [/COLOR]',
	'[COLOR=darkred]  **** Video Tutorial Para Windows **** [/COLOR]',
	'[COLOR=lime]  **** Ajudar Projeto ****[/COLOR]',
	'[COLOR=red]  **** YouTube Deixe Seu Like e Inscreva-se ****  [/COLOR]',
	'[COLOR=blue]  **** Facebook Group **** [/COLOR]',
	'[COLOR=lime]  **** Alicativo IPTV Premium **** [/COLOR]',
	'[COLOR=lime]  **** Gerar Usuario e Senha **** [/COLOR]',
	'[COLOR=lime]  **** Site Para Mais Detalhes **** [/COLOR]',
    '[COLOR=lime]  **** Whatsapp **** [/COLOR]',
	'[COLOR=lime]  **** Ajuda Por Dados de Conta OBS: Nao Obrigatorio ****[/COLOR]',])
	
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 1:
            return
        func = funcs[call-16]
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
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://keltecmp.tk/downloads' ) )
    else:
        opensite = webbrowser . open('http://keltecmp.tk/downloads')

def function2():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://bit.ly/kodi-keltec-18' ) )
    else:
        opensite = webbrowser . open('http://bit.ly/kodi-keltec-18')

def function3():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://bit.ly/kodi-keltec-16' ) )
    else:
        opensite = webbrowser . open('http://bit.ly/kodi-keltec-16')
        
def function4():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.youtube.com/c/KeltecMPIPTV' ) )
    else:
        opensite = webbrowser . open('https://www.youtube.com/c/KeltecMPIPTV')
		
def function5():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.youtube.com/c/KeltecMPIPTV' ) )
    else:
        opensite = webbrowser . open('https://www.youtube.com/c/KeltecMPIPTV')			
	
def function6():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://keltecmp.tk/repo/KeltecMP.repository-0.0.4.zip' ) )
    else:
        opensite = webbrowser . open('http://keltecmp.tk/repo/KeltecMP.repository-0.0.4.zip')
		
		
def function7():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.youtube.com/watch?v=CoTblBLoh34' ) )
    else:
        opensite = webbrowser . open('https://www.youtube.com/watch?v=CoTblBLoh34')		

def function8():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.youtube.com/watch?v=vuTyoc9ZKJQ' ) )
    else:
        opensite = webbrowser . open('https://www.youtube.com/watch?v=vuTyoc9ZKJQ')

def function9():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://app.picpay.com/user/keltecmp.iptv' ) )
    else:
        opensite = webbrowser . open('https://app.picpay.com/user/keltecmp.iptv')		

def function10():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.youtube.com/c/KeltecMPIPTV' ) )
    else:
        opensite = webbrowser . open('https://www.youtube.com/c/KeltecMPIPTV')	

def function11():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.facebook.com/groups/1637920199584939' ) )
    else:
        opensite = webbrowser . open('https://www.facebook.com/groups/1637920199584939')

def function12():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://iptv.starbr.in/StarBR.apk' ) )
    else:
        opensite = webbrowser . open('http://iptv.starbr.in/StarBR.apk')	
		
def function13():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://keltecmp-iptv.ga' ) )
    else:
        opensite = webbrowser . open('http://keltecmp-iptv.ga')	
		
def function14(): 
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://keltecmp-iptv.tk' ) )
    else:
        opensite = webbrowser . open('http://keltecmp-iptv.tk')	

def function15(): 
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://bit.ly/kel-WhatsApp' ) )
    else:
        opensite = webbrowser . open('http://bit.ly/kel-WhatsApp')
		
def function16(): 
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://ia801402.us.archive.org/0/items/Doaes/doa%c3%a7%c3%b5es.txt' ) )
    else:
        opensite = webbrowser . open('http://ia801402.us.archive.org/0/items/Doaes/doa%c3%a7%c3%b5es.txt')
		
menuoptions()