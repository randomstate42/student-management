from abc import ABC, abstractmethod
from collections import deque
from tkinter import *
import tkinter.ttk as ttk
import sqlite3

from models import DbMOdel
from callbacks import navigate, navigate_back
from config import *


views_queue = deque()


class BaseView(ABC):
    def __init__(self, root, db=DbMOdel("classes.db")):
        self.root = root
        self.db = db
        views_queue.append(self)

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def show_update(self):
        pass


class HomeView(BaseView):
    def __init__(self, root):
        super().__init__(root)
        self.db.create_table_branch()
        self.db.create_table_student()

    def show(self):
        self.frame = Frame(self.root)
        self.frame.config(width=400, height=500, background="black")
        self.frame.place(x=0, y=0)
        Label(self.frame, text="vous étes?", background="black", fg=FG, width=20).place(
            x=115, y=100
        )
        Button(
            self.frame,
            text="Admin",
            width=20,
            height=1,
            command=lambda: navigate(self.root, AdminView),
            bg=BG,
            fg=FG,
            activebackground=ABG,
            borderwidth="2",
        ).place(x=115, y=170)
        Button(
            self.frame,
            text="élève",
            width=20,
            height=1,
            command=lambda: navigate(self.root, StudentView),
            bg=BG,
            fg=FG,
            activebackground=ABG,
            borderwidth="2",
        ).place(x=115, y=210)
        Label(self.frame, text="INSEA @ 2020", bg=BG, fg=LFG).place(x=155, y=400)

    def show_update(self):
        pass


class AdminView(BaseView):
    def show(self):
        self.frame = Frame(self.root)
        self.frame.config(width=400, height=500, background="black")
        self.frame.place(x=0, y=0)
        Label(self.frame, text="surface admin", bg=BG, fg=LFG).place(x=140, y=10)
        Label(self.frame, text="Que desirez-vous faire?", bg=BG, fg=LFG).place(
            x=115, y=60
        )
        Button(
            self.frame,
            text="afficher les listes",
            command=lambda: navigate(self.root, DisplayView),
            width=20,
            height=1,
            bg=BG,
            fg=FG,
        ).place(x=115, y=350)
        Button(
            self.frame,
            text="ajouter un élève",
            command=lambda: navigate(self.root, AddStudentView),
            width=20,
            height=1,
            bg=BG,
            fg=FG,
            activebackground=ABG,
        ).place(x=115, y=110)
        Button(
            self.frame,
            text="modifier un élève",
            command=lambda: navigate(self.root, UpdateStudentView),
            width=20,
            height=1,
            bg=BG,
            fg=FG,
            activebackground=ABG,
        ).place(x=115, y=150)
        Button(
            self.frame,
            text="supprimer un élève",
            command=lambda: navigate(self.root, DeleteStudentView),
            width=20,
            height=1,
            bg=BG,
            fg=FG,
            activebackground=ABG,
        ).place(x=115, y=190)
        Button(
            self.frame,
            text="ajouter une filière",
            command=lambda: navigate(self.root, AddBranchView),
            width=20,
            height=1,
            bg=BG,
            fg=FG,
            activebackground=ABG,
        ).place(x=115, y=230)
        Button(
            self.frame,
            text="modifier une filière",
            command=lambda: navigate(self.root, UpdateBrancheView),
            width=20,
            height=1,
            bg=BG,
            fg=FG,
            activebackground=ABG,
        ).place(x=115, y=270)
        Button(
            self.frame,
            text="supprimer une filière",
            command=lambda: navigate(self.root, DeleteBranchView),
            width=20,
            height=1,
            bg=BG,
            fg=FG,
            activebackground=ABG,
        ).place(x=115, y=310)
        Button(
            self.frame,
            command=lambda: navigate_back(views_queue),
            text=NTXT,
            bg=NBG,
            fg=NFG,
            borderwidth="2",
        ).place(x=0, y=0)

    def show_update(self):
        pass


