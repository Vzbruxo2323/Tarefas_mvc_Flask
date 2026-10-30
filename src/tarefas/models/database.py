
import mysql.connector as mc
from mysql.connector import Error


class Database:
    """Classe que gerencia conexão e operações com um banco de dados MySQL."""
    def __init__(self)->None:
        self.host = 'localhost'
        self.username = 'root'
        self.password = 'admin'
        self.database = 'vendas'
        self.connection = None
        self.cursor = None

    def conectar(self)->None:
        """Estabelace um conexão com banco de dados MySQL"""
        try:
            self.connection = mc.connect(
                host=self.host,
                database=self.database,
                user=self.username,
                password=self.password
            )

            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print('Conexão ao banco de dados realizada com sucesso!')

        except Error as e:
            print(f'Erro de conexão: {e}')
            self.connection = None
            self.cursor = None

    def desconectar(self)->None:
        """Encerra a conexão com banco de dados e o cursor, se existirem."""
        if self.cursor:
            self.cursor.close()

        if self.connection and self.connection.is_connected():
            self.connection.close()

        print('Conexão encerrada com sucesso!')


# Área 51
"""Tudoque for escrito dessa área
será lido e executado como string."""
bd = Database()
bd.conectar()
bd.desconectar()