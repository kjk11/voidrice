# tags: handle bibtex,

# $1 Bibtex entry AS A FILE, NOT STDI

# WORKS, but is kind of ugly
# This script outputs a citation in some readable format
# This is not for use in academic papers, but only for indices I create for myself

#!/bin/bash
key="$(bash "$SCRIPTS/handle_bibtex/extract_key.sh" "$(cat $1)")"
author="$(bash "$SCRIPTS/handle_bibtex/extract_field.sh" "author" "$(cat $1)")"
date="$(bash "$SCRIPTS/handle_bibtex/extract_field.sh" "date" "$(cat $1)")"
if [[ -z $date ]]; then
	date="$(bash "$SCRIPTS/handle_bibtex/extract_field.sh" "year" "$(cat $1)")"
fi
title="$(bash "$SCRIPTS/handle_bibtex/extract_field.sh" "title" "$(cat $1)")"
publisher="$(bash "$SCRIPTS/handle_bibtex/extract_field.sh" "publisher" "$(cat $1)")"

echo "$author ; $date ; $title ; $publisher ; [$key]" 