class StudentView(BaseView):
    def show(self):
        self.frame = Frame(self.root)
        self.frame.config(width=400, height=500, background="black")
        self.frame.place(x=0, y=0)
        Label(self.frame, text="surface eleve", bg=BG, fg=LFG).place(x=140, y=10)
        Label(self.frame, text="Que desirez-vous faire?", bg=BG, fg=LFG).place(
            x=115, y=60
        )
        Button(
            self.frame,
            text="s'inscrire",
            command=lambda: navigate(self.root, SignUpView),
            width=20,
            height=1,
            bg=BG,
            fg=FG,
            activebackground=ABG,
        ).place(x=115, y=110)
        Button(
            self.frame,
            text="modifier mes données",
            command=lambda: navigate(self.root, UpdatePersonalInfoView),
            width=20,
            height=1,
            bg=BG,
            fg=FG,
            activebackground=ABG,
        ).place(x=115, y=150)
        Button(
            self.frame,
            command=lambda: navigate_back(views_queue),
            text=NTXT,
            bg=NBG,
            fg=NFG,
            borderwidth="2",
        ).place(x=0, y=0)

    def show_update(self):
        pass


class AddStudentView(BaseView):
    def show(self):
        self.frame = Frame(self.root)
        self.frame.config(width=400, height=500, background="black")
        self.frame.place(x=0, y=0)
        self._textlabel = Label(
            self.frame, text="Ajout d'un élève", bg=BG, fg=LFG, borderwidth="0"
        )
        self._textlabel.place(x=130, y=20)
        Label(self.frame, text="ideleve", bg=BG, fg=FG).place(x=60, y=80)
        self._entry1 = Entry(self.frame, bg="gray", fg=FG)
        self._entry1.place(x=125, y=80)
        Label(self.frame, text="idfiliere", bg=BG, fg=FG).place(x=60, y=120)
        self._entry2 = Entry(self.frame, bg="gray", fg=FG)
        self._entry2.place(x=125, y=120)
        Label(self.frame, text="nom", bg=BG, fg=FG).place(x=60, y=160)
        self._entry3 = Entry(self.frame, bg="gray", fg=FG)
        self._entry3.place(x=125, y=160)
        Label(self.frame, text="prenom", bg=BG, fg=FG).place(x=60, y=200)
        self._entry4 = Entry(self.root, bg="gray", fg=FG)
        self._entry4.place(x=125, y=200)
        Label(self.frame, text="age", bg=BG, fg=FG).place(x=60, y=240)
        self._entry5 = Entry(self.frame, bg="gray", fg=FG)
        self._entry5.place(x=125, y=240)
        Button(
            self.frame, command=self.show_update, text="ajouter", bg=NBG, fg=FG
        ).place(x=230, y=280)
        Button(
            self.frame,
            command=lambda: navigate_back(views_queue),
            text=NTXT,
            bg=NBG,
            fg=NFG,
            borderwidth="2",
        ).place(x=0, y=0)

    def show_update(self):
        if not self._entry1.get().isdigit():
            self._textlabel.config(text="idetudiant : seulement des nombres", fg="red")
        elif not self._entry2.get().isdigit():
            self._textlabel.config(text="idfiliere : seulement des nombres", fg="red")
        elif not self._entry3.get().isalpha() or not self._entry4.get().isalpha():
            self._textlabel.config(
                text="nom et prenom: seulement des alphabets", fg="red"
            )
        elif not self._entry5.get().isdigit():
            self._textlabel.config(text="age impossible", fg="red")
        else:
            try:
                self.db.add_student(
                    int(self._entry1.get()),
                    int(self._entry2.get()),
                    self._entry3.get(),
                    self._entry4.get(),
                    int(self._entry5.get()),
                )
                navigate_back(views_queue)
            except sqlite3.IntegrityError:
                self._textlabel.config(text="identifiant existe deja", fg="red")


