# tags: handle bibtex,

# This is not integrated into the actual shell script yet

# Delete all lines, which do not contain an @
/\@/!d
# Extract what lies between { and , with regex
s/.*{\(.*\),.*/\1/
