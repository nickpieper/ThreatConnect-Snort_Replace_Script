# [INSERT SID HERE]
# Take input like "{script name} new.rules 1000 1005" from command line
# Replace the '[INSERT SID HERE]' lines in my rules_file.txt with my range created (1000..1005) with numbers from cmd line.
# Example command: python tc_snort_replace.py new.rules 1000 1005 
# This replaces the 4 rules in your 'new.rules' file that have an '[INSERT SID HERE]' with sid numbers 100 to 104. 


import fileinput
import sys

rule_file = sys.argv[1]
myinput = open(rule_file, "rt")
myoutput = open("new_rules.txt", "wt")



for sig in range(int(sys.argv[2]),int(sys.argv[3])):
        sig = str(sig)
        for line in myinput:            
            myoutput.write(line.replace('[INSERT SID HERE]', sig, 1))
            break
