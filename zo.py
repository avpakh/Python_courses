# -*- coding: cp1251 -*-

import logging
LOG = logging.getLogger(__name__)
AVIARY_CAP = 3 # capactity of aviary
MAX_AV = 10 # maximum aviary

class AviaryManagementError(Exception):
    pass

import os
import subprocess
import re
import commands

class MyAnimal(object):
    def __init__(self,name,spe,age,sex):
        self.name = name   
        self.spe = spe
        self.age = age
        self.sex= sex
    def get_type(self):
        return self.__class__.__name__
  

class Venom(MyAnimal):
    def __init__(self,name,spe,age,sex):
        super(Venom,self).__init__(name=name,spe=spe,age=age,sex=sex)
        
    
class Herbivore(MyAnimal):
    def __init__(self,name,spe,age,sex):
        super(Herbivore,self).__init__(name=name,spe=spe,age=age,sex=sex)
  

class Aviary(object):
    
    COUNT = 0
   
    def __init__(self,name,_type):
        self.animals =[] 
        self.name = name   
        self._type = _type
        self.__class__.COUNT += 1

    def delete_animal(self, anml):
        """
        Delete of animal for Aviary 
        """
        if anml in self.animals:
            print "Animal {0} in {1} aviory was deleted ".format((anml.name),self.name)
            self.animals.remove(self.animals[self.animals.index(anml)])
        else:
            print AviaryManagementError ("Animal {0} in {1} aviory not found.".format((anml.name),self.name))
            
    def add_animal(self, anml):
        """
        Add animal to Aviary 
        """    
        
        if  len(self.animals) < AVIARY_CAP:
            if type(anml) not in [Venom, Herbivore]:
                raise AviaryManagementError("Cannot add animal. Bad param of type")
            else:
                if anml.get_type() == self._type:
                   self.animals.append(anml)
                else:
                    raise AviaryManagementError("Cannot add {0} to {1} aviory.".format(anml.get_type(), self._type))
                
        else:
            raise AviaryManagementError("Cannot add animal. Aviary is full")
         
    @classmethod
    def get_aviary_count(cls):
        return cls.COUNT


                
                
            
            
           
        

class Zoo(object):
    

    def __init__(self):
        self.aviaries = []


    def add_aviary(self,av):
        if type(av) != Aviary:
            raise AviaryCreationError ("Bad type of aviary. Not posssible to add")
        if len(t.aviaries) < MAX_AV:
            self.aviaries.append(av)
        else:
            raise AviaryCreationError ("No space for aviary ")
        pass      

    def delete_aviary(self,av):
        if type(av) != Aviary:
            raise AviaryCreationError ("Bad type of aviary. Not posssible to delete")
        self.aviaries.remove(av)
        pass    

    
   
