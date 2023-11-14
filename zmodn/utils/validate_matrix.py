def validate_matrix(matrix):
    if not isinstance(matrix, list) and not isinstance(matrix, int):
        return False

    row_length = None
    if isinstance(matrix, int):
        return [matrix]

    for row in matrix:
        if isinstance(row, int):
            if row_length is None:
                row_length = 1
            elif row_length != 1:
                return False
        elif isinstance(row, list):
            if row_length is None:
                row_length = len(row)
            elif row_length != len(row):
                return False

            for element in row:
                if not isinstance(element, int):
                    return False
        else:
            return False

    return matrix
