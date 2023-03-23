import delivery
import package
import address
import person


Luis = person.Person(123, "Juan", "Mendez")
Luis.last_name = "Melendez"

Luis_Add = address.Address("Bolivar", "Cartagena", "Manga", "Calle #Cualquiera Casa X", "Segundo Piso")

Alejandra = person.Person(456, "Alejandra", "Arevalo")
Alejandra_Add = address.Address("Atlantico", "Barranquilla", "Villamar", "Calle #Cualquiera Casa Y", "Primer Piso")
Alejandra_Add.detail = "Tercer Piso"

Andres = person.Person(789, "Andres", "Villalba")

FirstPack = package.StandardPackage()
FirstPack.weight = 70.0

SecondPack = package.OverWeightPackage(1321, 80.5, "Xbox", 30.0, 20.0)
SecondPack.overweight = 14.5

FirstDelivery = delivery.Delivery(12345, "12-10-2020", 14, Luis, Alejandra, Luis_Add, Alejandra_Add, Andres, [FirstPack, SecondPack])

print(FirstDelivery)