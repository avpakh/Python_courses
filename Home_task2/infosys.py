# -*- coding: cp1251 -*-
import os
import subprocess
import re
import commands


class sysInfo(object):
    """
    describe a class for system information getting from local computer

    """    
    def __init__(self):
       pass

    def _getProcessData(self):
        """
        Get list of processes
        """    
        ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).communicate()[0]
        processes = ps.split('\n')
        # this specifies the number of splits, so the splitted lines
        # will have (nfields+1) elements
        nfields = len(processes[0].split()) - 1
        retval = []
        for row in processes[1:]:
            retval.append(row.split(None, nfields))
        return retval
        

    def _get_user_name (self):
        """
        Get users names 
        """
        import getpass
        username = getpass.getuser()
        return username

    def _get_hddinfo (self,usercommand):
        """
        Get hhd info  
        """
        disk = os.statvfs("/var/")
        if usercommand == 'total space':
            val = float(disk.f_bsize*disk.f_blocks)
            val_Gb = '{:.3}'.format(val/1024/1024/1024) + ' Gb'
            return val_Gb
        if usercommand == 'used space':
            val = float(disk.f_bsize*(disk.f_blocks-disk.f_bfree))
            val_Gb = '{:.3}'.format(val/1024/1024/1024) + ' Gb'
            return val_Gb
        if usercommand == 'avaliable space':
            val = float(disk.f_bsize*disk.f_bfree)
            val_Gb = '{:.3}'.format(val/1024/1024/1024) + ' Gb'
            return val_Gb
        
          
    def _get_StrPro (self,workStr,inStr):
        """
        string processing during data collection

        """
        prStr = workStr.replace(inStr,'')
     
        prStr1 = prStr.replace(',','')
        prStr2 = prStr1.replace("'",'')
        prStr3 = prStr2.replace("[",'')
        prStr4 = prStr3.replace("]",'')

        prStr5 = prStr4[2:]
        prStr6 = prStr5[:-2]

        return prStr6
    

 
    def _get_cpu_info (self, data):
        """
        Get cpu info per request
        """
        
        with open('/proc/cpuinfo', 'r') as cpu:
            for z in cpu:
                sline = str(z.split(':'))
                if not sline.rfind(data) == -1:
                    tsline = self._get_StrPro(sline,data)              
                    return tsline

    def _get_mem_info (self, data):
        """
        Get memory info per request
        """
        
        with open('/proc/meminfo', 'r') as cpu:
            for z in cpu:
                sline = str(z.split(':'))
                if not sline.rfind(data) == -1:    
                    tsline = self._get_StrPro(sline,data)
                    return tsline

    def info_sys (self):
        """
        Get information per request

        """

        username = ' User name  -  '+ self._get_user_name()
        cpufamily = ' CPU family - : ' + self._get_cpu_info('cpu family')
        modelname = ' Model name - : ' +self._get_cpu_info('model name')
        vendorid =  ' Vendor  - ' +self._get_cpu_info('vendor_id')
        
        hdd1   = ' Total space  - ' + self._get_hddinfo('total space')
        hdd2   = ' Used space - ' +  self._get_hddinfo('used space')
        hdd3   = ' Avaliable space - ' +  self._get_hddinfo('avaliable space')

        mem1   = ' Total memory  - ' + self._get_mem_info('MemTotal')
        mem2   = ' Free memory - ' +  self._get_mem_info('MemFree')
        mem3   = ' Avaliable memory - ' +  self._get_mem_info('MemAvailable')        
        
        """
        get process data from subprocess request
        
        """
        pss1  = [ ]
        pstats = self._getProcessData()
        for ps in pstats:
            if (len(ps) >= 1):
                pss1.append(ps[0] + '    <----->  ' + ps [10])
            else: continue

        
        from jinja2 import Template

        tmpl = Template(u'''\
            <html>
            <head><title>{{ variable|escape }}</title></head>
            </body>
            <p>
            {{ variable|escape }}
            </p>
            <p>
            {% for item in item_list %}
            {{ item }}{% if not loop.last %},{% endif %}
            {% endfor %}
             <body>
             </p>
             <p>
            {% for item in item_list1 %}
            {{ item }}{% if not loop.last %},{% endif %}
            {% endfor %}
             </p>
              <p>
            {% for item in item_list2 %}
            {{ item }}{% if not loop.last %},{% endif %}
            {% endfor %}
             </p>
              <p>
            {{ var_pr|escape }}
            </p>
            <p>
            {{ var_pr1|escape }}
            </p>
            <p>
            {% for item in item_list3 %}
            <p>
            {{ item }}
            {% if not loop.last %},{% endif %}
            {% endfor %}
             </p>
            </body>
            </html>''')

        exportt = tmpl.render(
            variable='System info based on local python functions',
            var_pr=' Information about local processes',
            var_pr1='     user     <------->       process        ',
            item_list = [ username, cpufamily ,modelname, vendorid ],
            item_list1 = [ hdd1, hdd2, hdd3 ],
            item_list2 = [ mem1, mem2, mem3 ],
            item_list3 = pss1 )
         

        # to save the results of system test
        with open("sys_info.html", "wb") as fh:
            fh.write(exportt)
        fh.close()
 

        #information will be located in local directory in file (sys_info.html )
        print ' the results of estimation was located in sys_info.html file' 

r=sysInfo()
r.info_sys()



