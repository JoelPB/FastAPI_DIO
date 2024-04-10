from typing import Annotated

from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta",
                               example="João", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta",
                               example="01234567890", max_length=50)]
    idade: Annotated[int, Field(description="Idade do atleta",
                              example=40)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta",
                                example=90.0)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta",
                                         example=1.80)]
    sexo: Annotated[str, Field(description="Sexo do atleta",
                              example="M", max_length=1)]
