class FieldIndexError(IndexError):

    def __str__(self):
        return (
            'The value entered is outside the boundaries '
            'of the playing field'
        )


class CellOccupiedError(Exception):

    def __str__(self):
        return 'Attempting to change an occupied cell'
