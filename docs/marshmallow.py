import marshmallow as mars
# from marshmallow import Schema, fields, INCLUDE, ValidationError, validate

payload_raw = {
    "run_mode": 'run',
    # "target": 'lala',
    # "select": 'a_folder',

}

class DbtInput(mars.Schema):
    run_mode = mars.fields.Str(
        validate = mars.validate.OneOf(["debug","run","test","snapshot"]),
        required = True, 
    )
    target = mars.fields.Str( 
        required=False,
    ),
    select = mars.fields.Str(
        required=False,
    )
dbt_input = DbtInput() 
payload = dbt_input.load(payload_raw)