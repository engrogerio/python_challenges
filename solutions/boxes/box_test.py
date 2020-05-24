import unittest
from box import Box
from box import Object


class TestBoxMethods(unittest.TestCase):
    def setup(self): 
    
    
        dimx, dimy, dimz = 500, 400, 400
        box = Box(dimx, dimy, dimz)
        matchbox = Object(50,40,10) 

    def test_create_box(self):    
        # assert is empty
        self.assertEqual(box.available_x, dimx)
        self.assertEqual(box.available_y, dimy)
        self.assertEqual(box.available_z, dimz)
        # assert contains zero objects
        self.assertEqual(box.content, list())
    
    def test_create_object(self):
        
        self.assertNotEqual(matchbox, None)

    def test_add_object_to_box_fit(self):
        dimx, dimy, dimz = 500, 400, 400
        box = Box(dimx, dimy, dimz)
        matchbox = Object(50,40,10)
        x = box.add(matchbox)

    
    def test_add_object_to_box_does_not_fit(self):
        
        pass

    def test_add_multiple_objects(self):
        pass



if __name__ == '__main__':
    unittest.main()
