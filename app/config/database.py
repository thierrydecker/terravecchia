sql_dialect = 'postgresql'
sql_user = 'fastapi'
sql_password = 'fastapi'
sql_host = 'localhost'
sql_db_name = 'fastapi'

sql_db_url = f"{sql_dialect}" \
             f"://" \
             f"{sql_user}" \
             f":{sql_password}" \
             f"@" \
             f"{sql_host}" \
             f"/" \
             f"{sql_db_name}"
