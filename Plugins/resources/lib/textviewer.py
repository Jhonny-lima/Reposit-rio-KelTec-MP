from tools import *

ACTION_SELECT = 7
ACTION_NAV_BACK = 92

BaseWindow = xbmcgui.WindowXMLDialog


class textViewer(BaseWindow):

    TEXT_WINDOW_ID = 5

    def __init__(self, *args, **kwargs):
        self.text = None


    @staticmethod
    def createTextViewer():
        return textViewer('DialogTextViewer.xml', ADDON_PATH)


    def onAction(self, action):
        if (action == ACTION_NAV_BACK or action == ACTION_SELECT):
            self.close()


    def onInit(self):
        self.getControl(textViewer.TEXT_WINDOW_ID).setText(self.text)


    def close(self):
        BaseWindow.close(self)