class UpdateStudentView(BaseView):
    def show(self):
        self.frame = Frame(self.root)
        self.frame.config(width=400, height=500, background="black")
        self.frame.place(x=0, y=0)
        self._textlabel = Label(
            self.frame, text="modification", bg=BG, fg=LFG, borderwidth="0"
        )
        self._textlabel.place(x=130, y=20)
        Label(self.frame, text="idetudiant", bg=BG, fg=FG).place(x=60, y=80)
        self._entry1 = Entry(self.frame, bg="gray", fg=FG)
        self._entry1.place(x=125, y=80)
        Label(self.frame, text="idfiliere", bg=BG, fg=FG).place(x=60, y=120)
        self._entry2 = Entry(self.frame, bg="gray", fg=FG)
        self._entry2.place(x=125, y=120)
        Label(self.frame, text="nom", bg=BG, fg=FG).place(x=60, y=160)
        self._entry3 = Entry(self.frame, bg="gray", fg=FG)
        self._entry3.place(x=125, y=160)
        Label(self.frame, text="prenom", bg=BG, fg=FG).place(x=60, y=200)
        self._entry4 = Entry(self.frame, bg="gray", fg=FG)
        self._entry4.place(x=125, y=200)
        Label(self.frame, text="age", bg=BG, fg=FG).place(x=60, y=240)
        self._entry5 = Entry(self.frame, bg="gray", fg=FG)
        self._entry5.place(x=125, y=240)
        Button(
            self.frame, command=self.show_update, text="modifier", bg=NBG, fg=NFG
        ).place(x=230, y=280)
        Button(
            self.frame,
            command=lambda: navigate_back(views_queue),
            text=NTXT,
            bg=NBG,
            fg=NFG,
            borderwidth="2",
        ).place(x=0, y=0)

    def show_update(self):
        students = self.db.fetch_students()
        if not self._entry1.get().isdigit() or int(self._entry1.get()) not in students:
            self._textlabel.config(text="cet etudiant n'existe pas", fg="red")
        elif not self._entry2.get().isdigit():
            self._textlabel.config(text="idfiliere : seulement des nombres", fg="red")
        elif not self._entry3.get().isalpha() or not self._entry4.get().isalpha():
            self._textlabel.config(
                text="nom et prenom: seulement des alphabets", fg="red"
            )
        elif not self._entry5.get().isdigit():
            self._textlabel.config(text="age impossible", fg="red")
        else:
            self.db.update_student(
                int(self._entry2.get()),
                self._entry3.get(),
                self._entry4.get(),
                int(self._entry5.get()),
                int(self._entry1.get()),
            )
            lambda: navigate_back(views_queue)()


class DeleteStudentView(BaseView):
    def show(self):
        self.frame = Frame(self.root)
        self.frame.config(width=400, height=500, background="black")
        self.frame.place(x=0, y=0)
        self._textlabel = Label(
            self.frame, text="suppression", bg=BG, fg=LFG, borderwidth="0"
        )
        self._textlabel.place(x=175, y=35)
        Label(self.frame, text="ideleve", bg=BG, fg=FG).place(x=60, y=75)
        self._entry = Entry(self.frame, bg="white", fg=NFG)
        self._entry.place(x=140, y=75)
        Button(
            self.frame, command=self.show_update, text="supprimer", bg="red", fg=NFG
        ).place(x=225, y=110)
        Button(
            self.frame,
            command=lambda: navigate_back(views_queue),
            text=NTXT,
            bg=NBG,
            fg=NFG,
            borderwidth="2",
        ).place(x=0, y=0)

    def show_update(self):
        students = self.db.fetch_students()
        if not self._entry.get().isdigit() or int(self._entry.get()) not in students:
            self._textlabel.config(text="cet identifiant n'existe pas")
        else:
            self.db.delete_student(self._entry.get())
            navigate_back(views_queue)


