
'''

cal = subprocess("curl -d "username=xgt008@gmail.com&password=886677" http://10.42.0.84:8000/api2/auth-token/")

tokenjson = simplejson.loads(curl_op1)


token = tokenjson["token"]

#replace with "token"

data = simplejson.loads(curl_op2)


print "Your Usage"+data["usage"]

print "Your Total Space"+data["total"]

print "Your User ID"+data["email"]


'''

import subprocess
import simplejson

def curl(*args):
        curl_path = '/usr/bin/curl'
        curl_list = [curl_path]
        for arg in args:
            curl_list.append(arg)
        curl_result = subprocess.Popen(
                     curl_list,
                     stderr=subprocess.PIPE,
                     stdout=subprocess.PIPE).communicate()[0]
        return curl_result

token_json = curl('-d','username=xgt008@gmail.com&password=886677','http://10.42.0.84:8000/api2/auth-token/')

tokenparser = simplejson.loads(token_json)

token_string = tokenparser["token"]

list_json = curl('-H','Authorization: Token '+token_string,'-H','Accept: application/json; indent=4','http://10.42.0.84:8000/api2/repos/')

#print list_json

#JSON DECODING to BE DONE


list_items = simplejson.loads(list_json)
print "Your files : \n"
for each_item in list_items:
	print each_item["name"]+"\t"
	print each_item['size']
	print "\t \n"


'''



curl  -v  -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4'

 https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/?p=/foo.c


http://10.42.0.84:8000/api2/repos/21c5c154-a84f-4025-942e-f8bc16c402b6/file?p=/6E%20GRP%20TKT-BLR-BOM-BLR-26-28JUL-JPMC.pdf

'http://10.42.0.84:8000/api2/repos/'+repo+'/file?p=/'+p

http://10.42.0.84:8000/repo/21c5c154-a84f-4025-942e-f8bc16c402b6/files/?p=/6E%20GRP%20TKT-BLR-BOM-BLR-26-28JUL-JPMC.pdf
'''