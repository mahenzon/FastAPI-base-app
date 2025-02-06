from crud import users
from core.models import User, db_helper
from .send_email import send_email


async def send_welcome_email(user_id: int) -> None:
    async with db_helper.session_factory() as session:
        user: User = await users.get_user(
            session=session,
            user_id=user_id,
        )

    await send_email(
        recipient=user.email,
        subject="Welcome to our site!",
        body=f"Dear {user.username},\n\nWelcome to our site!",
    )
