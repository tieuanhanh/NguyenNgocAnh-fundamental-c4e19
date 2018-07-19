import pyexcel

file_excel = [
    {
        "Name": 'Anh',
        "Age": 23
    },
        
    {   "Name": 'Lien',
        "Age": 19
    }
]

pyexcel.save_as(records = file_excel, dest_file_name = "my_file.xlsx")