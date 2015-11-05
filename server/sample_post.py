import requests

# when deploying:
# - make sure you have python-requests package
# - set correct upload url
# - parameter 'files' of requests.post() should have docx1 and docx2
#   as parameter names

def docx_compare(file1, file2, result_file):
    with open(result_file, "wb") as handle:
        upload_url = 'http://trkchng.cloudapp.net:8081/upload'
        print 'Making request'
        r = requests.post(upload_url, files={'docx1': open(file1, 'rb'), 'docx2': open(file2, 'rb')}, stream=True)
        print 'Request sent'
        
        if not r.ok:
            print "Error"
            print r
            
        for block in r.iter_content(1024):
            handle.write(block)

docx_compare("sample1.docx", "sample2.docx", "result.docx")
