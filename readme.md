curl -X POST https://konbert.com/api/v1/convert \
	-H "Authorization: Bearer ${API_KEY}" \
	-d "input[file]=@myfile.json" \
	-d "input[format]=json" \
	-d "input[options][flatten_objects]=true" \
	-d "output[format]=avro" \
	-d "output[options][only_schema]=false"