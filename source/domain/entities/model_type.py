from enum import Enum


class ModelType(str, Enum):
    production = 'production'
    staging = 'staging'
