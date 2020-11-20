class Color(object):
    def __init__(self):
        self.PURPLE = '\033[1;35;48m'
        self.CYAN = '\033[1;36;48m'
        self.BOLD = '\033[1;37;48m'
        self.BLUE = '\033[1;34;48m'
        self.GREEN = '\033[1;32;48m'
        self.YELLOW = '\033[1;33;48m'
        self.RED = '\033[1;31;48m'
        self.BLACK = '\033[1;30;48m'
        self.UNDERLINE = '\033[4;37;48m'
        self.END = '\033[1;37;0m'


    def red(self, string):
        return f"{self.RED}{string}{self.END}"

    def green(self, string):
        return f"{self.GREEN}{string}{self.END}"
