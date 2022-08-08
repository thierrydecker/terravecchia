from luqum.parser import parser
from luqum.exceptions import ParseSyntaxError

from ..exceptions.custom_exception import CustomException

QUERY = '(title:"foo bar" AND body:"quick fox") OR title:fox'


async def query_parse(query):
    try:
        tree = parser.parse(query)
        return tree
    except ParseSyntaxError as e:
        raise CustomException(
                status_code=400,
                content=
                {
                    'error': 'query-001',
                    'message': 'Syntax error in query',
                    'detail': str(e),
                }
        )
