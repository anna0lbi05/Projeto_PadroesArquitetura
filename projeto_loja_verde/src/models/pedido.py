from dataclasses import dataclass
from typing import List


@dataclass
class ItemPedido:
    nome: str
    p: float
    q: int
    tipo: str


@dataclass
class Pedido:
    id: int
    cli: str
    itens: List[dict]
    tot: float
    st: str
    dt: str
    tp: str