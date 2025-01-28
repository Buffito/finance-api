from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=6))

    class Meta:
        ordered = True

class TransactionTypeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)

    class Meta:
        ordered = True

class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    transaction_type = fields.Nested(TransactionTypeSchema, required=True)
    amount = fields.Float(required=True)
    at_date = fields.DateTime()

    class Meta:
        ordered = True