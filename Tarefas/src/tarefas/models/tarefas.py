
from tarefas.models.database import Database


class Tarefa:
    """Métodos para armazenar, recuperar e processar tarefas."""

    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def salvarTarefa(self):
        """Salva uma tarefa no banco de dados."""

        sql = """
            INSERT INTO tarefa (titulo_tarefa, data_conclusao)
            VALUES (%s, %s);
        """

        params = (self.titulo, self.data_conclusao)

        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def listarTarefas() -> list:
        """Retorna todas as tarefas cadastradas."""

        sql = """
            SELECT id_tarefa, titulo_tarefa, data_conclusao
            FROM tarefa
            LIMIT 100;
        """

        with Database() as db:
            tarefas_banco = db.executar(sql)

        return tarefas_banco if tarefas_banco else []

    @staticmethod
    def apagarTarefa(id_tarefa):
        """Apaga uma tarefa pelo ID."""

        sql = "DELETE FROM tarefa WHERE id_tarefa = %s;"
        params = (id_tarefa,)

        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def atualizarTarefa(id_tarefa, titulo_tarefa, data_conclusao):
        """Atualiza uma tarefa existente."""

        sql = """
            UPDATE tarefa
            SET titulo_tarefa = %s, data_conclusao = %s
            WHERE id_tarefa = %s;
        """

        params = (titulo_tarefa, data_conclusao, id_tarefa)

        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def buscarTarefa(id_tarefa):
        """Busca uma tarefa específica pelo ID."""

        sql = """
            SELECT id_tarefa, titulo_tarefa, data_conclusao
            FROM tarefa
            WHERE id_tarefa = %s;
        """

        params = (id_tarefa,)

        with Database() as db:
            tarefa_banco = db.executar(sql, params)

        if tarefa_banco:
            dados = tarefa_banco[0]

            return Tarefa(
                titulo=dados['titulo_tarefa'],
                id=dados['id_tarefa'],
                data_conclusao=dados['data_conclusao']
            )

        return None