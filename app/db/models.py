from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)

    tg_id = fields.IntField(unique=True)


class Message(models.Model):
    id = fields.IntField(pk=True)
    message = fields.TextField()
    type = fields.BooleanField()
    first_parameter = fields.TextField()
    second_parameter = fields.TextField()
    third_parameter = fields.TextField()
    fourth_parameter = fields.TextField()
    allele = fields.TextField()

    def __str__(self):
        return self.message
