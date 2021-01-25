#! /bin/bash
i=0
while  ((i<=10))
do
	python3 /home/rishu/Desktop/spam.py &
	pkill zoom &

done
echo "exit"
