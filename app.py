from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

class AppBD:
    def __init__(self):
        pass

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres", password="kelly", host="127.0.0.1", port="5433", database="IBHJ_database")
        except (Exception, psycopg2.Error) as error:
            print("Falha ao se conectar ao Banco de Dados", error)

    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_select_query = "select * from despesas_administrativas"
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Erro na operação de seleção", error)
            registros = []
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
        return registros

    def inserirDados(self, codigo, descricao, valor_pago, data):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = "INSERT INTO despesas_administrativas (codigo, descricao, valor_pago, data) VALUES (%s, %s, %s, %s)"
            record_to_insert = (codigo, descricao, valor_pago, data)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao inserir dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()

    def deletarDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_delete_query = "DELETE FROM despesas_administrativas WHERE codigo = %s"
            cursor.execute(postgres_delete_query, (codigo,))
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao deletar dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()

    def editarDados(self, codigo, descricao, valor_pago, data):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_update_query = "UPDATE despesas_administrativas SET descricao = %s, valor_pago = %s, data = %s WHERE codigo = %s"
            cursor.execute(postgres_update_query, (descricao, valor_pago, data, codigo))
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao editar dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()

@app.route('/')
def index():
    bd = AppBD()
    registros = bd.selecionarDados()
    return render_template('index.html', registros=registros)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        codigo = request.form['codigo']
        descricao = request.form['descricao']
        valor_pago = request.form['valor_pago']
        data = request.form['data']

        bd = AppBD()
        bd.inserirDados(codigo, descricao, valor_pago, data)

        return redirect(url_for('index'))

@app.route('/delete/<codigo>', methods=['POST'])
def delete(codigo):
    bd = AppBD()
    bd.deletarDados(codigo)
    return redirect(url_for('index'))

@app.route('/edit', methods=['POST'])
def edit():
    if request.method == 'POST':
        codigo = request.form['codigo']
        descricao = request.form['descricao']
        valor_pago = request.form['valor_pago']
        data = request.form['data']

        bd = AppBD()
        bd.editarDados(codigo, descricao, valor_pago, data)

        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)