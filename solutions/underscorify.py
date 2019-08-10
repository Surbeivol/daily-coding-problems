"""
Write a function that takes in two strigns: a main string and a potential
substring of the main string. The funciton should return a version of the main
string with every instance of the substring in it wrapped between underscores.
If tow instances of the substring in the main string overlap each other or sit
side by side, the underscores relevant to these two substring should only
appear on the far left of the left substring and on the far right of the
right substring. If the main string does not contain the other string at all,
return the main string intact

"""
def underscorify_substring(string, substring):
    # Write your code here.
    
    idx_undersc = collapse_idx(get_locations(string, substring))
    return underscorify(string, idx_undersc)

def get_locations(string, substring):    
    len_sub = len(substring)
    locations  = []
    start_idx = 0
    while start_idx < len(string):
        next_idx = string.find(substring, start_idx)
        if next_idx != -1:            
            locations.append([next_idx, next_idx + len_sub])
            start_idx = next_idx + 1
        else:
            break
    
    return locations
            

def collapse_idx(locations):
    
    if not locations:
        return locations            
    
    new_locations = [locations[0]]    
    previous = new_locations[0]    
    for idx in range(1, len(locations)):
        current = locations[idx]
        if current[0] <= previous[1]:
            previous[1] = current[1]
        else:
            new_locations.append(current)
            previous = current    
    return new_locations
    

def underscorify(string, locations):
    
    str_idx = 0
    loc_idx = 0
    between_under = False
    i = 0
    new_str = []
    while str_idx < len(string) and loc_idx < len(locations):
        pair_loc = locations[loc_idx]
        if str_idx == pair_loc[i]:
            new_str.append('_')
            new_str.append(string[str_idx])
            if not between_under:                
                i = 1 if i == 0 else 0
                between_under = True
            else:
                loc_idx += 1
                between_under = False
                i = 1 if i == 0 else 0
        else:
            new_str.append(string[str_idx])
        str_idx += 1
        
    if str_idx < len(string):
        new_str.append(string[str_idx:])
    elif loc_idx < len(locations):
        new_str.append('_')
    
    return ''.join(new_str)
    
string = "this is a test to see if it works"
substring = "test"
print(underscorify_substring(string, substring))
