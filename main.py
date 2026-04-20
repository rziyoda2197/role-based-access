class Rol:
    def __init__(self, rol_id, rol_ismi):
        self.rol_id = rol_id
        self.rol_ismi = rol_ismi

class Foydalanuvchi:
    def __init__(self, foydalanuvchi_id, foydalanuvchi_ismi, rol):
        self.foydanuvchi_id = foydalanuvchi_id
        self.foydanuvchi_ismi = foydalanuvchi_ismi
        self.rol = rol

class RolBazasi:
    def __init__(self):
        self.rolar = {}
        self.foydanuvchilar = {}

    def qosh_rol(self, rol):
        self.rolar[rol.rol_id] = rol

    def qosh_foydalanuvchi(self, foydalanuvchi):
        if foydalanuvchi.rol.rol_id in self.rolar:
            self.foydanuvchilar[foydanuvchi.foydanuvchi_id] = foydalanuvchi
        else:
            print("Bunday rol yo'q")

    def rolni_olish(self, rol_id):
        return self.rolar.get(rol_id)

    def foydalanuvchini_olish(self, foydalanuvchi_id):
        return self.foydanuvchilar.get(foydanuvchi_id)

    def rolni_qoshish(self, foydalanuvchi_id, rol_id):
        foydalanuvchi = self.foydanuvchilar.get(foydanuvchi_id)
        if foydalanuvchi:
            foydalanuvchi.rol = self.rolar.get(rol_id)
        else:
            print("Bunday foydalanuvchi yo'q")

    def rolni_olish(self, foydalanuvchi_id):
        foydalanuvchi = self.foydanuvchilar.get(foydanuvchi_id)
        if foydalanuvchi:
            return foydalanuvchi.rol
        else:
            print("Bunday foydalanuvchi yo'q")

bazasi = RolBazasi()

rol1 = Rol(1, "Admin")
rol2 = Rol(2, "Moderator")

bazasi.qosh_rol(rol1)
bazasi.qosh_rol(rol2)

foydanuvchi1 = Foydalanuvchi(1, "Ali", rol1)
foydanuvchi2 = Foydalanuvchi(2, "Vali", rol2)

bazasi.qosh_foydalanuvchi(foydanuvchi1)
bazasi.qosh_foydalanuvchi(foydanuvchi2)

print(bazasi.rolni_olish(1).rol_ismi)  # Admin
print(bazasi.rolni_olish(2).rol_ismi)  # Moderator

bazasi.rolni_qoshish(1, 2)
print(bazasi.rolni_olish(1).rol_ismi)  # Moderator
