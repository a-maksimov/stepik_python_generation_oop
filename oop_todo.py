class Todo:
    def __init__(self):
        self.priorities = {}
        self.things = []

    def add(self, *task):
        self.things.append(task)
        self.priorities.setdefault(task[1], []).append(task[0])

    def get_by_priority(self, priority):
        return self.priorities.get(priority, [])

    def get_low_priority(self):
        return self.priorities.get(min(self.priorities.keys(), default=1), [])

    def get_high_priority(self):
        return self.priorities.get(max(self.priorities.keys(), default=1), [])


todo = Todo()

todo.add('Проснуться', 3)
todo.add('Помыться', 2)
todo.add('Поесть', 2)

print(todo.get_by_priority(2))

todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))

todo = Todo()

print(todo.things)
print(todo.get_by_priority(1))
print(todo.get_low_priority())
print(todo.get_high_priority())