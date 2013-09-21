import subprocess
import simplejson
import requests
import logging.config
import time
import httplib, mimetypes
import urlparse

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

def post_multipart(host, selector, fields, files):
    
    content_type, body = encode_multipart_formdata(fields, files)
    h = httplib.HTTP(host)
    h.putrequest('POST', selector)
    h.putheader('content-type', content_type)
    h.putheader('content-length', str(len(body)))
    h.endheaders()
    h.send(body)
    errcode, errmsg, headers = h.getreply()
    print errcode, errmsg, headers
    return h.file.read()

def encode_multipart_formdata(fields, files):
    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = '\r\n'
    L = []
    for (key, value) in fields:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

def get_upload_link(domain, uri):
    conn = httplib.HTTPConnection(domain)
    headers = {'Host': domain}
    headers['Authorization'] = 'Token '+token_string
    conn.request("GET", uri, None, headers)
    return conn.getresponse().read()

if __name__ == '__main__':

    token_json = curl('-d','username=xgt008@gmail.com&password=886677','http://10.42.0.84:8000/api2/auth-token/')

    tokenparser = simplejson.loads(token_json)

    token_string = tokenparser["token"]

    list_json = curl('-H','Authorization: Token '+token_string,'-H','Accept: application/json; indent=4','http://10.42.0.84:8000/api2/repos/')

    list_items = simplejson.loads(list_json)
    print "Your Repositories: \n"
    print "Name"+"\t"+"RepoID"+5*"\t"+"Size"
    for each_item in list_items:
        print each_item["name"]+"\t"+each_item['id']+'\t'+str(each_item['size'])+"\t \n"

    print token_string
    repo = '0e1fcd92-ff26-4382-af21-c2015017a850'

    upload_link = curl('-H','Authorization: Token '+token_string,'http://10.42.0.84:8000/api2/repos/0e1fcd92-ff26-4382-af21-c2015017a850/upload-link/')

    upload_link = upload_link[1:len(upload_link)-1]
    
    urlparts = urlparse.urlsplit(upload_link)

    fields = [('parent_dir', '/')]

    files = [('file', 'sample.pdf', open('sample.pdf').read())]
    
    post_multipart(urlparts[1], urlparts[2], fields, files)
