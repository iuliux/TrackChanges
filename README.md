--- install on Windows box
- needed
  - .NET version >= 2.0
  - MS Word with PIA installed (adding link where you can download
    only PIA, without Word; still Word itself is also needed)
    http://www.microsoft.com/en-us/download/details.aspx?id=3508
  - Python 2.7
  - python-cherrypy
- installation
  - copy comparator_service.py and docx_comp.exe to a folder    
  - make folder "C:\Temp\docx_comp" - temp files will be stored there
- configuration
  - currently, port 8081 is used, you may want to change it because
    of a firewall; search comparator_service.py for 'server.socket_port'    
- launch
  - from command line, and leave cmd window open
    > python comparator_service.py
- testing
  - you use URL "localhost:8081" on Windows box to see index page, where
    you can upload two documents by hand
- modifying docx_comp source
  - I used MS Visual Studio 2005 to create it; please, check docx_comp.zip

--- access from Python on other server, as per sample_post.py
- needed
  - Python 2.7
  - python-requests
- just set correct upload url and it should work
