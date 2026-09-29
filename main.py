from tkinter import *
from PIL import Image, ImageTk
from ManageFunk import MenuButtonFunkClass

# Перемменые Свойств TK:
rootBG = 'black'
# Переменные для всех FrameTopMenu
FrameTopMenuBg = 'white'
# Переменные FrameCenter
FrameCenterBackground = 'white'
FrameCenterFG = 'black'
# Переменные кнопок
ButtonCenterMenu_Image_size = (24, 24)
ButtonCenterMenuBg = FrameCenterBackground
ButtonCenterMenuPadX = (28,0)
# Переменные поднижнего меню выбора
FrameCenterMenuBottomArrow_BG = 'white' # #bbbbbb
FrameCenterMenuBottomArrow_Label_Text = ''
FrameCenterMenuBottomArrow_Label_RelX = 0.3
# Переменные нижнего меню
FrameMainBottomBG = 'White'
FrameMainBottomFG = 'Black'
LabelMainBottomFontWelk = ('Times New Romans',36, 'italic')
LabelMainBottomFont =('Times New Romans',18, 'italic')


# Основа приложения
root = Tk()
root.resizable(width=False, height=False)
root.geometry("1000x600")
root.iconbitmap('Images/icon.ico')
root.title('Менеджемент CompStore')
root.config(background=rootBG)

# 1. Клаасс FrameTopMenu и его дочерние классы
# FrameTopMenu Верхняя менюшка взаимодействия с программой
FrameTopMenu = Frame(root)
FrameTopMenu.configure(background=FrameTopMenuBg)
## Реализация
FrameTopMenu.place(relwidth=1, relheight=0.12, x=0, y=0)

# Лого в меню
pil_logo = Image.open("Images/logo.jpg").resize((64, 64))
Logo = ImageTk.PhotoImage(pil_logo)
LogoLabel = Label(FrameTopMenu, image=Logo, borderwidth=0)
## Реализация
LogoLabel.place(relx= 0.08, rely= 0.6, anchor="center")

# Меню выбора окон для работы менеджера
FrameCenterMenu = Frame(FrameTopMenu)
FrameCenterMenu.configure(background=FrameCenterBackground)
## Реализация
FrameCenterMenu.place(relheight= 1, relwidth= 0.80, relx= 0.18, rely= 0)

# Верхний Frame меню
FrameCenterMenuTop = Frame(FrameCenterMenu, background=FrameCenterBackground)
LabelCenterMenuTop_Text = Label(FrameCenterMenuTop, text = 'Меню настольного приложения для менеджера интернет-магазина:' ,font=('Times New Roman', 12), fg=FrameCenterFG, bg=FrameCenterBackground, pady=0, padx=0)
## Реализация
FrameCenterMenuTop.pack(fill='both', expand=0, side='top')
LabelCenterMenuTop_Text.pack()

