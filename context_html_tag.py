class HtmlTag:
    level = -1
    indent = '  '

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline
        if self.inline:
            self.end = ''
        else:
            self.end = '\n'

    def __enter__(self):
        self.__class__.level += 1
        print(f'{self.__class__.indent * self.__class__.level}<{self.tag}>', end=self.end)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{self.__class__.indent * self.__class__.level * (not self.inline)}</{self.tag}>')
        self.__class__.level -= 1
        return True

    def print(self, string):
        print(f'{self.__class__.indent * self.__class__.level * (not self.inline)}{self.indent * (not self.inline)}{string}', end=self.end)


with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

print()

with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Здесь есть что-то интересное')
    with HtmlTag('a', True) as section:
        section.print('https://stepik.org/media/attachments/course/98974/watch_me.mp4')

