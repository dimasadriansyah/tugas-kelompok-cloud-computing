#Import reticulum
import RNS

#Start reticulum
reticulum = RNS.Reticulum()

#Buat identitas baru
identity = RNS.Identity()

#Destination TBA

#Tampilkan Identitas
print("Reticulum Identity: ")
# Tampilkan Hash identifier
print("Identity hash: ", identity.hash.hex())
#Tampilkan Public key
print("Identity public key: ", identity.get_public_key().hex())
