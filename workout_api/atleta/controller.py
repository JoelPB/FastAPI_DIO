from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, status, Body, HTTPException, Query
from pydantic import UUID4
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError, NoResultFound

from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.categorias.controller import CategoriaModel
from workout_api.atleta.models import AtletaModel
from workout_api.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate, AtletaShort
from workout_api.contrib.depedencies import DatabaseDependency

router = APIRouter()


@router.post(
    "/",
    summary="Criar um novo atleta.",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut
)
async def post(
        db_session: DatabaseDependency,
        atleta_in: AtletaIn = Body(...)
):
    categoria_nome = atleta_in.categoria.nome
    centro_treinamento_nome = atleta_in.centro_treinamento.nome

    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_nome))
                 ).scalars().first()

    if not categoria:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"A categoria {categoria_nome} não foi encontada")

    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_nome))
                          ).scalars().first()

    if not centro_treinamento:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"O centro de treianmento {centro_treinamento_nome} não foi encontado")

    try:
        atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={"categoria", "centro_treinamento"}))

        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id

        db_session.add(atleta_model)
        await db_session.commit()


    except IntegrityError as e:
        # Se ocorrer uma exceção de integridade de dados, verifique se é devido ao CPF duplicado
        if "cpf" in str(e).lower():
            raise HTTPException(status_code=status.HTTP_303_SEE_OTHER,
                                detail=f"Já existe um atleta cadastrado com o CPF: {atleta_in.cpf}")

        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Ocorreu um erro ao inserir os dados no banco: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Ocorreu um erro ao inserir os dados no banco: {str(e)}")

    return atleta_out


@router.get(
    "/",
    summary="Consultar todos os Atletas.",
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaShort],
)
async def query(
        db_session: DatabaseDependency,
        nome: str = Query(None),
        cpf: str = Query(None)
) -> list[AtletaShort]:
    filters = []
    if nome:
        filters.append(AtletaModel.nome == nome)
    if cpf:
        filters.append(AtletaModel.cpf == cpf)

    try:
        atletas: list[AtletaModel] = (
            await db_session.execute(select(AtletaModel).filter(*filters))
        ).scalars().all()

        response_data = []
        for atleta in atletas:
            atleta_short = AtletaShort(
                nome=atleta.nome,
                categoria=atleta.categoria.nome,
                centro_treinamento=atleta.centro_treinamento.nome
            )
            response_data.append(atleta_short)

        return response_data

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Erro interno do servidor: {str(e)}")


@router.get(
    "/{id}",
    summary="Consulta um Atleta pelo id.",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def get(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    try:
        atleta: AtletaOut = (
            await db_session.execute(select(AtletaModel).filter_by(id=id))
        ).scalars().first()

    except NoResultFound:
        # Captura exceção quando nenhum resultado é encontrado
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Atleta não encontrado com o ID: {id}")
    except Exception as e:
        # Captura outras exceções não tratadas
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Erro interno do servidor: {str(e)}")

    return atleta


@router.patch(
    "/{id}",
    summary="Editar um Atleta pelo id.",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def update_atleta(id: UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    try:
        atleta: AtletaOut = (
            await db_session.execute(select(AtletaModel).filter_by(id=id))
        ).scalars().first()

    except NoResultFound:
        # Captura exceção quando nenhum resultado é encontrado
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Atleta não encontrado com o ID: {id}")
    except Exception as e:
        # Captura outras exceções não tratadas
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Erro interno do servidor: {str(e)}")

    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    try:
        await db_session.commit()
        await db_session.refresh(atleta)
        
    except Exception as e:
        # Se ocorrer um erro durante a atualização, lança uma exceção com uma mensagem de erro específica
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Erro ao atualizar o atleta com o ID {id}: {str(e)}")

    return atleta


@router.delete(
    "/{id}",
    summary="Deletar um Atleta pelo id.",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_atleta(id: UUID4, db_session: DatabaseDependency) -> None:
    try:
        atleta: AtletaOut = (
            await db_session.execute(select(AtletaModel).filter_by(id=id))
        ).scalars().first()

        if not atleta:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Atleta não encontrado no id: {id}")

        await db_session.delete(atleta)
        await db_session.commit()

    except Exception as e:
        # Captura qualquer exceção não tratada durante a exclusão do atleta
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Erro ao excluir o atleta com o ID {id}: {str(e)}")
