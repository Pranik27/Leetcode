# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 17:40:36 2021

@author: PRANIKP

There are two vector A and B and we have to find the dot product and cross product of two vector array. Dot product is also known as scalar product and cross product also known as vector product.

Dot Product – Let we have given two vector A = a1 * i + a2 * j + a3 * k and B = b1 * i + b2 * j + b3 * k. Where i, j and k are the unit vector along the x, y and z directions. Then dot product is calculated as dot product = a1 * b1 + a2 * b2 + a3 * b3

Example –

A = 3 * i + 5 * j + 4 * k
B = 2 * i + 7 * j + 5 * k
dot product = 3 * 2 + 5 * 7 + 4 * 5
            = 6 + 35 + 20
            = 61
Cross Product – Let we have given two vector A = a1 * i + a2 * j + a3 * k and B = b1 * i + b2 * j + b3 * k. Then cross product is calculated as cross product = (a2 * b3 – a3 * b2) * i + (a3 * b1 – a1 * b3) * j + (a1 * b2 – a2 * b1) * k, where [(a2 * b3 – a3 * b2), (a3 * b1 – a1 * b3), (a1 * b2 – a2 * b1)] are the coefficient of unit vector along i, j and k directions.

Example –



A = 3 * i + 5 * j + 4 * k
B = 2 * i + 7 * j + 5 * k
cross product 
= (5 * 5 - 4 * 7) * i 
      + (4 * 2 - 3 * 5) * j + (3 * 7 - 5 * 2) * k
= (-3)*i + (-7)*j + (11)*k
Example –

Input: vect_A[] = {3, -5, 4}
        vect_B[] = {2, 6, 5}
Output: Dot product: -4
         Cross product = -49 -7 28
         

Time Complexity: O(n)
Space Complexity: constant space 
"""

class Solution:
    
    def dotProduct(self,vect1,vect2):
        
        product = 0
        
        for idx in range(0,len(vect1)):
            
            product += vect1[idx] * vect2[idx]
        
        return product
    
    def crossProduct(self,vect1,vect2):
        
        out_list = []
        
        out_list.append((vect1[1] * vect2[2]) - (vect1[2] * vect2[1]))
        out_list.append((vect1[2] * vect2[0]) - (vect1[0] * vect2[2]))
        out_list.append((vect1[0] * vect2[1]) - (vect1[1] * vect2[0]))
        
        return out_list
    


s = Solution()
vect_A = [3, -5, 4]
vect_B = [2, 6, 5]
print(s.dotProduct(vect_A,vect_B))
print(s.crossProduct(vect_A, vect_B))