# Нижний Frame меню
FrameCenterMenuBottom = Frame(FrameCenterMenu, bg = FrameCenterBackground)
## Кнопки Меню
# Кнопка Клиенты
pil_Klients = Image.open('Images/CenterMenuPicture/Klients-Image.png').resize(ButtonCenterMenu_Image_size)
Klients_Image = ImageTk.PhotoImage(pil_Klients)
ButtonCenterMenu_Klients = Button(FrameCenterMenuBottom,text = 'Клиенты', bg=ButtonCenterMenuBg, borderwidth=0, image=Klients_Image, compound='top', command=lambda: MenuButtonFunk.ButtonKliens(FrameCenterMenuBottomArrow_Label,'Klients'))
# Кнопка Заказы
pil_Orders = Image.open('Images/CenterMenuPicture/Orders-Image.png').resize(ButtonCenterMenu_Image_size)
Orders_Image = ImageTk.PhotoImage(pil_Orders)
ButtonCenterMenu_Orders = Button(FrameCenterMenuBottom,text = 'Заказы', bg=ButtonCenterMenuBg, borderwidth=0, image=Orders_Image, compound='top', command=lambda: MenuButtonFunk.ButtonOrders(FrameCenterMenuBottomArrow_Label,'Orders'))
# Кнопка Анализ
pil_Anasiz = Image.open('Images/CenterMenuPicture/Analiz-Image.png').resize(ButtonCenterMenu_Image_size)
Anasiz_Image = ImageTk.PhotoImage(pil_Anasiz)
ButtonCenterMenu_GroupAnasiz = Button(FrameCenterMenuBottom,text = 'Анализ', bg=ButtonCenterMenuBg, borderwidth=0, image = Anasiz_Image, compound='top', command=lambda: MenuButtonFunk.ButtonAnaliz(FrameCenterMenuBottomArrow_Label,'Anasiz'))
# Кнопка Импорт/Экспорт
pil_ImpExp = Image.open('Images/CenterMenuPicture/ImpExp-Image.png').resize(ButtonCenterMenu_Image_size)
ImpExp_Image = ImageTk.PhotoImage(pil_ImpExp)
ButtonCenterMenu_ImpExp = Button(FrameCenterMenuBottom,text = 'Импорт/Экспорт', bg=ButtonCenterMenuBg, borderwidth=0, image = ImpExp_Image, compound='top', command=lambda: MenuButtonFunk.ButtonImpExp(FrameCenterMenuBottomArrow_Label,'ImpExp'))
# Кнопка смена темы
pil_ThemeICON = Image.open('Images/CenterMenuPicture/LightTheme.png').resize(ButtonCenterMenu_Image_size)
ThemeICON = ImageTk.PhotoImage(pil_ThemeICON)
ButtonCenterMenu_ChangeTheme = Button(FrameCenterMenuBottom, image=ThemeICON, borderwidth=0, bg=ButtonCenterMenuBg, command =lambda: MenuButtonFunk.ChangeTheme(root))

### Реализация
FrameCenterMenuBottom.pack(fill='both', expand=1, padx=(ButtonCenterMenuPadX))
ButtonCenterMenu_Klients.pack(fill='both', expand=1,side='left', padx=(ButtonCenterMenuPadX))
ButtonCenterMenu_Orders.pack(fill='both', expand=1,side='left', padx=(ButtonCenterMenuPadX))
ButtonCenterMenu_GroupAnasiz.pack(fill='both', expand=1,side='left', padx=(ButtonCenterMenuPadX))
ButtonCenterMenu_ImpExp.pack(fill='both', expand=1,side='left', padx=(ButtonCenterMenuPadX))
ButtonCenterMenu_ChangeTheme.pack(fill='both', expand=0,side='left', padx=(ButtonCenterMenuPadX))

# Дочерний клаасс Root : Поднижнее меню выбора
FrameCenterMenuBottomArrow = Frame(root, bg = FrameCenterMenuBottomArrow_BG)
FrameCenterMenuBottomArrow_Label = Label(FrameCenterMenuBottomArrow,text=FrameCenterMenuBottomArrow_Label_Text, font=('Times New Romans',8), bg = FrameCenterMenuBottomArrow_BG)
## Реализация
FrameCenterMenuBottomArrow.place(relwidth=1, relheight=0.02, relx= 0, rely= 0.11)
FrameCenterMenuBottomArrow_Label.place(relx= FrameCenterMenuBottomArrow_Label_RelX, rely= 0, relheight= 1)

# 2. Нижний экран вкладок для управления менеджемента
# Главный фрейм взаимодействия
FrameMainBottom = Frame(root, bg = FrameMainBottomBG, padx= 8)
# Начальный экран приветсвия
LabelMainBottom_Welk = Label(FrameMainBottom, text='Добро пожаловать', bg=FrameMainBottomBG, fg=FrameMainBottomFG, font=LabelMainBottomFontWelk)
LabelMainBottom_Desk = Label(FrameMainBottom,text = 'Это программа для редактирования и работы с менеджером\n интернет магазина, здесь можно работать с заказами, клиентами, \nэкспортировать таблицы и импортировать таблицу, для начала работы \nвыберете любой из выше перечисленных выше оконок', bg=FrameMainBottomBG, fg=FrameMainBottomFG, font=LabelMainBottomFont)
## Реализация
FrameMainBottom.place(relwidth=0.99, relheight= 0.845, relx= 0.5, rely= 0.56, anchor= 'center')
LabelMainBottom_Welk.pack(pady=(120,20))
LabelMainBottom_Desk.pack()

# Запуск приложения
MenuButtonFunk = MenuButtonFunkClass(LabelMainBottom_Welk, LabelMainBottom_Desk, FrameMainBottom)
root.mainloop()