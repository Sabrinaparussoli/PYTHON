import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passaword='',
    db='livraria',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conexao.cursor()

cursor.execute('create tables users(nome varchar (30), idade int, end varchar(100));')

cursor.close()
conexao.close()


