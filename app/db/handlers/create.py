from db.models import User


async def create_user(tg_id):
    user = User(tg_id=tg_id).save()
    return user


