import sqlite3
import json

from src.models.pedido import Pedido


class PedidoRepository:
    def __init__(self, db_path='loja.db'):
        self.db = sqlite3.connect(db_path)
        self.c = self.db.cursor()

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS ped (
                id INTEGER PRIMARY KEY,
                cli TEXT,
                itens TEXT,
                tot REAL,
                st TEXT,
                dt TEXT,
                tp TEXT
            )
        ''')

        self.db.commit()

    def salvar(self, cli, itens, tot, st, dt, tp):
        itens_str = json.dumps(itens)

        self.c.execute(
            """
            INSERT INTO ped (cli, itens, tot, st, dt, tp)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (cli, itens_str, tot, st, dt, tp)
        )

        self.db.commit()

        return self.c.lastrowid

    def buscar_por_id(self, pedido_id):
        self.c.execute(
            "SELECT * FROM ped WHERE id = ?",
            (pedido_id,)
        )

        r = self.c.fetchone()

        if not r:
            return None

        return Pedido(
            id=r[0],
            cli=r[1],
            itens=json.loads(r[2]),
            tot=r[3],
            st=r[4],
            dt=r[5],
            tp=r[6]
        )

    def atualizar_status(self, pedido_id, status):
        self.c.execute(
            "UPDATE ped SET st = ? WHERE id = ?",
            (status, pedido_id)
        )

        self.db.commit()

    def listar_todos(self):
        self.c.execute("SELECT * FROM ped")

        resultados = self.c.fetchall()

        pedidos = []

        for r in resultados:
            pedidos.append(
                Pedido(
                    id=r[0],
                    cli=r[1],
                    itens=json.loads(r[2]),
                    tot=r[3],
                    st=r[4],
                    dt=r[5],
                    tp=r[6]
                )
            )

        return pedidos

    def close(self):
        self.db.close()