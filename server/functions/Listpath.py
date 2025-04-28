import os 


def Listpath(pathname:  str ,  data: list) -> list:

    file_list = []
    for i in data:
                 
                if os.path.isdir(f"{pathname}/{i}"):
                       
                    file_list.append({  "isdir": True , "name": i , "path": f"{pathname}/{i}" , "ext": f"{os.path.splitext(i)[-1]}"})
                        
                else:
                    file_list.append({ "isdir": False  , "name": i , "path" : f"{pathname}/{i}" , "ext": f"{os.path.splitext(i)[-1]}"})
    return file_list