class MenuManager(object):
    def __init__(self):
        pass


    def mainmenu(self):
        """
        Main menu selection 
        """
        print "Please made a choice 1-9:"        
        print " ---------------------------------------------------------"        
        print "| 1.  Add animal                                         |"
        print "| 2.  Del animal                                         |"
        print "| 3.  Add aviary                                         |"
        print "| 4.  List of existing aviary with animals               |"
        print "| 5.  Distribution of animals in aviaries                |"
        print "| 6.  Delete of aviary                                   |"
        print "| 7.  Move of animal within Zoo                          |"
        print "| 8.  Statistics                                         |"
        print "| 9.  Exit                                               |"
        print " ---------------------------------------------------------"
        main_menu = raw_input('Input menu position : ')
        if main_menu.isdigit() ==1:
            if int(main_menu) in  range(1,10):
                if int(main_menu)== 1:
                    self.main_menu1()
                if int(main_menu)== 2:
                    self.main_menu2()
                if int(main_menu)== 3:
                    self.main_menu3()
                if int(main_menu) == 4:
                    self.main_menu4()
                if int(main_menu) == 5:
                    self.main_menu5()
                if int(main_menu) == 6:
                    self.main_menu6()
                if int(main_menu) == 8:
                    self.main_menu8()
                if int(main_menu) == 9:
                    self.main_menu9()
                if int(main_menu) == 7:
                    self.main_menu7()
                    
            else:
                print " Incorrect input"    
                self.mainmenu()
        else:
            print " Incorrect input"
            self.mainmenu()

        return

    def main_menu9(self):
        print "Exit from ZOO "
        quit

    def main_menu2(self):
        name_an_list=[]
        print " Existing animals in avaries "
        for i in t.aviaries:
            k = []
            x = ''
            for tt in range(len(i.animals)):
                x += " " + "X"
            for ii in range(len(i.animals)):
                k.append(i.animals[ii].name)
                name_an_list.append(i.animals[ii].name)
            print i.name + "  --> " + i._type +  " ::: " + str(k) + x

        name_animal = raw_input('Input name of deleted animal:->  ')
        if name_animal.isalpha() and name_animal in name_an_list:
            for i in t.aviaries:
                for ii in range(len(i.animals)):
                    if name_animal == i.animals[ii].name:
                        i.delete_animal(i.animals[ii])
                        
                        self.mainmenu()
                        return
        else:
             print "Error of operation . Please write a name as it's displayed "
             self.main_menu2()
             
        return
        

    def main_menu1(self):
        """
        add animal procedure
        """
        list_1 = ["V","v","H","h"]
        list_2 = ["M","m","F","f"]
        vlist = []
        hlist = []

        infile = open('vlist.txt','r')   #list this types of venoms
        for line in infile:
            vlist.append(line.strip())
            
        infile.close()
        infile = open('hlist.txt','r')   #list this types of herbivores
        for line in infile:
            hlist.append(line.strip())
        infile.close()
        
        print " 1. Add animal:"        
        print " ---------------------------------------------------------"


        in1 = False
        while in1 == False:
            name_mtype = raw_input('Input klass of animal ("V"enom or "H"erbivore") : type "V" or "H" :-> ')
            if name_mtype.isalpha():
                if str(name_mtype) in list_1:
                    if name_mtype == "V" or name_mtype == "v":
                        name_mtype = "Venom"
                        in1 = True
                    if name_mtype == "H" or name_mtype == "h":
                        name_mtype = "Herbivore"
                        in1 = True
                else:
                    print " Incorrect input of klass of animal. Retry "
                    
                        
            else:
                print " Incorrect input of klass of animal. Retry "


        in0 = False
        while in0 == False:
            name_animal = raw_input('Input name of animal:-> (minimum  3 characters) ')
            if name_animal.isalpha() and len(name_animal) >=3:
                in0=True
            else:
                print " Incorrect input name of animal. Retry "    

        
        in4 = False
        print " Help : "
        if name_mtype == "Venom":
            print vlist
        if name_mtype == "Herbivore":
            print hlist
        while in4 == False:
            name_kind = raw_input('Input kind(species) of animal :-> (from list) ')
            if name_mtype == "Venom":
                if str(name_kind) in vlist:
                    in4=True
                else:
                    print " Incorrect input kind of venom animal. Retry "
                

            if name_mtype == "Herbivore":
                if str(name_kind) in hlist:
                    in4=True
                else:
                    print " Incorrect input kind of herbivore animal. Retry "
                    

        
        in2 = False
        while in2 == False:
            name_sex = raw_input('Input sex of animal ("M"ale or "F"emale ") : type "M" or "F" :-> ')
            if name_sex.isalpha():
                if str(name_sex) in list_2:
                    if name_sex == "M" or name_sex == "m":
                        name_sex = "Male"
                        in2 = True
                    if name_sex == "F" or name_sex == "f":
                        name_age = "Female"
                        in2 = True
                else:
                    print " Incorrect name of sex. Retry "
                   
            else:
                print " Incorrect name of sex. Retry "        

        in3 = False    
        while in3 == False:
            name_age = raw_input('Input age of animal : - >')
            if  name_age.isdigit():
                if int(name_age) in range(1,100):
                    name_age  = int (name_age)
                    in3 = True
                else:
                    print " Incorrect input of age. not in the range (1-100) years. Retry"    
            
            else:
                print " Incorrect input of age. Retry"

       
        if  name_mtype == "Venom":
            an=Venom(name_animal,name_kind,name_age,name_sex)
            print ' animal  coming to Zoo '
         

      
        if  name_mtype == "Herbivore":
            an=Herbivore(name_animal,name_kind,name_age,name_sex)
            print ' animal  coming to Zoo '

        if len(t.aviaries) > 0:
            
            for z in t.aviaries:
                if an.get_type() == z._type:
                    if  len(z.animals) < AVIARY_CAP: 
                        z.add_animal(an)
                        self.mainmenu()
                        return
                        
        else:
            print "Not avaliable aviaries"

        
        return


    def main_menu8(self):

        """
        get ZOO statistics
        """

        print " 8. Statistics in ZOO "
        print " ---------------------------------------------------------"

        vv = 0
        hv = 0

        A_count = 0

        AV_count = 0
        AH_count = 0

        k_v = []
        k_h = []
          
        for az in t.aviaries:
            vk = 0
            vz = 0
            if az._type == 'Venom':
                for ii in range(len(az.animals)):
                    k_v.append(az.animals[ii].name)
                    vk +=1 
                vv = vv + AVIARY_CAP - vk
                            
            if az._type == 'Herbivore':    
                for ii in range(len(az.animals)):
                    k_h.append(az.animals[ii].name)
                    vz +=1
                hv = hv + AVIARY_CAP - vz

  
        V_count = len(k_v)
        H_count = len(k_h)
        
        print " Venom - ", V_count
        print " Herbivore - ", H_count
        print " Vacancy(Venom) - ", vv
        print " Vacancy(Herbivore) - ", hv
        

        self.mainmenu()         
        return

            

        
    def main_menu4(self):
        """
        Show a existing aviaries with animal
        """
        print " Lists of existing aviaries with animals "
        for i in t.aviaries:
            k = []
            x = ''
            for tt in range(len(i.animals)):
                x += " " + "X"
            for ii in range(len(i.animals)):
                k.append(i.animals[ii].name)  
            print i.name + "  --> " + i._type +  " ::: " + str(k) + x

        self.mainmenu()         
        return

    def main_menu5(self):
        """
        Show a existing aviaries with setalied information about animals
        """
        print " Lists of animals in aviaries "
        for i in t.aviaries:
            k = []

            x = ''
            for tt in range(len(i.animals)):
                x += " " + "X"
            for ii in range(len(i.animals)):
                k.append(i.animals[ii].name + "|" +  str(i.animals[ii].age) + "|" + i.animals[ii].spe + "|" + i.animals[ii].sex  )
             
                              
                
            print i.name + "  --> " + i._type +  " ::: " + str(k) +" | "   + x 

        self.mainmenu()         
        return
    


    def main_menu6(self):
        """
        Delete existing existing aviaries
        """
        list_av = []
        list_an = []
        del_in  = 0
        print " 6. Delete of existing aviaries:"        
        print " ---------------------------------------------------------"

         
        for l in t.aviaries:
          
            print l.name + "  --> " + l._type
            list_av.append(l.name)

        #print list_av 

        name_av = raw_input('Input name of deleted aviary:->  ')
        if name_av in list_av:
            for i in t.aviaries:
                if name_av == i.name:
                    del_in = i
                    if len(i.animals)== 0:  # delete empty aviary 
                        t.delete_aviary(i)
                        self.mainmenu()
                        return 
                    else:   # try to realocate animals in nearest aviary
                        for ii in range(len(i.animals)):
                            list_an.append(i.animals[ii])
                        #list_an

                        for n in list_an:            
                            for z in t.aviaries:
                                if n.get_type() == z._type and z != del_in:
                                    if  len(z.animals) < AVIARY_CAP: 
                                        z.add_animal(n)
                                      
                        
                             

                        t.delete_aviary(i)
                        self.mainmenu()
                        return
        else:
            print "Error of operation . Please write a name as it's displayed "
            self.main_menu6()
             
        return


    def main_menu7(self):
        """
        Moving animal within ZOO (aviaries)
        """
        list_av = []
        list_name2 = []
        name_at_list = []
        del_in  = 0
    
        
        print " 7. Move of animal within Zoo                             "        
        print " ---------------------------------------------------------"

        print " List of animals in aviaries "
        for i in t.aviaries:
            k = []

            x = ''
            for tt in range(len(i.animals)):
                x += " " + "X"
            for ii in range(len(i.animals)):
                    k.append(i.animals[ii].name + " ")
                    name_at_list.append(i.animals[ii].name) 
            print i.name + "  --> " + i._type +  " ::: " + str(k) +" | "   + x


        name_animal_m = raw_input('Input name of animal which you want to move :->  ')
        
        if name_animal_m.isalpha() and name_animal_m in name_at_list:
            for i in t.aviaries:
                for ii in range(len(i.animals)):
                    if i.animals[ii].name == name_animal_m:
                        av_ob=i
                        an_ob=i.animals[ii]
                        print av_ob._type

            for zz in t.aviaries:
                
                    if  av_ob != zz and av_ob._type == zz._type and  len(zz.animals) < AVIARY_CAP :
                        list_av.append(zz.name) 

            
                      
            print " List of avaliable aviary with free spaces"
            print list_av

            print "You selected animal {0} for moving ".format(name_animal_m)


            if len(list_av) == 0:
                print "Not free places for moving animal. Please add new aviary"
                self.mainmenu() 
                return
            else:
                name_in = raw_input('Input name of aviary in where you want to move selected animal : = >> ')
                if name_in in list_av:
                    for i in t.aviaries:
                        if name_in == i.name:
                            if  len(i.animals) < AVIARY_CAP:
                                i.add_animal(an_ob)
                                av_ob.delete_animal(an_ob) 
                                self.mainmenu()
                                return
                            else:
                                print "Error of operation . Please write a correct name as it's displayed "
                                self.main_menu7()   
                    

            
        else:
            print "Error of operation . Please write a name as it's displayed "
            self.main_menu7()

                          
        return





          

    def main_menu3(self):
        """
        Add aviary
        """
        list_1 = ["V","v","H","h"]
        vlist = []
        hlist = []
        infile = open('vlist.txt','r')   #list this types of venoms
        for line in infile:
            vlist.append(line.strip())
            
        infile.close()
        infile = open('hlist.txt','r')   #list this types of herbivores
        for line in infile:
            hlist.append(line.strip())
        infile.close()
        
        print  " 3: Add_aviary "
        print " ---------------------------------------------------------"
        in1 = False
        while in1 == False:
            name_mtype = raw_input('Input klass of animal ("V"enom or "H"erbivore") : type "V" or "H" :-> ')
            if name_mtype.isalpha():
                if str(name_mtype) in list_1:
                    if name_mtype == "V" or name_mtype == "v":
                        name_mtype = "Venom"
                        in1 = True
                    if name_mtype == "H" or name_mtype == "h":
                        name_mtype = "Herbivore"
                        in1 = True
                else:
                    print " Incorrect input of klass of animal. Retry "
                    
                        
            else:
                print " Incorrect input of klass of animal. Retry "

        in4 = False
        print " Help : "
        if name_mtype == "Venom":
            print vlist
        if name_mtype == "Herbivore":
            print hlist
        while in4 == False:
            name_kind = raw_input('Input kind(species) of animal :-> (from list) ')
            if name_mtype == "Venom":
                if str(name_kind) in vlist:
                    in4=True
                else:
                    print " Incorrect input kind of venom animal. Retry "
                

            if name_mtype == "Herbivore":
                if str(name_kind) in hlist:
                    in4=True
                else:
                    print " Incorrect input kind of herbivore animal. Retry "
        
        av=Aviary(name_kind,name_mtype)
        t.add_aviary(av)
        self.mainmenu()          
        return 

    def Generator(self):
        av1 = Aviary('wolf','Venom')
        av2 = Aviary('puma','Venom')
        av3 = Aviary('tiger','Venom')
        av4 = Aviary('cows','Herbivore')

        t.add_aviary(av1)
        t.add_aviary(av2)
        t.add_aviary(av3)
        t.add_aviary(av4)

        a1= Venom('Chucha','wolf',10,'M')
        a2= Venom('Gosha','wolf',9,'M')
        a3= Venom('Rub','wolf',8,'M')
        a4= Venom('Rony','puma',6,'F')
        a5= Venom('Petr','tiger',9,'M')
        a6= Venom('Zak','puma',8,'M')
        a7= Herbivore('Roza','cows',4,'F')

        av1.add_animal(a1)
        av1.add_animal(a2)
        av1.add_animal(a3)

        av2.add_animal(a4)
        av3.add_animal(a5)
        av2.add_animal(a6)
    
        av4.add_animal(a7)
        return

t= Zoo()


menu  = MenuManager()
menu.Generator()
menu.mainmenu()