class AddBranchView(BaseView):
    def show(self):
        self.frame = Frame(self.root)
        self.frame.config(width=400, height=500, background="black")
        self.frame.place(x=0, y=0)
        self._textlabel = Label(
            self.frame, text="ajout d'une filière", bg=BG, fg=LFG, borderwidth="0"
        )
        self._textlabel.place(x=135, y=20)
        Label(self.frame, text="idfiliere", bg=BG, fg=FG).place(x=60, y=80)
        self._entry1 = Entry(self.frame, bg="gray", fg=FG)
        self._entry1.place(x=125, y=80)
        Label(self.frame, text="la filiere", bg=BG, fg=FG).place(x=60, y=120)
        self._entry2 = Entry(self.frame, bg="gray", fg=FG)
        self._entry2.place(x=125, y=120)
        Button(
            self.frame, command=self.show_update, text="ajouter", bg=NBG, fg=NFG
        ).place(x=230, y=160)
        Button(
            self.frame,
            command=lambda: navigate_back(views_queue),
            text="<--",
            bg=NBG,
            fg=NFG,
            borderwidth="2",
        ).place(x=0, y=0)

    def show_update(self):
        filieres = self.db.fetch_branches()
        if not self._entry1.get().isdigit():
            self._textlabel.config(text="idfiliere : seulement des nombres", fg="red")
        elif int(self._entry1.get()) in filieres.keys():
            self._textlabel.config(text="cet identifiant existe déja", fg="red")
        elif self._entry2.get() in filieres.values():
            self._textlabel.config(text="cette filiere existe déja", fg="red")
        elif self._entry2.get().isdigit():
            self._textlabel.config(text="entrer un nombre valable", fg="red")
        else:
            self.db.add_branch(int(self._entry1.get()), self._entry2.get())
            navigate_back(views_queue)


class UpdateBrancheView(BaseView):
    def show(self):
        self.frame = Frame(self.root)
        self.frame.config(width=400, height=500, background="black")
        self.frame.place(x=0, y=0)
        self._textlabel = Label(
            self.frame, text="modification de filière", bg=BG, fg=LFG, borderwidth="0"
        )
        self._textlabel.place(x=135, y=20)
        Label(self.frame, text="idfiliere", bg=BG, fg=FG).place(x=60, y=80)
        self._entry1 = Entry(self.frame, bg="gray", fg=FG)
        self._entry1.place(x=125, y=80)
        Label(self.frame, text="la filiere", bg=BG, fg=FG).place(x=60, y=120)
        self.entry2 = Entry(self.frame, bg="gray", fg=FG)
        self.entry2.place(x=125, y=120)
        Button(
            self.frame, command=self.show_update, text="modifier", bg=NBG, fg=NFG
        ).place(x=230, y=150)
        Button(
            self.frame,
            command=lambda: navigate_back(views_queue),
            text=NTXT,
            bg=NBG,
            fg=NFG,
            borderwidth="2",
        ).place(x=0, y=0)

    def show_update(self):
        filieres = self.db.fetch_branches().keys()
        if not self._entry1.get().isdigit() or int(self._entry1.get()) not in filieres:
            self._textlabel.config(text="entrer un identifiant valable", fg="red")
        elif self.entry2.get().isdigit():
            self._textlabel.config(text="le nom n'est pas valable", fg="red")
        else:
            self.db.update_branch(self.entry2.get(), int(self._entry1.get()))
            navigate_back(views_queue)


class DeleteBranchView(BaseView):
    def show(self):
        self.frame = Frame(self.root)
        self.frame.config(width=400, height=500, background="black")
        self.frame.place(x=0, y=0)
        self.frame.place(x=0, y=0)
        self._textlabel = Label(
            self.frame, text="suppression de filière", bg=BG, fg=LFG, borderwidth="0"
        )
        self._textlabel.place(x=130, y=20)
        Label(self.frame, text="idfiliere", bg=BG, fg=FG).place(x=60, y=80)
        self._entry = Entry(self.frame, bg="white", fg=NFG)
        self._entry.place(x=125, y=80)
        Button(
            self.frame, command=self.show_update, text="supprimer", bg="red", fg=NFG
        ).place(x=210, y=110)
        Button(
            self.frame,
            command=lambda: navigate_back(views_queue),
            text="<--",
            bg=NBG,
            fg=NFG,
            borderwidth="2",
        ).place(x=0, y=0)

    def show_update(self):
        filieres = self.db.fetch_branches().keys()
        try:
            if (
                not self._entry.get().isdigit()
                or int(self._entry.get()) not in filieres
            ):
                self._textlabel.config(text="entrer un identifiant valable", fg="red")
            else:
                self.db.delete_branch(int(self._entry.get()))
                navigate_back(views_queue)
        except:
            self.frame.config(text="entrer un identifiant valable", fg="red")


