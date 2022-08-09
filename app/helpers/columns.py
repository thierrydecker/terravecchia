from app.exceptions.custom_exception import CustomException


def sanitise(columns: list, valid_columns: dict) -> set:
    #
    # Create a list of multiple columns query parameters
    #
    columns = ','.join(columns).split(',')
    #
    # Take all columns
    #
    if 'all' in columns:
        columns = ['all']
    else:
        #
        # Remove single and double quotes from each element
        #
        for pos, column in enumerate(columns):
            columns[pos] = columns[pos].strip("'").strip('"')
        #
        # Validate columns names
        #
        for column in columns:
            if column not in valid_columns:
                raise CustomException(
                    status_code=422,
                    content={
                        'error'  : 'columns-001',
                        'message': 'Invalid column name',
                        'detail' : f'{column} is not valid',
                    }
                )
    return set(columns)
