# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:08:59 2017

@author: curio
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    
    sum = 0
    count = 0
    for i in s:
        
        try:
            sum += int(i)
        except ValueError:
            count += 1
    
    if count == len(s):
        raise ValueError()
    
    return sum

def test_sum_digits():
    
    assert sum_digits("123") == 6
    assert sum_digits("12a") == 3
    assert sum_digits("000") == 0
    
    try:
        sum_digits("aa")
        assert False
    except ValueError:
        assert True
    
    
def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    
    max = 0
    
    for e in t:
        
        if type(e) == list or type(e) == tuple:
            i = max_val(e)
            
        else:
            i = e
        
        if i > max:
            max = i
    
    return max


def test_max_val():
    assert max_val((5, (1,2), [[1],[2]])) == 5
    assert max_val((5, (1,2), [[1],[9]])) == 9
    assert max_val([1, 2, 3]) == 3
    assert max_val((1, 3)) == 3


def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    
    key_code = {}
    decoded = ""
    
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    
    for c in code:
        decoded += key_code[c]
    
    return key_code, decoded


def test_cipher():
    assert cipher("abcd", "dcba", "dab") == ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')

    
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s


class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        
        if e in self.vals:
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        
        if not e in self.vals:
            return 0
        
        return self.vals[e]
    
    def __add__(self, other):
        
        sum = Bag()
        
        for i in self.vals:
            sum.vals[i] = self.vals[i]
            
        for i in other.vals:
            
            if i in sum.vals:
                sum.vals[i] += other.vals[i]
            else:
                sum.vals[i] = other.vals[i]
        
        return sum
        

def test_bag():
    
    bag1 = Bag()
    bag1.insert("a")
    assert bag1.count("a") == 1
    
    bag1.remove("a")
    assert bag1.count("a") == 0
    
    assert bag1.count("b") == 0
    
    bag1.remove("a")
    bag1.remove("a")
    bag1.remove("a")
    assert bag1.count("a") == -3
    assert bag1.__str__() == "a:-3\n"


def test_bag_add():
    
    bag1 = Bag()
    bag1.insert("a")
    bag1.insert("b")
    
    bag2 = Bag()
    bag2.insert("a")
    bag2.insert("c")
    
    bag3 = bag1 + bag2
    
    assert bag3.count("a") == 2
    assert bag3.count("b") == 1
    assert bag3.count("c") == 1

    
class ASet(Container):
    
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        
        if e in self.vals:
            del self.vals[e]

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        
        return e in self.vals

def test_aset():
    
    set1 = ASet()
    set1.insert("a")
    
    assert set1.is_in("a") == True
    assert set1.is_in("b") == False
    
    set1.remove("a")
    
    assert set1.is_in("a") == False
    

### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        
        Campus.__init__(self, center_loc)
        self.tents = []
        self.add_tent(tent_loc)
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        
        for t in self.tents:
            if t.dist_from(new_tent_loc) < 0.5:
                return False
        
        for i in range(len(self.tents)):
            if self.tents[i].getX() > new_tent_loc.getX():
                self.tents.insert(i, new_tent_loc)
                return True
            
        self.tents.append(new_tent_loc)
        return True
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        
        for t in self.tents:
            if t == tent_loc:
                del t
                return
        
        raise ValueError()
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        
        tents = []
        
        for t in self.tents:
            tents.append(t.__str__())
        
        return tents


def test_MITCampus():
    
    c = MITCampus(Location(1,2))
    
    assert c.add_tent(Location(2,3)) == True
    assert c.add_tent(Location(1,2)) == True
    assert c.add_tent(Location(0,0)) == False
    assert c.add_tent(Location(2,3)) == False
    assert c.get_tents() == ['<0,0>', '<1,2>', '<2,3>'], c.get_tents()


if __name__ == "__main__":
    
    test_sum_digits()
    test_max_val()
    test_cipher()
    test_bag()
    test_bag_add()
    test_aset()
    test_MITCampus()
