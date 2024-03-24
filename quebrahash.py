import hashlib
import binascii
usuario = "Junior"
hashMimikatz = "87497869209472ieu872joww8e7893te" #hash de exemplo
try:
  with open("lista.txt", "r") as lista:
	  while True:
		  senha = lista.readline().strip("\n")
		  if not senha:
			  break
		  hash = hashlib.new('md4', senha.encode('utf-16le')).digest()
		  if binascii.hexlify(hash) == hashMimikatz:
			  print ("USER \t", usuario)
			  print ("USER \t", senha)
			  print ("USER \t", binascii.hexlify(hash))
			  break
except:
  print('Ocorreu um erro')
