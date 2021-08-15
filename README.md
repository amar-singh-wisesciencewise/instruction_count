# instruction_count
This is a script to read the assembly file produced while compiling and count how many times any instruction has been used

How to produce assembly file with GCC:  
gcc -S file.c  
Above command will produce file.s asssembely file along with executable 

how to use this python script:  
python instruction_count.py file.s  
