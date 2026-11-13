
from flask import Flask, redirect, render_template, request, url_for

from tarefas.models.database import init_db
from tarefas.models.tarefas import Tarefa

app = Flask(__name__)

with app.app_context():
    init_db()


@app.route('/test')
def test():
    return 'Servidor online!'


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        titulo_form = request.form.get('tituloTarefa', '').strip()
        data_conclusao_form = request.form.get('dataConclusao')

        data_corrigida = data_conclusao_form or None

        # Instanciamos uma nova tarefa com os dados recebidos do formulário
        if titulo_form:

            tarefa = Tarefa(
                titulo=titulo_form,
                data_conclusao=data_corrigida
            )

            # Salvamos a tarefa no banco
            tarefa.salvarTarefa()

        return redirect(url_for('home'))

    tarefas = Tarefa.listarTarefas()

    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista de tarefas',
        titulo='Minha lista de tarefas',
        tarefas_da_pagina=tarefas,
        tarefa=None
    )


# Funcionalidade para apagar cada tarefa cadastrada
@app.route('/delete/<int:id>', methods=['POST'])
def apagar_id_especificado(id):

    tarefa = Tarefa(titulo='', id=id)
    tarefa.excluirTarefa()

    return redirect(url_for('home'))


# Rota para atualizar uma tarefa específica
@app.route('/atualizar/<int:id_tarefa>', methods=['GET', 'POST'])
def atualizar_tarefa(id_tarefa):

    # Carrega a tarefa do banco
    tarefa = Tarefa.buscarTarefa(id_tarefa)

    if tarefa is None:
        return redirect(url_for('home'))

    if request.method == 'POST':

        titulo_form = request.form.get('tituloTarefa', '').strip()
        data_conclusao_form = request.form.get('dataConclusao')

        data_corrigida = data_conclusao_form or None

        if titulo_form:

            # Envia os dados alterados para o banco
            Tarefa.atualizarTarefa(
                id_tarefa,
                titulo_form,
                data_corrigida
            )

        return redirect(url_for('home'))

    return render_template(
        'base.html',
        titulo='Atualizar tarefa',
        titulo_da_pagina='Atualizar tarefa',
        tarefas_da_pagina=Tarefa.listarTarefas(),
        tarefa=tarefa
    )


if __name__ == '__main__':
    app.run(debug=True)
