import md5 # imports the md5 module to generate a hash
import os, binascii # include this at the top of your file
password = 'password'
# encrypt the password we provided as 32 character string
hashed_password = md5.new(password).hexdigest()
print hashed_password #this will show you the hashed value
# 5f4dcc3b5aa765d61d8327deb882cf99 -> nice!
salt = binascii.b2a_hex(os.urandom(15))
hashed_pw = md5.new(password + salt).hexdigest()
print hashed_pw
