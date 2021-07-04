# This script outputs all the tags that exist in a given folder
# First sed command removes lines, which do not contain the word tag
# Second sed command selects the string between the curly brackets
# Third sed command turns commas into new lines
# Fourth sed command removes whitespace before and after whatever is in each line
# Fifth sed command removes empty lines
ls | xargs cat | sed -e '/tags/!d' -e 's/.*{\(.*\)}.*/\1/' -e 's/,/\n/g' | sed -e 's/\s*\(\)\s*/\1/' -e '/^$/d' | sort | uniq
