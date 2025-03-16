from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Request, Depends

from core.models import db_helper
from crud import users as users_crud
from utils.templates import templates


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", name="users:list")
async def users_list(
    request: Request,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    users = await users_crud.get_all_users(session=session)

    return templates.TemplateResponse(
        request=request,
        name="users/list.html",
        context={"users": users},
    )
