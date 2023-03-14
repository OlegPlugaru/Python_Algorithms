"""
Non repeat element 
Take a string and return character that newer repeats if multiple uniques then return only the first unique
"""
def non_repeating(s):
    s = s.replace(' ', '').lower()

    char_count = {}
    

    for c in s: 
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    # list = []
    # for c in char_count:
    #     if char_count[c] == 1:

    #         list.append(c)
    #     else: 
    #         continue
    # for e in list:    
    #     print(e)

    all_uniques = []
    y = sorted(char_count.items(), key=lambda x: x[1])
    
    for item in y:
        if item[1] == y[0][1]:
            all_uniques.append(item)
    return all_uniques

   

    
    

print(non_repeating('I Apple Ape Peels'))
        