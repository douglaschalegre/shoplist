'''Module for database object utilities'''

from domain import schemas, models


def replace_values(model: models.GenericBase, schema: schemas.GenericSchema) -> models.GenericBase:
    '''Replace values of a model with values from a schema, util for updating database with edit schemas'''
    model_copy = model
    for key, value in schema.model_dump().items():
            setattr(model_copy, key, value)
    return model_copy