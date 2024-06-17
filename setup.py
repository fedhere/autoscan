from distutils.core import setup

metadata = {'name':'autoscan',
            'version':'3',
            'description': 'Random Forest-powered difference image scanner for DES.',
            'author':'Danny Goldstein',
            'author_email':'dgold@berkeley.edu',
            'packages':['autoscan'],
            'package_data':{'autoscan':['database/*']}}

if __name__ == '__main__':
    setup(**metadata)      
      
