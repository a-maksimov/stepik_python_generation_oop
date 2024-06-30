class Versioned:

    def __set_name__(self, owner, name):
        self._attr = name
        self._attr_version_name = name + '_version'

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr][obj.__dict__[self._attr_version_name]]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        obj.__dict__[self._attr_version_name] = obj.__dict__.setdefault(self._attr_version_name, 0) + 1
        obj.__dict__.setdefault(self._attr, {}).update({obj.__dict__[self._attr_version_name]: value})

    def get_version(self, obj, n):
        return obj.__dict__[self._attr][n]

    def set_version(self, obj, n):
        obj.__dict__[self._attr_version_name] = n


# TEST_7:
class Student:
    age = Versioned()


student1 = Student()
student2 = Student()

student1.age = 18
student1.age = 19
student1.age = 20

student2.age = 30
student2.age = 31
student2.age = 32

print(student1.age)
print(student2.age)
Student.age.set_version(student1, 1)
Student.age.set_version(student2, 2)
print(student1.age)
print(student2.age)

# 20
# 32
# 18
# 31
