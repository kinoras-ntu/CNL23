build:
	docker build -t profon9 . --no-cache
run:
	docker run -it --name junox --privileged -p 9025:25 -p 9080:80 -p 9110:110 \
		-p 9143:143 -p 9465:465 -p 9587:587 -p 9993:993 -p 9995:995 profon9
clean:
	docker rm junox
	docker rmi profon9

