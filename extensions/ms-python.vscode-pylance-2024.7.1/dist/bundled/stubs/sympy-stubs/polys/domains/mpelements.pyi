from typing import Any, Literal

from mpmath.ctx_mp_python import PythonMPContext, _mpc, _mpf
from sympy.polys.domains.domainelement import DomainElement
from sympy.utilities import public

@public
class RealElement(_mpf, DomainElement):
    __slots__ = ...
    _mpf_ = ...
    def parent(self): ...

@public
class ComplexElement(_mpc, DomainElement):
    __slots__ = ...
    _mpc_ = ...
    def parent(self): ...

new = ...

@public
class MPContext(PythonMPContext):
    def __init__(ctx, prec=..., dps=..., tol=..., real=...) -> None: ...
    def make_tol(ctx) -> _mpf: ...
    def to_rational(ctx, s, limit=...) -> tuple[Any, Any | Literal[1]]: ...
    def almosteq(ctx, s, t, rel_eps=..., abs_eps=...) -> Literal[True]: ...