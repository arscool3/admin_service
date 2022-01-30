from django.core.exceptions import ValidationError


def validate_id(value, id_type: str):
    number = value % 100
    if id_type == 'client' and number != 1:
        raise ValidationError(f'{value} не действительный идентификатор клиента')
    if id_type == 'legal_person' and number != 2:
        raise ValidationError(f'{value} не действительный идентификатор юридического лица')
    if id_type == 'department' and number != 3:
        raise ValidationError(f'{value} не действительный идентификатор департамента')


def validate_client_id(value):
    validate_id(value, 'client')


def validate_legal_person_id(value):
    validate_id(value, 'legal_person')


def validate_department_id(value):
    validate_id(value, 'department')


def validate_inn(value):
    if len(value) != 12:
        raise ValidationError(f'{value} не действительный ИНН')


def validate_kpp(value):
    if len(value) != 9:
        raise ValidationError(f'{value} не действительный КПП')


def validate_level(value):
    if value > 7:
        raise ValidationError('Нельзя создавать департаменты с уровнем больше 7')
