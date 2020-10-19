# [INSERT SID HERE]
# Take input like "{script name} new.rules 1000 1005" from command line
# Replace the '[INSERT SID HERE]' lines in my rules_file.txt with my range created (1000..1005) with numbers from cmd line.
# Example command: python replace.py new.rules 1000 1005 

####################
# Example lines:
#alert tcp any any <> 45.147.230.87 any (msg:"TCP established connection to IP address indicator '45.147.230.87'"; flow:established; reference:url,app.threatconnect.com/auth/indicators/details/address.xhtml?address=45.147.230.87; sid:[INSERT SID HERE]; rev:1;)
#alert udp any 53 -> any any (msg:"DNS Response with IP address 45.147.230.87"; content:"|00 04 2d 93 e6 57|"; sid:[INSERT SID HERE]; rev:1;)

#alert udp any any -> any 53 (msg:"DNS request for host indicator 'backup1nas.com'"; content:"|0a|backup1nas|03|com|00|"; nocase; reference:url,app.threatconnect.com/auth/indicators/details/host.xhtml?host=backup1nas.com; sid:[INSERT SID HERE]; rev:1;)

#alert tcp any any <> 45.147.229.253 any (msg:"TCP established connection to IP address indicator '45.147.229.253'"; flow:established; reference:url,app.threatconnect.com/auth/indicators/details/address.xhtml?address=45.147.229.253; sid:[INSERT SID HERE]; rev:1;)
#####################

import fileinput
import sys

rule_file = sys.argv[1]
myinput = open(rule_file, "rt")
myoutput = open("out.txt", "wt")



for sig in range(int(sys.argv[2]),int(sys.argv[3])):
        sig = str(sig)
        for line in myinput:            
            myoutput.write(line.replace('[INSERT SID HERE]', sig, 1))
            break
