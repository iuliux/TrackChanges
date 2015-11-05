import cherrypy
import cherrypy.lib.static
import os
import tempfile
import subprocess

import time

class TempFile(object):
    def __init__(self, file_):
        self._file = file_

    def close(self):
        name = self._file.name
        self._file.close()
        os.remove(name)

    def __getattr__(self, attr):
         return getattr(self._file, attr)


def copy_file(src_file, dest_file):
    df = open(dest_file, "wb")    
    while True:
        data = src_file.read(8192)
        if not data:
            break
        df.write(data)
    df.close()

class ComparatorService(object):

    def index(self):
        return """
        <html><body>
            <h2>Upload two DOCX files, they are compared and result returned</h2>
            <form action="upload" method="post" enctype="multipart/form-data">
            filename1: <input type="file" name="docx1" /><br />
            filename2: <input type="file" name="docx2" /><br />
            <input type="submit" />
            </form>
        </body></html>
        """
    index.exposed = True

    def upload(self, docx1, docx2):
        doc1 = tempfile.mkstemp(dir="C:\Temp\docx_comp")
        doc2 = tempfile.mkstemp(dir="C:\Temp\docx_comp")
        output = tempfile.mkstemp(".docx", dir="C:\Temp\docx_comp") # reserving file name
        
        os.close(doc1[0])
        os.close(doc2[0])
        os.close(output[0])

        copy_file(docx1.file, doc1[1])
        copy_file(docx2.file, doc2[1])
        
        callstr = "docx_comp.exe %s %s %s" % (doc1[1], doc2[1], output[1])
        print "Processing: %s" % callstr
        res = subprocess.call(callstr)
                             
        if res:
            raise Exception("docx_comp error %d" % res)            
        else:
            resf = TempFile(open(output[1], "rb"))
                
            # lets remove those only when all is ok
            os.remove(doc1[1])
            os.remove(doc2[1])
            return resf

    upload.exposed = True

config = {'global':
    {
        'server.socket_port': 8081
    }
}

if __name__ == '__main__':
    cherrypy.quickstart(ComparatorService(), config=config)

