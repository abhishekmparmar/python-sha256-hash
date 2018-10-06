import hashlib
path=raw_input('enter complete file path:')
hasher=hashlib.new('sha256')
with open(path,'r') as a:
	contents=a.read()
	hasher.update(contents)
print('SHA256 Hash :')
print(hasher.hexdigest())
