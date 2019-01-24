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
			
			self.panel=wx.Panel(self)
			self.panel.SetBackgroundColour(wx.BLACK)
			fonte=wx.Font(14,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)
			vert_menu_box=wx.BoxSizer(wx.VERTICAL)
			
			button_new=wx.Button(self.panel,wx.ID_ANY,label='Nuevo',size=(350,40))
			button_new.SetFont(fonte)
			button_new.SetBackgroundColour(wx.BLACK)
			button_new.SetForegroundColour(wx.WHITE)
			self.panel.Bind(wx.EVT_BUTTON,self.onButtonNewPress,button_new)
			vert_menu_box.Add(button_new,flag=wx.ALIGN_CENTER|wx.ALL|wx.EXPAND,border=10)

			button_cred=wx.Button(self.panel,wx.ID_ANY,label='Info.',size=(350,40))
			button_cred.SetFont(fonte)
			button_cred.SetBackgroundColour(wx.BLACK)
			button_cred.SetForegroundColour(wx.WHITE)
			self.panel.Bind(wx.EVT_BUTTON ,self.onButtonCredPress , button_cred)
			vert_menu_box.Add(button_cred,flag=wx.ALIGN_CENTER|wx.ALL|wx.EXPAND,border=10)

			button_close=wx.Button(self.panel,wx.ID_ANY,label='Cerrar',size=(350,40))
			button_close.SetFont(fonte)
			button_close.SetBackgroundColour(wx.BLACK)
			button_close.SetForegroundColour(wx.WHITE)
			self.panel.Bind(wx.EVT_BUTTON , self.OnCloseWindow ,button_close)
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
			# self.panel_2.SetBackgroundColour('#f9f4d1')
			# box_results.SetBackgroundColour(wx.Colour(240,240,240))
			
			#Data Display 
			m,n,s = np.shape(circles)
			text=[]
			static_texts=[]
			for x in range(n):
				text.append('Centro x: '+str(circles[0,x,0])+'	Centro y: '+str(circles[0,x,1])+'	Radio: '+str(circles[0,x,2]))
				static_texts.append(wx.StaticText(self.panel_2,label=text[x],style=wx.ALIGN_LEFT,size=(340,16)))
				static_texts[x].SetFont(fonte2)
				# static_texts[x].SetBackgroundColour(wx.Colour(240,240,240))
				box_vert_data.Add(static_texts[x], flag=wx.ALL|wx.EXPAND,border=6)


			#Picture 			
			self.picture = wx.StaticBitmap(self.panel_2,wx.ID_ANY,wx.Bitmap("picture.jpeg"))
		


			#Buttons 
			button_new_picture=wx.Button(self.panel_2,wx.ID_ANY,label='Procesar',size=(180,60))
			button_edit=wx.Button(self.panel_2,wx.ID_ANY,label='Editar',size=(180,60))
			button_save=wx.Button(self.panel_2,wx.ID_ANY,label='Guardar',size=(180,60))
			button_back=wx.Button(self.panel_2,wx.ID_ANY,label='Atras',size=(180,60))

			button_new_picture.SetFont(fonte_buttons)
			button_edit.SetFont(fonte_buttons)
			button_save.SetFont(fonte_buttons)
			button_back.SetFont(fonte_buttons)

			# button_new_picture.SetBackgroundColour('#21a831')
			# button_edit.SetBackgroundColour('#21a831')
			# button_save.SetBackgroundColour('#21a831')
			# button_back.SetBackgroundColour('#21a831')

			# button_new_picture.SetForegroundColour('#f9f4d1')
			# button_edit.SetForegroundColour('#f9f4d1')
			# button_save.SetForegroundColour('#f9f4d1')
			# button_back.SetForegroundColour('#f9f4d1')

			button_new_picture.Bind(wx.EVT_BUTTON, self.onTakeNewPicture)
			button_edit.Bind(wx.EVT_BUTTON, self.onEditPicture)
			button_save.Bind(wx.EVT_BUTTON, self.onSaveData)
			button_back.Bind(wx.EVT_BUTTON, self.onBackToMenu)

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

			info1='INFORMATION'
			info2='''Antibiogramas Detector
Version:	1.00.XX
By:	UCB La Catolica Group'''
			info3='LICENCES'
			info4='''BSD
LGPL
MIT
and so on.....'''

			self.panel_3=wx.Panel(self)
			
			bag_sizer2=wx.GridBagSizer(5, 5)
			fonte_inf_titles=wx.Font(14,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_LIGHT)
			fonte_inf=wx.Font(12,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)

			text_info1=wx.StaticText(self.panel_3,label=info1)
			text_info2=wx.StaticText(self.panel_3,label=info2)
			div_line=wx.StaticLine(self.panel_3)
			text_info3=wx.StaticText(self.panel_3,label=info3)
			text_info4=wx.StaticText(self.panel_3,label=info4)
			button_back_info=wx.Button(self.panel_3,wx.ID_ANY,label='Atras',size=(70,40))


			text_info1.SetFont(fonte_inf_titles)
			text_info2.SetFont(fonte_inf)
			text_info3.SetFont(fonte_inf_titles)
			text_info4.SetFont(fonte_inf)
			button_back_info.SetFont(fonte_inf)
			text_info1.SetForegroundColour(wx.WHITE)
			text_info2.SetForegroundColour(wx.WHITE)
			text_info3.SetForegroundColour(wx.WHITE)
			text_info4.SetForegroundColour(wx.WHITE)
			button_back_info.SetForegroundColour(wx.WHITE)
			button_back_info.SetBackgroundColour(wx.BLACK)

			bag_sizer2.Add(text_info1,pos=(0,0),span=(1,2),flag=wx.ALIGN_LEFT|wx.ALL,border=28)
			bag_sizer2.Add(text_info2,pos=(1,1),flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL,border=15)
			bag_sizer2.Add(div_line,pos=(2,0),span=(1,3),flag=wx.TOP|wx.BOTTOM|wx.EXPAND,border=3)
			bag_sizer2.Add(text_info3,pos=(3,0),span=(1,2),flag=wx.ALIGN_LEFT|wx.ALL,border=28)
			bag_sizer2.Add(text_info4,pos=(4,1),flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL,border=15)
			bag_sizer2.Add(button_back_info,pos=(5,1),span=(1,2),flag=wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT,border=28)

			bag_sizer2.AddGrowableCol(1)
			bag_sizer2.AddGrowableRow(1)
			bag_sizer2.AddGrowableRow(4)

			self.panel_3.SetBackgroundColour(wx.BLACK)
			self.panel_3.Bind(wx.EVT_BUTTON,self.onBackToMenu,button_back_info)
			self.panel_3.SetSizer(bag_sizer2)
			bag_sizer2.Fit(self)
			

			self.SetSize(420,520)#,400)
			#I need to add more functions for that works
			# self.SetScrollbar(wx.VERTICAL, 0, 400, 520)

		elif flag_main_window==4:
			print('This is the edit window............. Maybe it has to be in cv2')


		self.Bind(wx.EVT_CLOSE, self.onEventClose)
		self.SetTitle('Halo`s Diameter Detector')
		self.Show(True)


	def OnCloseWindow(self,e):
		global flag_main_window
		dial = wx.MessageDialog(None, 'Estas seguro?', 'Finalizar?',    wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		flag_main_window=9
		if ret == wx.ID_YES:
			self.Destroy()
		else:
			e.Veto()

	def onBackToMenu(self,e):
		global flag_main_window
		self.Close()
		flag_main_window=1
			
	def onButtonNewPress(self,e):
		global flag_main_window
		self.Close()
		flag_main_window = 2
	
	def onButtonCredPress(self,e):
		global flag_main_window
		self.Close()
		flag_main_window = 3

	def onEventClose(self,e):
		global flag_main_window
		flag_main_window = 9
		self.Destroy()

	def onTakeNewPicture(sefl,e):
		print('this call to function <getting centers and circles> or something named like that')

	def onEditPicture(self,e):
		global flag_main_window
		self.Close()
		flag_main_window=4

	def onSaveData(sefl,e):
		print('Here we have to put the code to save data on the cloud')


#Global sttatements
flag_main_window = 1
app = wx.App()
wind_app = antibiogApp(None)
app.MainLoop()
#Radious and centers of circles example picture 2.jpeg
circles=np.array([[[236, 194,  40],[248, 312,  40],[330, 244,  40], [158, 438,  40],[370, 432,  40],[242,  58,  40],[ 96, 410,  40],[406, 432,  40]]])

def main():

	global wind_app
	global flag_main_window
	global app

	while flag_main_window==1 or flag_main_window==2 or flag_main_window==3 or flag_main_window==4:
		app.__init__()
		wind_app=antibiogApp(None)
		app.MainLoop()


    

if __name__ == '__main__':
    main()	
