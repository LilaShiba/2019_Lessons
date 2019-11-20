test_dict = {'geeks': 
                {'Geeks': 
                    {'for': 7}
                }, 
            'for': 
                {'geeks': 
                    {'Geeks': 3}
                }, 
            'Geeks': 
                {'for': 
                    {'for': 1, 'geeks': 4}
                }
            } 
  

def flatten_d(dd, sep='.'):
    ans = {}
    for key,value in dd.items():
        if isinstance(value, dict):
            flatten_values = flatten_d(value)
            for fkey, fvalue in flatten_values.items():
                ans[key + sep + fkey] = fvalue
        else:
            ans[key] = value
    return ans
    
def flatten_dd(dd, sep='.'):
    ans = {}
    for key,value in dd.items():
        if type(value) is dict:
            ans = make_flat(key, value, ans)
        else:
            ans[key] = value
    return ans

def make_flat(key, val, ans):
    for fkey, fvalue in val.items():
        if type(fvalue) is dict:
            new_key = key + '.' + fkey
            ans = make_flat(new_key, fvalue, ans)
        else:
            ans[key + '.' + fkey] = fvalue
    return ans

print(flatten_dd(test_dict))
print(flatten_d(test_dict))

