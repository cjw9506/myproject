#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)

    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:
    
    def issubset(self, other):
        self_list = []
        other_list = []
        compare_list = []
        for x in self:
            self_list.append(x)
        for x in other:
            other_list.append(x)
        print(self_list, other_list)
        print("other>=self에 없는 요소는")
        for i in self_list:
            if i not in other_list:
                compare_list.append(i)
        if compare_list == []:
            print("없습니다")
            print("self<=other입니다")
            print()
        else:
            for i in range(len(compare_list)):
                print(compare_list[i], end=' ')
            print()
            print("self!=other입니다")
            print()
    def issuperset(self, other):
        self_list = []
        other_list = []
        compare_list = []
        for x in self:
            self_list.append(x)
        for x in other:
            other_list.append(x)
        print(self_list, other_list)
        print("self>=other에 없는 요소는")
        for i in other_list:
            if i not in self_list:
                compare_list.append(i)
        if compare_list == []:
            print("없습니다")
            print("self>=other입니다")
            print()
        else:
            for i in range(len(compare_list)):
                print(compare_list[i], end=' ')
            print()
            print("self!=other입니다")
            print("update the self")
            a = self_list+compare_list
            print(a, "\nself>=other이 됩니다")
            print()
            
    def intersection_update(self, other):
        self_list = []
        other_list = []
        compare_list = []
        for x in self:
            self_list.append(x)
        for x in other:
            other_list.append(x)
        print(self_list, other_list)
        for i in self_list:
            if i not in other_list:
                compare_list.append(i)
        print("self&=other은")
        print(compare_list+other_list)
        print()
    
    def difference_update(self, other):
        self_list = []
        other_list = []
        compare_list = []
        for x in self:
            self_list.append(x)
        for x in other:
            other_list.append(x)
        print(self_list, other_list)
        for x in self_list:
            if x not in other_list:
                compare_list.append(x)
        print("self-=other은")
        print(compare_list)
        print()
    def symmetric_difference_update(self, other):
        self_list = []
        other_list = []
        compare_list = []
        for x in self:
            self_list.append(x)
        for x in other:
            other_list.append(x)
        print(self_list, other_list)
        for i in self_list:
            if i not in other_list:
                compare_list.append(i)
        for i in other_list:
            if i not in self_list:
                compare_list.append(i)
        print("self^=other은")
        print(compare_list)
        print()
        
    def add(self, elem):
        self_list = []
        elem_list = []
        compare_list = []
        for x in self:
            self_list.append(x)
        for x in elem:
            elem_list.append(x)
        for i in elem_list:
            if i not in self_list:
                compare_list.append(i)
        print(self_list, elem_list)
        print("add하면")
        print(self_list+compare_list)
        print()
    
    def remove(self, elem):
        self_list = []
        elem_list = []
        compare_list = []
        none_list = []
        for x in self:
            self_list.append(x)
        for x in elem:
            elem_list.append(x)
        for i in self_list:
            if i not in elem_list:
                compare_list.append(i)
        for i in elem_list:
            if i not in self_list:
                none_list.append(i)
        if none_list!=[]:
            raise Exception('key Error: 해당 요소가 self에 없습니다')
        print(self_list, elem_list)
        print("remove하면")
        print(compare_list)
        
        
x = Set([1,3,5,7, 1, 3])
y = Set([2,1,4,5,6])
x.issubset(y)
x.issuperset(y)
x.intersection_update(y)
x.difference_update(y)
x.symmetric_difference_update(y)
x.add([1,3,6])
x.remove([1,3])
#x.remove([1,3,6]) 
#exception입니다 