class SignUpView(BaseView):
    def show(self):
        self.frame = Frame(self.root)
        self.frame.config(width=400, height=500, background="black")
        self.frame.place(x=0, y=0)
        self._textlabel = Label(
            self.frame, text="inscription", bg=BG, fg=LFG, borderwidth="0"
        )
        self._textlabel.place(x=170, y=20)
        Label(self.frame, text="ideleve", bg=BG, fg=FG).place(x=60, y=80)
        self._entry1 = Entry(self.frame, bg="gray", fg=FG)
        self._entry1.place(x=125, y=80)
        Label(self.frame, text="filiere", bg=BG, fg=FG).place(x=60, y=120)
        self._entry2 = Entry(self.frame, bg="gray", fg=FG)
        self._entry2.place(x=125, y=120)
        Label(self.frame, text="nom", bg=BG, fg=FG).place(x=60, y=160)
        self._entry3 = Entry(self.frame, bg="gray", fg=FG)
        self._entry3.place(x=125, y=160)
        Label(self.frame, text="prenom", bg=BG, fg=FG).place(x=60, y=200)
        self._entry4 = Entry(self.root, bg="gray", fg=FG)
        self._entry4.place(x=125, y=200)
        Label(self.frame, text="age", bg=BG, fg=FG).place(x=60, y=240)
        self._entry5 = Entry(self.frame, bg="gray", fg=FG)
        self._entry5.place(x=125, y=240)
        Button(
            self.frame, command=self.show_update, text="ajouter", bg=NBG, fg=NFG
        ).place(x=230, y=270)
        Button(
            self.frame,
            text=NTXT,
            command=lambda: navigate_back(views_queue),
            bg=NBG,
            fg=NFG,
            borderwidth="2",
        ).place(x=0, y=0)

    def show_update(self):
        students = self.db.fetch_students()
        filieres = self.db.fetch_branches()
        if not self._entry1.get().isdigit() or int(self._entry1.get()) in students:
            self._textlabel.config(text="entrer un identifiant valable", fg="red")
        elif self._entry2.get() not in filieres.values():
            self._textlabel.config(text="cette filiere n'existe pas", fg="red")
        elif not self._entry3.get().isalpha() or not self._entry4.get().isalpha():
            self._textlabel.config(
                text="nom et prenom: seulement des alphabets", fg="red"
            )
        elif not self._entry5.get().isdigit():
            self._textlabel.config(text="age impossible", fg="red")
        else:
            l = [f for f in filieres if filieres[f] == self._entry2.get()]
            idfiliere = l[0]
            self.db.add_student(
                int(self._entry1.get()),
                idfiliere,
                self._entry3.get(),
                self._entry4.get(),
                int(self._entry5.get()),
            )
            navigate_back(views_queue)


