dev:
	pbpaste | tr " " "\n" | sort | uniq > data/output.txt
