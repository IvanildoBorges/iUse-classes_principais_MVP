from datetime import datetime
import re
from uuid import UUID, uuid4


class Usuario:
    def __init__(self, nome: str, email: str, senha: str, id: str | None = None, criado_em: datetime | None = None):
        self.__set_id(id if id is not None else str(uuid4()))
        self.nome = nome              # usa setter
        self.email = email            # usa setter
        self.senha = senha            # usa setter
        self.__set_criado_em(criado_em if criado_em is not None else datetime.utcnow())

    # ----------------------------
    # ID
    # ----------------------------

    @property
    def id(self) -> str:
        return self.__id

    # Setter privado — só o construtor usa
    def _set_id(self, valor: str):
        # valida se é um UUID válido
        try:
            UUID(valor)
        except Exception:
            raise ValueError("ID deve ser um UUID válido.")
        self.__id = valor

    # ----------------------------
    # Criado_em
    # ----------------------------

    @property
    def criado_em(self) -> datetime:
        return self.__criado_em

    def __set_criado_em(self, valor: datetime):
        if not isinstance(valor, datetime):
            raise ValueError("criado_em deve ser um datetime válido.")

        self.__criado_em = valor

    # ----------------------------
    # Nome
    # ----------------------------

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not valor or len(valor) < 2:
            raise ValueError("O nome deve conter pelo menos 2 caracteres.")
        self._nome = valor.strip()

    # ----------------------------
    # Email
    # ----------------------------

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str):
        padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(padrao_email, valor):
            raise ValueError("E-mail inválido.")
        self._email = valor.lower()

    # ----------------------------
    # Senha
    # ----------------------------

    @property
    def senha(self) -> str:
        """Por segurança, retornar a senha não é recomendado."""
        raise AttributeError("A senha não pode ser acessada diretamente.")

    @senha.setter
    def senha(self, valor: str):
        if len(valor) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")
        # ⚠️ Aqui você poderia aplicar hash (ex: bcrypt)
        self._senha = valor

    # Método seguro para checar a senha
    def verificar_senha(self, senha: str) -> bool:
        return self._senha == senha

    # ----------------------------
    # Representação
    # ----------------------------

    def __repr__(self):
        return f"Usuario(id='{self._id}', nome='{self._nome}', email='{self._email}')"
