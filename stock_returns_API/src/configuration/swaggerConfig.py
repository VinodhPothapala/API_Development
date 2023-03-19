from flasgger import LazyString
from flask import request


# Provides Configurations for Swagger UI setup
class SwaggerConfig:
    swagger_template = dict(
        info={
            'title': LazyString(lambda: 'University of Virginia'),
            'description': LazyString(lambda: '<h3>This Page shows the stocks data using IEX Cloud API.</h3>'
                                              '<h5> By Vinodh Pothapala </h5>'),
        },
        host=LazyString(lambda: request.host)
    )
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'stock_data',
                "route": '/stock_data.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/stocksdata/"
    }
