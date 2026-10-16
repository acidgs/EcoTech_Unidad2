
import hashlib
import hmac
import os


class Usuario:

    def __init__(self, idUsuario, email, passwordHash, rol):
        self.__idUsuario = idUsuario
        self.__email = email
        self.__rol = rol

        # Crear un hash seguro a partir de la contraseña recibida
        self.__salt = os.urandom(16)
        self.__passwordHash = hashlib.pbkdf2_hmac(
            "sha256",
            passwordHash.encode("utf-8"),
            self.__salt,
            200000
        )

    def autenticar(self, passwordHash):
        hashIngresado = hashlib.pbkdf2_hmac(
            "sha256",
            passwordHash.encode("utf-8"),
            self.__salt,
            200000
        )

        return hmac.compare_digest(
            self.__passwordHash,
            hashIngresado
        )

    def verificarAutorizacion(self, rol):
        if self.__rol == rol:
            return True
        else:
            return False
