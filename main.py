def __cursorToListOfProduto(self, cursor):
    row = cursor.fetchone()
    result = []
    while row is not None:
        result.push(self.__rowToProduto(row))
        row = cursor.fetchone()
    return result
