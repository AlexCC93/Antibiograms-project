'''It is the first design. I used wxPython for it
The design include a menu at begining of the app,
then a window that shows results of proves. In the future,
I will add a second window where we will be able to make changes at results 
'''
try:
	import cv2
except ImportError as e:
	raise e,"Se requiere el modulo de Open CV"
try:
	import wx
except ImportError as e:
	raise e,"Se requiere el modulo wxPython"


class antibiogApp(wx.Frame):

	def __init__(self, parent):
		super(antibiogApp, self).__init__(parent)
		

		self.initGUI()
		self.Centre()

	def initGUI(self):
		global flag_main_window
		
		  
		if flag_main_window==1:
			
			#self.Bind(wx.EVT_CLOSE, self.onEventClose)
			self.panel=wx.Panel(self)
			self.panel.SetBackgroundColour(wx.BLACK)
			fonte=wx.Font(14,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)
			vert_menu_box=wx.BoxSizer(wx.VERTICAL)
			
			button_new=wx.Button(self.panel,wx.ID_ANY,label='Nuevo',size=(350,40))
			button_new.SetFont(fonte)
			button_new.SetBackgroundColour(wx.BLACK)
			button_new.SetForegroundColour(wx.WHITE)
			self.panel.Bind(wx.EVT_BUTTON,onButtonNewPress,button_new)
			vert_menu_box.Add(button_new,flag=wx.ALIGN_CENTER|wx.ALL|wx.EXPAND,border=10)

			button_cred=wx.Button(self.panel,wx.ID_ANY,label='Creditos',size=(350,40))
			button_cred.SetFont(fonte)
			button_cred.SetBackgroundColour(wx.BLACK)
			button_cred.SetForegroundColour(wx.WHITE)
			self.panel.Bind(wx.EVT_BUTTON ,onButtonCredPress , button_cred)
			vert_menu_box.Add(button_cred,flag=wx.ALIGN_CENTER|wx.ALL|wx.EXPAND,border=10)

			button_close=wx.Button(self.panel,wx.ID_ANY,label='Cerrar',size=(350,40))
			button_close.SetFont(fonte)
			button_close.SetBackgroundColour(wx.BLACK)
			button_close.SetForegroundColour(wx.WHITE)
			self.panel.Bind(wx.EVT_BUTTON , self.onEventClose ,button_close)
			vert_menu_box.Add(button_close,flag=wx.ALIGN_CENTER|wx.ALL|wx.EXPAND,border=10)

			self.logo_cato = wx.StaticBitmap(self.panel,wx.ID_ANY,wx.Bitmap("LogoCatoBW.jpg",wx.BITMAP_TYPE_ANY))
			vert_menu_box.Add(self.logo_cato,flag=wx.ALIGN_BOTTOM|wx.ALIGN_CENTRE|wx.ALL , border=0)


			self.panel.SetSizer(vert_menu_box)

			self.SetSizeWH(300,500)
			self.SetSizeHints(300,500,350,535)

		
		elif flag_main_window==2:
			print "Cambiaste de pantalla"
		elif flag_main_window==3:
			print "Cambiaste a la 3ra pantalla"

		#self.Bind(wx.EVT_CLOSE,self.onEventClose)

		self.SetTitle('Halo`s Diameter Detector')
		self.Show(True)


	def onEventClose(self,e):
		# self.Close()
		dial = wx.MessageDialog(None, 'Estas seguro?', 'Pregunta',    wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			self.Destroy()
		else:
			e.Veto()
	
			
def onButtonNewPress(e):
	global wind_app
	global flag_main_window

	flag_main_window = 2
	wind_app.Close()

	
def onButtonCredPress(e):
	global wind_app
	global flag_main_window
	flag_main_window = 3
	wind_app.Close()


flag_main_window = 1
app = wx.App()
wind_app = antibiogApp(None)
app.MainLoop()

def main():

	global wind_app
	global flag_main_window

	if flag_main_window == 2:
		app_second = wx.App()
		wind_app_second = antibiogApp(None)
		app_second.MainLoop()


    

if __name__ == '__main__':
    main()	
