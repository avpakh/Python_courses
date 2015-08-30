# -*- coding: cp1251 -*-
import os ,sys, fnmatch


class roots(object):
    def __init__(self,path):
        self.path = path
     

    def _read_path(self):
        
        mask = '*.py'
        if self.path =='':
            path1 = "/home/alex"
        else:
            path1 = self.path
        path_f=[]
        for d, dirs, files in os.walk(path1): 
            for f in files:
                if fnmatch.fnmatch(f,mask): 
                    path = os.path.join(d,f)
                    path_f.append(path)
                
        return path_f
   

    def _read_file(self,namef):

        """
        Function for file reading 
        """
        
        tmp=''
        pr=0 # conditons of existing in line docstring
        f = open(namef)
        while True:
            line = f.readline()     # reading per line
            if not line.find('"""') == -1 and pr==0:
                tmp += line
                pr=1
            else:
                if pr==1 and line.find('"""') == -1:
                    tmp += line
                if pr==1 and  not line.find('"""') == -1:
                    tmp +=line
                    pr = 0
                
              
            if len(line) == 0:       #end of file
                break                #close of cycle
        return tmp
              
              
            
            
    def  add_path(self):
        k = self._read_path()
        i = 0
        tt = []
        while i < k.__len__():
            zz= self._read_file(k[i])
            tt.append(k[i] + '  !!!!!!!!!   ' + str(zz))
            i += 1

           
                    
        from jinja2 import Template

        tmpl = Template(u'''\
            <html>
           <head><title>{{ variable|escape }}</title></head>
            <html>
           </body>
            <p>
            {{ variable|escape }}
            </p>
        
            {% for item in item_list %}
            <p>
            {{ item }}
            </p>
            {% if not loop.last %}{% endif %}
            {% endfor %}
             </body>
             </html>''')

        exportt = tmpl.render(
            variable= ' List of files !!!! Docstring fragemens in files ',
            item_list = tt,
            
           )

           # to save the results
        with open("docstr.html", "wb") as fh:
            fh.write(exportt)
            fh.close()
        print 'File docstr.html was created in local directory'

"""
Write a path to local directory

"""
r = roots("/home/alex/Sources/Projects")
r.add_path() 

