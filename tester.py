import threading, sys, subprocess, os
import requests
import tempfile
from bs4 import BeautifulSoup

from subprocess import PIPE

get_problem_num = input("Number of problem  ")
get_problem_let = input("Letter of problem  ")

url = f'https://codeforces.com/problemset/problem/{get_problem_num}/{get_problem_let}'

Code_force_raw = requests.get(url).text

soup = BeautifulSoup(Code_force_raw,'html.parser')



def input_sections(soup_object):
    in_els = soup.find_all("div", {"class":"input"})

    input_val_array = []

    
    for items in in_els:
        tmp_arr = []
        for pres in items.find_all("pre"):
            for val in pres.get_text():
                if val != '\r':
                    tmp_arr.append(val)

        input_val_array.append(tmp_arr)
                      
    return input_val_array
            

def output_sections(soup_object):
    in_els = soup.find_all("div", {"class":"output"})

    output_val_array = []
    
    
    for items in in_els:
        tmp_arr = []
        for pres in items.find_all("pre"):
            for val in pres.get_text():
                if val != '\r':
                    tmp_arr.append(val)

        output_val_array.append(tmp_arr[1:-1])
                      
    
    return output_val_array        


input_scts = input_sections(soup)
output_sections = output_sections(soup)


print(input_scts) #testing here
print(output_sections) #testing here

def prog_output_function(input_list):
    response_array = []
    index = 0  
    
    for block in input_list: 
        block_result = []
        f = tempfile.TemporaryFile(mode='w+')
      
        
        
        for val in block[1:-1]: 
            f.write(val)
            
        f.seek(0)
   
        user_code= subprocess.Popen(['python', 'test_code.py'], stdin=f, stdout=PIPE)
        user_code.wait()
        mssg = user_code.communicate()
        for val in mssg[0].decode('utf-8').strip():
            if val != '\r':
                block_result.append(val)

        response_array.append(block_result)
    
    print(response_array) #testing here
    return response_array

def matching_phase(program_response, output_divs):
    if program_response==output_divs:
        return True
    else:
        return False
    


print(matching_phase(prog_output_function(input_scts), output_sections))
input("...")


