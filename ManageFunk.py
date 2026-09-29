from PandasDatas import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class MenuButtonFunkClass:
    def __init__(self, LabelMainBottom_Welk, LabelMainBottom_Desk, FrameMainBottom):
        #Переменные общие
        self.ChangeThemeIndex = True
        self.ActiveButton = None
        self.delWelText = True

        #Присваивание элементов к переменных
        self.LabelMainBottom_Welk = LabelMainBottom_Welk
        self.LabelMainBottom_Desk = LabelMainBottom_Desk
        self.FrameMainBottom = FrameMainBottom

        #Переменные окна "Клиенты"
        self.FrameKlientsBg = 'gray'
        self.FrameCardKlientsBg = 'gray'
        self.UpMenuXPad = 2
        self.UpMenuYPad = 4
        self.UpMenuFont = ('Times New Roman', 16, 'bold')
        self.J_Start_index = 0
        self.J_End_index = 4
        self.pil_ClientFrameImage = Image.open('Klients-Image.png').resize((64, 64))
        self.ClientFrameImage = ImageTk.PhotoImage(self.pil_ClientFrameImage)

    def FirstButtonClick(self, ArrowLabel, NameButton, ArrowRelX):
        self.ActiveButton = NameButton
        ArrowLabel.place(relx=ArrowRelX, rely=0, relheight=1)
        if self.delWelText:
            self.LabelMainBottom_Welk.destroy()
            self.LabelMainBottom_Desk.destroy()
            ArrowLabel['text'] = '▲'

    def ChangeTheme(self, root):
        if self.ChangeThemeIndex:
            root['bg'] = 'white'
            self.ChangeThemeIndex = False
        else:
            root['bg'] = 'black'
            self.ChangeThemeIndex = True

    def ScrollUP(self):
        pass

    def ScrollDOWN(self):
        pass
    
    def ScrollFrames(self, FrameList):
        ScrollBar_UpButton = Button(FrameList, text='↑', command=self.ScrollUP)
        ScrollBar_DownButton = Button(FrameList, text='↓', command=self.ScrollDOWN)
        ScrollBar_UpButton.place(relx=0.985, rely=0.43, anchor='center')
        ScrollBar_DownButton.place(relx=0.985, rely=0.53, anchor='center')

    def CreateKlien(self, FrameList) -> None:
        List_Frame = []
        ClientFrameInfoList = []
        relycalc = 0.25
        relxFrames = 0.13
        self.ScrollFrames(FrameList)
        for i in range(0,2):
            ListColorBg = ['white', 'white', 'green', 'blue', 'gray', 'gray', 'gray']
            ClientFrame = Frame(FrameList, bg=ListColorBg[i])
            ClientFrame.place(anchor='center', relx=0.488, relwidth=0.96, relheight=0.48, rely = relycalc)
            relycalc+=0.49
            List_Frame.append(ClientFrame)
        #Создание Карточки клиента
            for j in range(self.J_Start_index,self.J_End_index):
                ClientFrameInfo = Frame(ClientFrame, bg=self.FrameCardKlientsBg)
                ClientFrameInfo.place(anchor='center', rely=0.5, relx=relxFrames, relheight=0.9, relwidth=0.23)
                relxFrames+=0.245
                try:
                    ClientPhoto = Label(ClientFrameInfo, borderwidth=0, bg=self.FrameCardKlientsBg, image=self.ClientFrameImage, font=('Times New Roman', 12))
                    ClientReqFio = Label(ClientFrameInfo)
                    ClientReqAdress = Label(ClientFrameInfo)
                    ClientFio = Label(ClientFrameInfo, bg=self.FrameCardKlientsBg, text=f'ФИО:{KlientsData.iloc[j]["FIO"]}')
                    ClientDate = Label(ClientFrameInfo, bg=self.FrameCardKlientsBg, text=f'Дата Рождения:{KlientsData.iloc[j]["Date"]}')
                    ClientAdress = Label(ClientFrameInfo, bg=self.FrameCardKlientsBg, text=f"Адресс:{KlientsData.iloc[j]['Adress']}")
                    ClientPhoto.pack(pady=((16, 0)))
                    ClientFio.pack()
                    ClientDate.pack()
                    ClientAdress.pack()
                except:
                    pass
            relxFrames = 0.13
            self.J_Start_index+=4
            self.J_End_index+=4


    def ButtonKliens(self, ArrowLabel, NameButton : str):
        if self.ActiveButton == NameButton:
            return
        self.FirstButtonClick(ArrowLabel, NameButton, 0.3)
        # 1.Левый Фрейм включающий в себя все данные клиентов которые есть в таблице
        LeftFrame_KlientsData = Frame(self.FrameMainBottom, bg=self.FrameKlientsBg)

        # Верхнее Меню по клиенским данным
        UpMenuFrame = Frame(LeftFrame_KlientsData, bg=self.FrameKlientsBg)
        UpLabel_KlientsData = Label(UpMenuFrame, fg='black', bg = self.FrameKlientsBg, text='Клиенты:', font=self.UpMenuFont)
        EntrySeach_KlientsData = Entry(UpMenuFrame,)
        SeachButton_KlientsData = Button(UpMenuFrame, text='Поиск')
        RefrehButton_KlientsData = Button(UpMenuFrame, text='Обновить')
        LineLabelEnd_KlientsData = Label(UpMenuFrame, bg='black')

        # Нижний фрейм список клиентов
        DownListFrame_KlientsData =  Frame(LeftFrame_KlientsData, bg=self.FrameKlientsBg)
        DownListFrame_KlientsData.place(relx=0.5, rely=0.536,relwidth=1, relheight=0.92 ,anchor='center')
        self.CreateKlien(DownListFrame_KlientsData)


        # 2.Правый Фрейм включающий в себя ввод новых клиентов в базу данных и вывод их в таблице
        RightFrame_KlientsInput = Frame(self.FrameMainBottom, bg=self.FrameKlientsBg)

        ## Реализация
        #Левый Фрейм
        LeftFrame_KlientsData.place(relx= 0.34, rely= 0.5, relheight= 0.98, relwidth= 0.68, anchor= 'center')
        UpMenuFrame.pack(fill='x', pady =2)
        UpLabel_KlientsData.pack(side= 'left', pady=(0,4))
        RefrehButton_KlientsData.pack(side='right', padx= self.UpMenuXPad, pady=self.UpMenuYPad)
        SeachButton_KlientsData.pack(side= 'right', padx= self.UpMenuXPad, pady=self.UpMenuYPad)
        EntrySeach_KlientsData.place(relwidth= 0.24, anchor='center', relx=0.69, relheight=0.6, rely = 0.45)
        LineLabelEnd_KlientsData.place(relwidth=1, relheight= 0.1, rely=0.9)

        #Правый Фрейм
        RightFrame_KlientsInput.place(relx= 0.85, rely= 0.5, relheight= 0.98, relwidth= 0.3, anchor= 'center')

    def ButtonOrders(self, ArrowLabel, NameButton):
        if NameButton == self.ActiveButton:
            return
        self.FirstButtonClick(ArrowLabel, NameButton, 0.465)
        messagebox.showinfo('Оповещение', 'Это часть ещё не сделанна, перейдите на "Клиенты"')

    def ButtonAnaliz(self, ArrowLabel, NameButton):
        if NameButton == self.ActiveButton:
            return
        self.FirstButtonClick(ArrowLabel, NameButton, 0.63)
        messagebox.showinfo('Оповещение', 'Это часть ещё не сделанна, перейдите на "Клиенты"')

    def ButtonImpExp(self, ArrowLabel, NameButton):
        if NameButton == self.ActiveButton:
            return
        self.FirstButtonClick(ArrowLabel, NameButton, 0.822)
        messagebox.showinfo('Оповещение', 'Это часть ещё не сделанна, перейдите на "Клиенты"')


