def as_int_category(dataframe, attribute):
    # XXX: tried to do something generic but it depends on the order of input values
    #  input values maybe partial, it's not reliable
    categories = {
        'Sex': { 'male': 0, 'female': 1 },
        'Embarked': { 'S': 0, 'Q': 1, 'C': 2}
    }

    # NOTE: dataframe fill nan with -1
    if attribute not in categories:
        raise ValueError(f"Attribute '{attribute}' is not defined yet")

    return dataframe[attribute].map(categories[attribute]).astype(int)
