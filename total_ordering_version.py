from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version):
        self.version = self.pad_version(version)

    @staticmethod
    def pad_version(version):
        version = version.split('.')

        for i in range(3 - len(version)):
            version.append(0)

        return tuple([int(num) for num in version])

    def __repr__(self):
        version_string = '.'.join(map(str, self.version))
        return f"Version('{version_string}')"

    def __str__(self):
        return '.'.join(map(str, self.version))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.version == other.version
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.version < other.version
        else:
            return NotImplemented


print(Version('3.0.3') == Version('1.11.28'))
print(Version('3.0.3') < Version('1.11.28'))
print(Version('3.0.3') > Version('1.11.28'))
print(Version('3.0.3') <= Version('1.11.28'))
print(Version('3.0.3') >= Version('1.11.28'))

print()

versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))