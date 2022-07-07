#! /bin/bash
declare -i k=1
for i in {5..1}
do
        rem=$(($i % 2))
        if [ "$rem" -ne "0" ]; then
                while [ "$k" -le "$i" ]
					do
						printf "*"
						((i--))
					done
			echo""
        fi
done
$SHELL
