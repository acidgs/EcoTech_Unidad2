import hashlib
import hmac
import os


class Usuario:

    def __init__(self, id_usuario=None, email=None, password_hash=None, rol=None, idUsuario=None, passwordHash=None):
        self.__id_usuario = id_usuario if id_usuario is not None else idUsuario
        self.__email = email
        self.__rol = rol

        # Aceptar tanto password_hash como passwordHash
        password_origen = password_hash if password_hash is not None else passwordHash

        # Crear un hash seguro a partir de la contraseña recibida
        self.__salt = os.urandom(16)
        if password_origen is not None:
            raw_password = (
                password_origen.encode("utf-8")
                if isinstance(password_origen, str)
                else password_origen
            )
            self.__password_hash = hashlib.pbkdf2_hmac(
                "sha256",
                raw_password,
                self.__salt,
                200000
            )
        else:
            self.__password_hash = None

    # Propiedades (getters) para acceder a los atributos protegidos de manera limpia
    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def idUsuario(self):
        return self.__id_usuario

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):
        if isinstance(nuevo_email, str) and "@" in nuevo_email:
            self.__email = nuevo_email
        else:
            raise ValueError("El email debe ser válido.")

    @property
    def rol(self):
        return self.__rol

    @rol.setter
    def rol(self, nuevo_rol):
        self.__rol = nuevo_rol

    @property
    def password_hash(self):
        return self.__password_hash

    @property
    def passwordHash(self):
        return self.__password_hash

    @property
    def salt(self):
        return self.__salt

    def autenticar(self, password_ingresada):
        if not isinstance(password_ingresada, str) or self.__password_hash is None:
            return False

        hash_ingresado = hashlib.pbkdf2_hmac(
            "sha256",
            password_ingresada.encode("utf-8"),
            self.__salt,
            200000
        )

        return hmac.compare_digest(
            self.__password_hash,
            hash_ingresado
        )

    def verificar_autorizacion(self, rol):
        if self.__rol == rol:
            return True
        if isinstance(self.__rol, str) and isinstance(rol, str):
            return self.__rol.lower() == rol.lower()
        return False

    def verificarAutorizacion(self, rol):
        return self.verificar_autorizacion(rol)