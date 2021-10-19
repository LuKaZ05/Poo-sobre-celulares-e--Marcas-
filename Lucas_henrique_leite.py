import datetime
class Celular:

    def __init__(self,Modelo,Marca,preco,dtalancamento=datetime.date(2020,8,25)):
        self.Modelo = Modelo
        self.Marca  = Marca
        self.preco  = preco
        self.dtalancamento =dtalancamento

    def get_Modelo(self):
        return self.Modelo

    def get_Marca(self):
        return self.Marca

    def get_preco(self):
        return self.preco

    def get_dtalancamento(self):
        return  self.dtalancamento

    def set_Modelo(self,NModelo):
        self.Modelo = NModelo

    def set_Marca(self,NMarca):
        self.Marca = NMarca

    def set_preco(self,Npreco):
        self.preco = Npreco

    def set_dtalancamento(self,Ndta):
        self.dtalancamento = Ndta

    def Mdados(self):
        print('Modelo: ', self.Modelo)
        print('Marca: ',self.Marca)
        print('Preço: ',self.preco)
        print('Data de lançemento: ',self.dtalancamento)

    def MD2(self):
        print('Modelo: ',self.get_Modelo())
        print('Marca: ',self.get_Marca())
        print('Preço: ',self.get_preco())
        print('Data de lançemento: ',self.get_dtalancamento())

    def Rdados(self):

        dados = f'{self.Modelo},{self.Marca},{self.preco},{self.dtalancamento}'
        return dados

    def preco_bom(self):
        if self.preco >=3500:
            print("O preço condiz com o mercado")
        else:
            print("Um preço muito alto e pouco competitivo")

    def software(self):

        if self.Marca == 'Iphone':
            print("sistema operacional da Apple")
        elif self.Marca == 'Android':
            print('Usa sistema operacional Android')

if __name__ == '__main__':
        cell1 = Celular('Galaxy s10','Android',3800)
        cell2 = Celular('Iphone X','Iphone',6000)
        print("Celular 1: ")
        print("Modelo: ",cell1.get_Modelo())
        print("Marca: ",cell1.get_Marca())
        print("preco: ",cell1.get_preco())
        print("celular 2: ")
        print(f"Modelo:{cell2.get_Modelo()}")
        print(f"Marca:{cell2.get_Marca()}")
        print(f"Preço:{cell2.get_preco()}")
        print(cell1)
        print(cell2)
        print('Dados retidos:',cell1.Rdados())
        print('Dados retidos:',cell2.Rdados())

        cell1.preco_bom()
        cell1.software()
        cell2.preco_bom()
        cell2.software()