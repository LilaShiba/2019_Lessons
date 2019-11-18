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

print(flatten_d(test_dict))