class UpdatePersonalInfoView(BaseView):
    def show(self):
        self.frame = Frame(self.root)
        self.frame.config(width=400, height=500, background="black")
        self.frame.place(x=0, y=0)
        self._textlabele = Label(
            self.frame, text="modification", bg=BG, fg=LFG, borderwidth="0"
        )
        self._textlabele.place(x=160, y=20)
        Label(self.frame, text="ideleve", bg=BG, fg=FG).place(x=60, y=80)
        self._entry1 = Entry(self.frame, bg="gray", fg=FG)
        self._entry1.place(x=125, y=80)
        Label(self.frame, text="nom", bg=BG, fg=FG).place(x=60, y=120)
        self._entry2 = Entry(self.frame, bg="gray", fg=FG)
        self._entry2.place(x=125, y=120)
        Label(self.frame, text="prenom", bg=BG, fg=FG).place(x=60, y=160)
        self._entry3 = Entry(self.frame, bg="gray", fg=FG)
        self._entry3.place(x=125, y=160)
        Label(self.frame, text="filiere", bg=BG, fg=FG).place(x=60, y=200)
        self._entry4 = Entry(self.frame, bg="gray", fg=FG)
        self._entry4.place(x=125, y=200)
        Label(self.frame, text="age", bg=BG, fg=FG).place(x=60, y=240)
        self._entry5 = Entry(self.frame, bg="gray", fg=FG)
        self._entry5.place(x=125, y=240)
        Button(
            self.frame, command=self.show_update, text="modifier", bg=NBG, fg=NFG
        ).place(x=230, y=270)
        Button(
            self.frame,
            text=NTXT,
            command=lambda: navigate_back(views_queue),
            bg=NBG,
            fg=NFG,
            borderwidth="2",
        ).place(x=0, y=0)

    def show_update(self):
        students = self.db.fetch_students()
        filieres = self.db.fetch_branches()
        if not self._entry1.get().isdigit() or int(self._entry1.get()) not in students:
            self._textlabele.config(text="cet identifiant n'existe pas", fg="red")
        elif not self._entry2.get().isalpha() or not self._entry3.get().isalpha():
            self._textlabele.config(
                text="nom et prenom: seulement des alphabets", fg="red"
            )
        elif not self._entry5.get().isdigit():
            self._textlabele.config(text="age impossible", fg="red")
        elif self._entry4.get() not in filieres.values():
            self._textlabele.config(text="cette filiere n'existe pas", fg="red")
        elif self._entry4.get().isdigit():
            self._textlabele.config(text="entrer une filiere valable", fg="red")
        else:
            l = [f for f in filieres if filieres[f] == self._entry4.get()]
            idfiliere = l[0]
            self.db.update_student(
                idfiliere,
                self._entry3.get(),
                self._entry4.get(),
                int(self._entry5.get()),
                int(self._entry1.get()),
            )
            navigate_back(views_queue)


class DisplayView(BaseView):
    def show(self):
        self.frame = Frame(self.root)
        self.frame.config(width=400, height=500, background="black")
        self.frame.place(x=0, y=0)
        self._textlabel = Label(
            self.frame, text="afficher la liste de la filiere:", bg=BG, fg=LFG
        )
        self._textlabel.place(x=110, y=100)
        filieres = list(self.db.fetch_branches().values())
        self.c = ttk.Combobox(self.frame, values=filieres)
        self.c.place(x=60, y=190)
        Button(
            self.frame, text="afficher", command=self.show_update, bg=NBG, fg=NFG
        ).place(x=250, y=190)
        Button(
            self.frame,
            command=lambda: navigate_back(views_queue),
            text=NTXT,
            bg=NBG,
            fg=NFG,
            borderwidth="2",
        ).place(x=0, y=0)

    def show_update(self):
        try:
            r = Tk()
            r.geometry("600x900")
            r.config(bg="white")
            students = self.db.fetch_branch_students(self.c.get())
            s = "liste de la filiere : {}".format(self.c.get())
            Label(r, text=s, bg="white").place(x=200, y=2)
            s1 = "idetudiant              nom             prenom              filiere              age"
            Label(r, text=s1, bg="white").place(x=0, y=50)
            for i, e in enumerate(students):
                s = "{}                        {}                      {}                       {}                   {}".format(
                    e[0], e[2], e[3], self.c.get(), e[4]
                )
                Label(r, text=s, bg="white").place(x=0, y=(100 + i * 50))
            r.mainloop()
        except:
            self._textlabel.config(text="choisissez une liste SVP")
