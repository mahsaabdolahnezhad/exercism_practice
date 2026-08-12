"""Functions for classifying triangles."""


def true_triangle(sides):
    """Function deciding if the object passes the triangle test. """
    return sides[0]>0 and sides[1]>0 and sides[2] >0 and sides[0] + sides[1] >=           sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >=           sides[1]


def equilateral(sides):    
    """Function determining if a triangle is equal on all sides. """
    if true_triangle(sides):
        return sides[0] == sides[1] == sides[2] 
    return False



def isosceles(sides):
    """Function determining if a triangle is equal on at least 2 parts."""
    if true_triangle(sides):
        return sides[0] ==sides[1] or sides[1] ==sides[2] or sides[0]== sides[2]
    return False
    


def scalene(sides):
    """Function determining if a triangle doesn't have equal sides."""
    if true_triangle(sides):
        return sides[0] != sides[1] and  sides[0] !=sides[2] and sides[1]!=sides[2]
    return False
