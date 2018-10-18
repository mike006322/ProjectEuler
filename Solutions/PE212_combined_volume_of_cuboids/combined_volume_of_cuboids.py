#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler212

from kd_tree import kd_tree

def find_intersections(cuboid, three_d_tree):
    """
    Input is a cuboid in form (begin_x, end_x, begin_y, end_y, begin_z, end_z)
    and an augmented kd-tree with cuboids and their intersection values.
    Search through the tree that contains cuboids with their intersection values
    Return list of cuboids incident to input with their intersection values
    """

def cuboid_contained(cuboid, intersections):
    """
    Input is a cuboid in form (begin_x, end_x, begin_y, end_y, begin_z, end_z)
    and a list of cuboids together with their intersection values.
    Return boolean of whether or not the cuboid is contained in the other cuboids.
    """
    # This could be slow
    inters = []
    for c in intersections:
        inters.append(c[0])
    begin_x = cuboid[0]
    begin_y = cuboid[2]
    begin_z = cuboid[4]
    end_x = cuboid[1]
    end_y = cuboid[3]
    end_z = cuboid[5]
    x = [(begin_x, end_x)]
    y = [(begin_y, end_y)]
    z = [(begin_z, end_z)]
    while (len(x) > 0 or len(y) > 0 or len(z) > 0) and len(inters) > 0:
        # pop a cuboid from inters and take it's overlapping dimensions away from x, y or z
        # if the cuboid overlaps in a way that splits a dimension then replace it with two intervals less the overlap
        c = inters.pop()
        cbegin_x = c[0]
        cbegin_y = c[2]
        cbegin_z = c[4]
        cend_x = c[1]
        cend_y = c[3]
        cend_z = c[5]
        for interval in x:
            pass
    # is this the right course?
    # should I instead focus on whether it's fully contains to just weed out the obvoius non-belonging ones?
    # this mini problem reduces to the bigger problem.



def cuboid_intersection(cuboid1, cuboid2):
    """
    Input are cuboids in form (begin_x, end_x, begin_y, end_y, begin_z, end_z)
    Return cuboid of their intersection
    """
    begin_x = cuboid1[0]
    begin_y = cuboid1[2]
    begin_z = cuboid1[4]
    end_x = cuboid1[1]
    end_y = cuboid1[3]
    end_z = cuboid1[5]
    x = (begin_x, end_x)
    y = (begin_y, end_y)
    z = (begin_z, end_z)
    while len(x) > 0 and len(y) > 0 and len(z) > 0 and

def cuboid_volume(cuboid):
    """
    Input is cubdoid in form (begin_x, end_x, begin_y, end_y, begin_z, end_z).
    Return volume of cuboid.
    """
    begin_x = cuboid[0]
    begin_y = cuboid[2]
    begin_z = cuboid[4]
    end_x = cuboid[1]
    end_y = cuboid[3]
    end_z = cuboid[5]
    x = begin_x - end_x
    y = begin_y - end_y
    z = begin_z - end_z
    return abs(x*y*z)

def combined_volume_of_cuboids(cuboids):
    """
    Input is a list of cuboids in the form (begin_x, end_x, begin_y, end_y, begin_z, end_z).
    Return the combined volume of the cuboids.
    """

    three_d_tree = kd_tree()

    for cuboid in cuboids:
        intersections = find_intersections(cuboid, three_d_tree)
        if not cuboid_contained(cuboid, intersections):
            for intersection in intersections:
                three_d_tree.insert((cuboid, 0))
                c = cuboid_intersection(cuboid, intersection[0])
                three_d_tree.insert((c, intersection.value + 1))

    volume = 0
    for cuboid, intersection_value in three_d_tree.members:
        volume += cuboid_volume(cuboid) * (-1)**intersection_value
    return volume

if __name__ == '__main__':
    pass
