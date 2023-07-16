from enum import Enum


def make_db_choices_from_enum(e: Enum):
    choices = [(member.name, member.value) for member in e.__members__.values()]

    return choices
