#!/bin/sh

export HOWDOI_DISABLE_CACHE="donotwant"

printf_input=$(echo "$@" | sed "s/+/ /g" | sed "s/%/\\\\x/g")

query=$(printf "%b" "$printf_input")

answer=$(howdoi "$query")

printf "%s\n\n" "Content-type: text/plain"
printf "%s\n\n" "howdoi $query ?"
printf "%s\n" "$answer"


