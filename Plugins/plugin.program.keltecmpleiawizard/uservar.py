import os, xbmc, xbmcaddon
import binascii
#########################################################
### User Edit Variables #################################
#########################################################
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR gold]-[COLOR blue][B]KelTecMP Leia [COLOR red]Wizard[/B][COLOR gold]-[/COLOR]'
BUILDERNAME    = 'GUI Wiz'
#########################Make sure to change the repo to yours!!!!
EXCLUDES       = [ADDON_ID, 'repository.firetvguru', 'roms', 'My_Builds', 'backupdir']
BUILDFILE      = 'https://pastebin.com/raw/g9VeLWS4'
UPDATECHECK    = 0
APKFILE        = 'http://keltecmp-iptv.tk/apks.txt'
YOUTUBETITLE   = 'Suporte Videos' 
YOUTUBEFILE    = 'http://keltecmp-iptv.tk/you.txt'
ADDONFILE      = 'https://pastebin.com/raw/zsifs1cM'
ADVANCEDFILE   = 'http://keltecmp-iptv.tk/Advanced.txt'
ROMPACK        = 'http://keltecmp-iptv.tk/rom-packs.txt'
EMUAPKS        = 'http://'
ADDONPACK      = 'http://'
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################

##Alway test to see the color combo!!

#### NEW GUI THEME ###################################
# Choose from the following 
# Only these colors avalable
# white , blue , orange , yellow , red , purple , pink , lime , cyan, green
#Button focus color
FOCUS_BUTTON_COLOR = 'blue'
EXIT_BUTTON_COLOR = 'red'
#Highlight outline for lists
HIGHLIGHT_LIST = 'blue'
##No TXT file Banner
NO_TXT_FILE = 'red'

############################################
############################################
### The full list of colors for below can found @ https://forum.kodi.tv/showthread.php?tid=210837

#Top Main buttons
MAIN_BUTTONS_TEXT = 'orange'
#All other buttons
OTHER_BUTTONS_TEXT = 'lime'
#all list text color
##FYI any color placed in the txt file will overide this
LIST_TEXT = 'khaki'


#Description text title color
DES_T_COLOR = 'cornflowerblue'
#Description color
DESCOLOR = 'cyan'

#Wizard title name and verion color
WIZTITLE = 'KelTecMP Leia Wizard'
WIZTITLE_COLOR = 'chartreuse'
VERTITLE_COLOR = 'lightsaltegray'
VER_NUMBER_COLOR = 'red'
############################################################

## The colors and theme below is still used for the pop up dialogs
##Alway test to see the color combo
# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'blue'
COLOR2         = 'yellow'
COLOR3         = 'red'
COLOR4         = 'snow'
COLOR5         = 'lime'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR2+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR2+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
THEME6         = '[COLOR '+COLOR3+'][B]%s[/B][/COLOR]'



#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/Settings-icon.png'
ICONMAINT      = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/maintenance.png'
ICONAPK        = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/apk.png'
ICONADDONS     = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/addons.png'
ICONYOUTUBE    = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/youtube.png'
ICONSAVE       = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/save.png'
ICONTRAKT      = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/trakt.png'
ICONREAL       = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/real.png'
ICONLOGIN      = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/login.png'
ICONCONTACT    = 'http://keltecmp-iptv.tk/icon.png'
ICONSETTINGS   = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/settings.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '~'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Obrigado por escolher o KelTecMP Leia Wizard.'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://keltecmp-iptv.tk/icon.png'
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = 'http://'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'http://'
# Url to folder zip is located in
REPOZIPURL     =  'http://'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'http://keltecmp-iptv.tk/wizard-notification.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font13'
HEADERMESSAGE  = 'KelTecMP Leia Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Font for Notification Window
FONTSETTINGS   = 'Font12'
# Background for Notification Window
BACKGROUND     = 'https://i97.servimg.com/u/f97/19/82/45/70/15029910.png'
############################    #############################