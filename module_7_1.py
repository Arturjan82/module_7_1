
#"Режимы открытия файлов". Задача "Учёт товаров":
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        text = file.read()
        file.close()
        return text


    def add(self, *products):
        file = open(self.__file_name, 'a')
        text = self.get_products()
        for i in products:
            var = i.name
            if var not in text:
                file.write(i.name)
                file.write(' ')
                file.write(str(i.weight))
                file.write(' ')
                file.write(i.category)
                file.write(' \n')
            else:
                print('Продукт', i.name, i.weight, i.category, 'уже есть в магазине')

        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1,p2,p3)

print(s1.get_products())