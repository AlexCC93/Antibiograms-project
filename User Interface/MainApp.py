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
try:
	import numpy as np
except ImportError as e:
	raise e,"Se requiere modulo Numpy"



class antibiogApp(wx.Frame):

	def __init__(self, parent):
		super(antibiogApp, self).__init__(parent)
		

		self.initGUI()
		self.Centre()

	def initGUI(self):
		global flag_main_window
		global circles
		#Menu window  
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

			button_cred=wx.Button(self.panel,wx.ID_ANY,label='Info.',size=(350,40))
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

			self.SetSize(300,500)
			self.SetSizeHints(300,500,350,535)

		#Main Data Window
		elif flag_main_window==2:
			
			self.panel_2=wx.Panel(self)
			box_vert_main_window=wx.BoxSizer(wx.VERTICAL)
			box_hor_picture_data=wx.BoxSizer(wx.HORIZONTAL)
			box_vert_data=wx.BoxSizer(wx.VERTICAL)
			box_hor_buttons=wx.BoxSizer(wx.HORIZONTAL)

			fonte2=wx.Font(12,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_LIGHT)
			#Data Display panel
			m,n,s = np.shape(circles)
			text=[]
			static_texts=[]
			for x in range(n):
				text.append('centro x: '+str(circles[0,x,0])+'\tcentro y: '+str(circles[0,x,1])+'\tRadio:'+str(circles[0,x,2]))
				static_texts.append(wx.StaticText(self.panel_2,label=text[x],style=wx.ALIGN_LEFT))
				static_texts[x].SetFont(fonte2)
				box_vert_data.Add(static_texts[x], flag=wx.ALL,border=20)


			#Picture panel			
			self.picture = wx.StaticBitmap(self.panel_2,wx.ID_ANY,wx.Bitmap("picture.jpeg"))
			box_hor_picture_data.Add(self.picture,flag=wx.RIGHT|wx.TOP|wx.BOTTOM|wx.EXPAND|wx.ALIGN_LEFT,border=15)


			#Buttons Panel
			button_new_picture=wx.Button(self.panel_2,label='Nueva Foto')
			button_edit=wx.Button(self.panel_2,label='Editar')
			button_save=wx.Button(self.panel_2,label='Guardar')
			button_back=wx.Button(self.panel_2,label='Atras')

			# button_new_picture.Bind(wx.EVT_BUTTON, self.onTakeNewPicture)
			# button_edit.Bind(wx.EVT_BUTTON, onEditPicture)
			# button_save.Bind(wx.EVT_BUTTON, self.onSaveData)
			# button_back.Bind(wx.EVT_BUTTON, onBackToMenu)

			box_hor_buttons.Add(button_new_picture, flag=wx.EXPAND|wx.ALL,border=25)
			box_hor_buttons.Add(button_edit, flag=wx.EXPAND|wx.ALL,border=25)
			box_hor_buttons.Add(button_save, flag=wx.EXPAND|wx.ALL,border=25)
			box_hor_buttons.Add(button_back, flag=wx.EXPAND|wx.ALL,border=25)

			#Ordering Panels and BoxSizers
			box_hor_picture_data.Add(box_vert_data,flag=wx.ALIGN_RIGHT,border=2)
			box_vert_main_window.Add(box_hor_picture_data,flag=wx.CENTER,border=5)
			box_vert_main_window.Add(box_hor_buttons,flag=wx.CENTER,border=5)
			
			self.panel_2.SetSizer(box_vert_main_window)


		#Info. Window
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

#Global statements
flag_main_window = 1
app = wx.App()
wind_app = antibiogApp(None)
app.MainLoop()
#Radious and centers of circles example picture 2.jpeg
circles=np.array([[[246, 134, 39],[48, 116, 39],[186, 214, 39],[218, 62, 40]]])

def main():

	global wind_app
	global flag_main_window

	if flag_main_window == 2:
		app_second = wx.App()
		wind_app_second = antibiogApp(None)
		app_second.MainLoop()


    

if __name__ == '__main__':
    main()	
