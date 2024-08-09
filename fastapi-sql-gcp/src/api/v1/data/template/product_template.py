from fastapi import Body

from schemas.product_schema import BaseProductSchema


CreateProductBody = Body(
    title='Product',
    description='The product json representation.',
    examples=[
        BaseProductSchema(
            name='apple',
            category='food',
            value= 37.99
        )
    ]
)