from itertools import batched


class Page:
    def __init__(self, page_data):
        self._page_data = page_data

    @property
    def page_data(self):
        return list(self._page_data)


class Pagination:
    def __init__(self, elements, page_size):
        self._pages = [Page(data) for data in batched(elements, page_size)]
        self._current_page = 1

    @property
    def total_pages(self):
        return len(self._pages)

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, page_num):
        if page_num > self.total_pages:
            self._current_page = self.total_pages
        elif page_num < 1:
            self._current_page = 1
        else:
            self._current_page = page_num

    def get_visible_items(self):
        return self._pages[self._current_page - 1].page_data

    def prev_page(self):
        self.current_page -= 1
        return self

    def next_page(self):
        self.current_page += 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, page_number):
        self.current_page = page_number
        return self


# TEST_1:
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.next_page()
print(pagination.get_visible_items())    # ['e', 'f', 'g', 'h']

pagination.last_page()
print(pagination.get_visible_items())    # ['y', 'z']

pagination.first_page()
pagination.next_page().next_page()
print(pagination.get_visible_items())    # ['i', 'j', 'k', 'l']

print(pagination.total_pages)            # 7
print(pagination.current_page)           # 3

pagination.first_page()
pagination.prev_page()
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.last_page()
pagination.next_page()
print(pagination.get_visible_items())    # ['y', 'z']

pagination.go_to_page(-100)
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.go_to_page(100)
print(pagination.get_visible_items())    # ['y', 'z']
