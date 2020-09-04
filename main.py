import csv
from dao.PersonDao import PersonDao
from dao.AddressDao import AddressDao


address = AddressDao()


id_bairo = address.get_state("Centro")

print(id_bairo)
