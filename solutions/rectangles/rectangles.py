
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)

class Rectangle:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

    def __repr__(self):
        return "[(%s, %s), (%s, %s), (%s, %s), (%s, %s)]" % (self.point1.x, self.point1.y, self.point2.x, self.point2.y, self.point3.x, self.point3.y, self.point4.x, self.point4.y)

    def __hash__(self):
        return hash((self.point1, self.point2, self.point3, self.point4))

    def __eq__(self,other):
        # A rectangle is equal to other rectangle when all points of the first exists on the other.
        other_points = [other.point1, other.point2, other.point3, other.point4]
        return self.point1 in other_points and self.point2 in other_points and self.point3 in other_points and self.point4 in other_points

    def __ne__(self, other):
        return not (self == other)




def get_colinear_points_dic(points):
    # Colinear points have the same X ou Y coordinate.
    # Returns a dictionary of colinear points for every single point given as parameter.

    colinear_x_points = []
    colinear_y_points = []
    result_dic = { point:[] for point in points }

    for point1 in points:
        for point2 in points:
            if point1 != point2:
                if point1.x == point2.x:
                    colinear_x_points.append(point2)
        
                if point1.y == point2.y:
                    colinear_y_points.append(point2)

        result_dic[point1] = result_dic[point1] + colinear_x_points
        result_dic[point1] = result_dic[point1] + colinear_y_points
        colinear_x_points = []
        colinear_y_points = []
    return result_dic



def get_rectangles(points):

    # Function that receives a list of points      
    # And return all possible rectangles (4 points) that can be obtained from the given points.
    
    rectangles = []
    intersects = []


    # for every point, look other point that has 2 points in common with the first
    # for example, (10,10) has (20,20) as corner points because (10,10) and (20,20) has (20,10) and (10,20) as colinear points 
    
    rec_dic = get_colinear_points_dic(points)
    for p1 in rec_dic:
        for p2 in rec_dic:
            if p1 != p2:
                intersect = set(rec_dic[p1]).intersection(set(rec_dic[p2]))
                
                if len(intersect) == 2:
                    if intersect not in intersects:
                        intersects.append(intersect)
                        rectangle = Rectangle(p1, p2, list(intersect)[0], list(intersect)[1])
                        if rectangle not in rectangles:
                            rectangles.append(rectangle)
    return rectangles



if __name__ == "__main__":
    points = [
            Point(10, 10),
            Point(10, 20),
            Point(10, 30),
            Point(20, 10),
            Point(20, 20),
            Point(20, 30),
            Point(30, 10),            
            Point(30, 20),
            Point(30, 30),
            Point(40, 10),
            Point(40, 20),
            Point(40, 30),
            Point(50, 10),  
            Point(50, 20),
            Point(50, 30),
            Point(60, 10),
            Point(60, 20),
            Point(60, 30)
            ]

    answer = get_rectangles(points)

    print(len(answer))

