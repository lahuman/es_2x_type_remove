#!/bin/bash

FILESIZE=$(stat -c%s "id_list.json")
echo "Size $FILESIZE"

while [ $FILESIZE -gt 0 ]; do

python EsDeleteByType.py

echo "Binary Data Gen"
sleep 1

curl -s -XPOST localhost:9200/index/type/_bulk --data-binary "@id_list.json" > /dev/null

echo "REMOVED"
sleep 1

done