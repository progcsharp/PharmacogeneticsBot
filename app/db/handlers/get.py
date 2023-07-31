from db.models import User, Message


async def get_user(tg_id):
    user = User.get(tg_id=tg_id)
    return user


async def get_message(data):
    message = await Message.filter(type=data["type"], first_parameter=data["first_parameter"],
                              second_parameter=data["second_parameter"], third_parameter=data["third_parameter"],
                              fourth_parameter=data["fourth_parameter"], allele=data["allele"]).first()
    return message
