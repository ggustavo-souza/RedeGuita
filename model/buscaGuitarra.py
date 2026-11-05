from screens.menuInicial import menuInicial


class buscaGuitarra:
    # Atributos de uma guitarra a ser buscada
    __marca: str = ""
    __minPreco: float = 0
    __maxPreco: float = 0
    __cor: str = ""
    __modelo: str = ""

    # Getters
    @property
    def marca(self):
        return self.__marca

    @property
    def minPreco(self):
        return self.__minPreco

    @property
    def maxPreco(self):
        return self.__maxPreco

    @property
    def cor(self):
        return self.__cor

    @property
    def modelo(self):
        return self.__modelo
    
    # Setters
    @marca.setter
    def marca(self, marca: str):
        self.__marca = marca

    @minPreco.setter
    def minPreco(self, minPreco: float):
        self.__minPreco = minPreco

    @maxPreco.setter
    def maxPreco(self, maxPreco: float):
        self.__maxPreco = maxPreco

    @cor.setter
    def cor(self, cor: str):
        self.__cor = cor

    @modelo.setter
    def modelo(self, modelo: str):
        self.__modelo = modelo

    def estaVazia(self):
        return self.__marca == "" and self.__minPreco == 0 and self.__maxPreco == 0 and self.__cor == "" and self.__modelo == ""

    def buscarGuitarras(self):
        # implementar a lógica futuramente
        print("Buscando guitarras com o perfil:")
        print(f"Marca: {self.marca}")
        print(f"Preço mínimo: {self.minPreco}")
        print(f"Preço máximo: {self.maxPreco}")
        print(f"Cor: {self.cor}")
        print(f"Modelo: {self.modelo}")

        menuInicial("")

