from enum import Enum


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    NON_BINARY = 3


class SupportedMarket(Enum):
    US = "us"
    RU = "ru"
