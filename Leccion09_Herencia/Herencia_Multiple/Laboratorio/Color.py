class Color(object):
    def __init__(self, color: str) -> None:
        self._color = color
    
    # Getters
    @property
    def color(self) -> str:
        return self._color
    
    # Setters
    @color.setter
    def color(self, color: str) -> None:
        self._color = color

