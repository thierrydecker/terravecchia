import sqlparse

colum_name = []


def tree_recursion(token_List):
    for token in token_List:
        token_type = token._get_repr_name()
        token_value = token._get_repr_value()
        print('Type:', token_type, ', Value:', token_value)
        if token.is_group:
            tree_recursion(token)


def get_where_fields_names(token_list):
    for token in token_list.tokens:
        try:
            name = token.get_name()
            if isinstance(token, sqlparse.sql.Comparison):
                print('Comparison on:', token.left)
            else:
                get_where_fields_names(token)
        except Exception as e:
            pass


def main():
    sql = '(id > 10 and id < 20) or last_name LIKE "DE%" or uuid not in [1,2,3]'
    token_list = sqlparse.parse(sql)[0]
    get_where_fields_names(token_list)
    # tree_recursion(token_list)
    token_list._pprint_tree()



if __name__ == '__main__':
    main()
