from rolepermissions.roles import AbstractUserRole


class Gerente(AbstractUserRole):
    avaliable_permissions = {
        "cadstrar_produtos": True,
        "liberar_descontos": True,
        "cadastrar_vendedor": True,
    }


class Vendedor(AbstractUserRole):
    avaliable_permissions = {
        "realizar_venda": True,
    }
