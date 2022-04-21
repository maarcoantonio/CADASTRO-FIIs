import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='cadastro_fii'
)
cursor = conexao.cursor()
#cursor.execute("CREATE TABLE FIIs(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Ticker VARCHAR(10) NOT NULL, Nome VARCHAR (50) NOT NULL, Preco DOUBLE, Categoria VARCHAR (20))")
#comando = """INSERT INTO FIIs(Ticker, Nome, Preco,Categoria) VALUES ('MXRF11', 'Maxi Renda FII', 9.14 ,'Papel')"""
comando = ("SELECT * FROM fiis")
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#conexao.commit()

#print(cursor.rowcount,'dados inserido')


