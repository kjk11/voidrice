# tags: handle bibtex,

# Field to be extracted is in variable $field
# This sed script is currently not used in the shell script or called in any other shell scripts

/"$field" =/!d
s/.*{\(.*\)}.*/\1/
