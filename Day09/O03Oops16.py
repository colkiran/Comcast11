
class Product:

    def __init__(self):
        self.prod = "Rin"
        self.__supplier = "HLL"          # private
        self._tax = "12%"                     # protected

    def get_details(self):
        print(f"The name of the product is :{self.prod}")
        print(f"The supplier is :{self.__supplier}")
        print(f"The tax is :{self._tax}")

prd1 = Product()
prd1.get_details()


# --------------------------------------------------------------
print("#" * 40)
class SurfExcel(Product):

    def disp(self):
        print("Disp of SurfExcel....")
        # print(self.__supplier)          # private
        print(self._tax)                # protected

s1 = SurfExcel()
s1.disp()