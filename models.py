import sqlite3


class DbMOdel:
    def __init__(self, dbname="classes.db"):
        self.db = sqlite3.connect(dbname)
        self.cu = self.db.cursor()

    def create_table_student(self):
        try:
            self.cu.execute(
                """create table etudiant(
            idetudiant integer ptimary key unique,
            idfiliere references filiere(idfiliere),
            nom  text,
            prenom text,
            age integer )"""
            )
        except sqlite3.OperationalError:
            pass

    def create_table_branch(self):
        try:
            self.cu.execute(
                """create table filiere(
            idfiliere integer primary key unique,
            nomfiliere text)"""
            )
        except sqlite3.OperationalError:
            pass

    def add_student(self, *args):
        self.cu.execute("""insert into etudiant values(?,?,?,?,?);""", args)
        self.db.commit()

    def update_student(self, *args):
        self.cu.execute(
            """update etudiant set idfiliere=?,nom=?,prenom=?,age=? where idetudiant=?""",
            args,
        )
        self.db.commit()

    def delete_student(self, idetudiant):
        self.cu.execute("""delete from etudiant where idetudiant=?""", idetudiant)
        self.db.commit()

    def add_branch(self, *args):
        self.cu.execute("""insert into filiere values(?,?);""", args)
        self.db.commit()

    def update_branch(self, *args):
        self.cu.execute("""update filiere set nomfiliere=? where idfiliere=?""", args)
        self.db.commit()

    def delete_branch(self, idfiliere):
        self.cu.execute("""delete from filiere where idfiliere=%d""" % idfiliere)
        self.db.commit()

    def fetch_branch_students(self, filiere):
        self.cu.execute("""select * from filiere;""")
        branches = self.cu.fetchall()
        br = [branch[0] for branch in branches if branch[1] == filiere]
        idfiliere = br[0]
        self.cu.execute("""select * from etudiant where idfiliere=%d;""" % idfiliere)
        students = self.cu.fetchall()
        self.db.commit()

        return students

    def fetch_students(self):
        self.cu.execute("""select * from etudiant;""")
        eleves = self.cu.fetchall()
        el = [eleve[0] for eleve in eleves]

        return el

    def fetch_branches(self):
        self.cu.execute("""select * from filiere;""")
        branches = self.cu.fetchall()
        br = {branch[0]: branch[1] for branch in branches}

        return br

    def close(self):
        self.db.close()
