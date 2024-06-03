


import os

global output
output = []

print()
print()




def show_output_line():
    os.system('cls')
    output_reversed = output.copy()
    output_reversed.reverse()
    print("kolejka")
    print(output_reversed)
    print()
    print("podaj liczbę input: ")




    





for i in range(5):

    
    show_output_line()
    rece = input()
    if rece == '0':
        continue
    output.append(rece)

show_output_line()

    
