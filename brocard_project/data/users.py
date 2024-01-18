import dataclasses


@dataclasses.dataclass
class User:
    name: str
    email: str
    password: str


@dataclasses.dataclass
class NewUser:
    name: str
    email: str
    password: str
    confirm_password: str
