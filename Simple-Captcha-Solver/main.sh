i=0

rm -f log.txt

while [ $i -le 1000 ]
do 
	curl http://query.bjeea.cn/captcha.jpg 1> $i.jpg 2>> log.txt
	echo Picture $i
	((i++))
	sleep 0.1
done
