class H:
    ...


class D(H):
    ...


class E(H):
    ...


class F(H):
    ...


class G(H):
    ...


class B(D, E):
    ...


class C(F, G):
    ...


class A(B, C):
    ...

