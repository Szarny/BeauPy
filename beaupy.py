from enum import IntEnum, auto


class Color(IntEnum):
    black = 0
    red = auto()
    green = auto()
    yellow = auto()
    blue = auto()
    purple = auto()
    cyan = auto()
    white = auto()
    default = auto()


class Decoration(IntEnum):
    bold = 1
    underline = 4
    default = 9


class Beaupy:
    @classmethod
    def beaupy(cls, txt, fg=Color.default, bg=Color.default, decoration=Decoration.default):
        output = "\033["

        if fg != Color.default:
            output += f"3{fg}"
        
        if bg != Color.default:
            output += f";4{bg}"
        
        if decoration != decoration.default:
            output += f";{decoration}"
        
        output += "m"
        output += txt
        output += "\033[m"

        return output

    @classmethod
    def txt_with_header(cls, header, txt, fg=Color.default, bg=Color.default, decoration=Decoration.default):
        return cls.beaupy(f" {header} ", fg, bg, decoration) + " " + cls.beaupy(txt)