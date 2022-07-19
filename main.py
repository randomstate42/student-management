from tkinter import *
from views import HomeView, views_queue


if __name__ == "__main__":
    r = Tk()
    r.config(background="black")
    r.geometry("400x500")
    view = HomeView(r)
    view.show()
    r.mainloop()
    views_queue[-1].db.close()
