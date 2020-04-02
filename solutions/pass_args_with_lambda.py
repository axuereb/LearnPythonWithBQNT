def process_data(data, extra_process=None):
    if extra_process:
        print(extra_process(data))
    else:
        print(data)

def make_upper(data):
    return data.upper()

def reverse(data, start, end):
    
    return data[:start] + data[end-1:start-1:-1] + data[end:] 

process_data([1,2,3,4,5], extra_process=lambda x: reverse(x,2,4))