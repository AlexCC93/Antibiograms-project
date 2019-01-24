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
			
			fonte2=wx.Font(11,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_LIGHT)
			fonte_buttons=wx.Font(16,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_ITALIC,wx.FONTWEIGHT_LIGHT)
			self.panel_2=wx.Panel(self)
			bag_sizer = wx.GridBagSizer(5,5)
			box_results=wx.StaticBox(self.panel_2,label='Resultados')
			box_results.SetFont(fonte2)
			box_vert_data=wx.StaticBoxSizer(box_results,wx.VERTICAL)
			box_hor_buttons=wx.BoxSizer(wx.HORIZONTAL)

			
			#Data Display 
			m,n,s = np.shape(circles)
			text=[]
			static_texts=[]
			for x in range(n):
				text.append('Centro x: '+str(circles[0,x,0])+'	Centro y: '+str(circles[0,x,1])+'	Radio: '+str(circles[0,x,2]))
				static_texts.append(wx.StaticText(self.panel_2,label=text[x],style=wx.ALIGN_LEFT,size=(340,16)))
				static_texts[x].SetFont(fonte2)
				box_vert_data.Add(static_texts[x], flag=wx.ALL|wx.EXPAND,border=6)


			#Picture 			
			self.picture = wx.StaticBitmap(self.panel_2,wx.ID_ANY,wx.Bitmap("picture.jpeg"))
		


			#Buttons 
			button_new_picture=wx.Button(self.panel_2,label='Nueva Foto',size=(180,60))
			button_edit=wx.Button(self.panel_2,label='Editar',size=(180,60))
			button_save=wx.Button(self.panel_2,label='Guardar',size=(180,60))
			button_back=wx.Button(self.panel_2,label='Atras',size=(180,60))

			button_new_picture.SetFont(fonte_buttons)
			button_edit.SetFont(fonte_buttons)
			button_save.SetFont(fonte_buttons)
			button_back.SetFont(fonte_buttons)

			# button_new_picture.Bind(wx.EVT_BUTTON, self.onTakeNewPicture)
			# button_edit.Bind(wx.EVT_BUTTON, onEditPicture)
			# button_save.Bind(wx.EVT_BUTTON, self.onSaveData)
			# button_back.Bind(wx.EVT_BUTTON, onBackToMenu)

			box_hor_buttons.Add(button_new_picture, flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=20)
			box_hor_buttons.Add(button_edit, flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=20)
			box_hor_buttons.Add(button_save, flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=20)
			box_hor_buttons.Add(button_back, flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=20)

			#Setting separators
			line_hor=wx.StaticLine(self.panel_2)

			#Ordering GridBack and BoxSizers
			bag_sizer.Add(self.picture,pos=(0,0),span=(3,3),flag=wx.EXPAND|wx.ALIGN_LEFT|wx.TOP|wx.RIGHT|wx.BOTTOM,border=20)
			bag_sizer.Add(line_hor, pos=(3,0),span=(1,4),flag=wx.EXPAND|wx.BOTTOM,border=0)
			bag_sizer.Add(box_vert_data,pos=(0,3),span=(3,1),flag=wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND,border=25)
			bag_sizer.Add(box_hor_buttons,pos=(4,1),span=(1,3),flag=wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL,border=60)
			

			bag_sizer.AddGrowableCol(0)
			bag_sizer.AddGrowableRow(2)

			self.panel_2.SetSizer(bag_sizer)
			bag_sizer.Fit(self)

			self.SetSize(1500,800)
			self.SetSizeHints(300,500,1600,850)

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
circles=np.array([[[236, 194,  40],[248, 312,  40],[330, 244,  40], [158, 438,  40],[370, 432,  40],[242,  58,  40],[ 96, 410,  40],[406, 432,  40]]])

def main():

	global wind_app
	global flag_main_window

	if flag_main_window == 2:
		app_second = wx.App()
		wind_app_second = antibiogApp(None)
		app_second.MainLoop()


    

if __name__ == '__main__':
    main()	
