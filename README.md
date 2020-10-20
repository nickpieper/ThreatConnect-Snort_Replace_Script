# ThreatConnect-Snort Replace Script
Takes a list of Snort rules from ThreatConnect and replaces all of the '[INSERT SID HERE]' string with a given range of numbers. 

# Example
python tc_snort_replace.py new.rules 1000 1005

This replaces the 4 rules in your 'new.rules' file that have an '[INSERT SID HERE]' with sid numbers 100 to 104. Remember that a range excludes the last number which in our case is 105.

Note that if you had 20 rules in your new.rules file, and your range was '1000 1050' it will fill out all of the strings without erroring out.

# Warning
It is recommended to not run this script on your production Snort rules file (unless you're daring).
