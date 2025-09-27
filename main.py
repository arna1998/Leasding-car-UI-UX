from pl.AppRegister import *
from pl.AppRegister import App




if __name__=="__main__":
    screen=CTk()
    screen.geometry(("1200x700+100+10"))
    screen.title("Car_gallery")
    screen.iconbitmap("img/cis.ico")
    screen.configure(background="white")
    PageMe=App(screen)

    screen.mainloop()


