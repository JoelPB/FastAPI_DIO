from typing import Annotated, Optional

from pydantic import Field, PositiveFloat

from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchema, OutMixin


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
    categoria: Annotated[CategoriaIn, Field(description="Categoria do Atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="Centro de treinamento do Atleta")]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass


class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description="Nome do atleta",
                                         example="João", max_length=50)]
    idade: Annotated[Optional[int], Field(None, description="Idade do atleta",
                                          example=40)]
