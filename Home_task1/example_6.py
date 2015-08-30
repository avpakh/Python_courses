"""

Generator of person()

>>> pg()
>>> pg()
>>> pg()
>>> pg()
>>> pg()

"""

def pg( ):
    """Return the resume for person  (man or woman).

    ValueError: x must be == 'man' or x must be == 'woman'

    """
    dict_name = {'man':['Ted','Alex','Rob'], 'woman':['Anna','Olga','Iren','Julia']}
    list_sex = ['man','woman']
    list_mstatus = ['single','married','divorced']
    list_children = ['no','one ','two','three ']
    list_workplace = ['company','freelance']
    list_position = ['senior','junior','lead']
    list_hobby = ['sport','cinema','tv shows']

    # generate person profile
    import random
    i_sex=random.randrange(0,len(list_sex))
    x = list_sex[i_sex]
    i_name = random.randrange(0,len(dict_name.get(x)))
    i_mst = random.randrange(0,len(list_mstatus))
    i_chdr = random.randrange(0,len(list_children))
    i_job = random.randrange(0,len(list_workplace))
    i_pos = random.randrange(0,len(list_position))
    i_hobby = random.randrange(0,len(list_hobby))

    in_name = dict_name.get(x)
    name = in_name[i_name]
    # define a resume
    resume = []
    resume.append (' ! Name -'+ name + ' ! sex - ' + x + ' ! status - ' + list_mstatus[i_mst-1] +  ' ! children :  - ' + list_children[i_chdr]
                   + ' ! work place: ' + list_workplace[i_job] + ' ! position ' +  list_position[i_pos] + ' ! hobby - ' +  list_hobby [i_hobby] );
    return resume
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()



