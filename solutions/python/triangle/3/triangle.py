def true_triangle(sides):
    if sides[0]>0 and sides[1]>0 and sides[2] >0 and sides[0] + sides[1] >=           sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >=           sides[1]:
        return True
    else:
        return False



def equilateral(sides):
    if true_triangle(sides):
        return sides[0] == sides[1] == sides[2] 
    else: return False


def isosceles(sides):
    if true_triangle(sides):
        return sides[0] ==sides[1] or sides[1] ==sides[2] or sides[0]== sides[2]
    else: return False
    


def scalene(sides):
    if true_triangle(sides):
        return sides[0] != sides[1] and  sides[0] !=sides[2] and sides[1]!=sides[2]
    else: return False
