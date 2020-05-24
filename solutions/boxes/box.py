class Thing():
    def __init__(self, dim_x:int, dim_y:int, dim_z:int):
        """
        A box has 3 dimensions:
            dim_x = length
            dim_y = width
            dim_z = height
        """
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.dim_z = dim_z
        
        # starting with an empty box
        self.available_x = dim_x
        self.available_y = dim_y
        self.available_z = dim_z
        

class Box(Thing):
    
    # starting with an empty list of contents
    content = list()    
    
    def add_object(self, obj):
        """
        Aqui a porca torce o rabo...
        1- check if the box has space enough
        2- if it has, add the object
        3- return the box
        4- if has no space, raise an error "Not suitable"

        """
        if self.it_fits(obj):
            self.content.append(obj)
            return self
        else:
            raise Exception(f"Object {obj.name} does not fit on the box")

    def it_fits(self, obj):
          available = self.get_space_available()



    def remove_object(self, obj):
        """
        remove the object passed as parameter 
        Returns: the object removed
        """
        pass

    def list_content(self):
        """
        return box content
        """
        pass

    def get_space_available(self):
        pass




class Object(Thing):
    name = 
    def __str__(self):
        return '<Object {self.dim_x}, {self.dim_y}, {self.dim_z}>'
