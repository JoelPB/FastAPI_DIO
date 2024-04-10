from typing import Annotated

from pydantic import BaseModel, Field, PositiveFloat


class Atleta(BaseModel):
    nome: Annotated[str, Field(description="Nome do atleta",
                               examples="João", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta",
                               examples="01234567890", max_length=50)]
    idade: Annotated[int, Field(description="Idade do atleta",
                              examples=40)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta",
                                examples=90.0)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta",
                                         examples=1.80)]
    sexo: Annotated[str, Field(description="Sexo do atleta",
                              examples="M", max_length=1)]
