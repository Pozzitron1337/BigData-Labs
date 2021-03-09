#!/bin/sh
query=$1
src=$2
source="Source"

if [ "$src" = "$source" ]; then
    curl -X GET 'http://localhost:9200/_all/_search?pretty=true&size=20' -H 'Content-Type:application/json' -d '
    {
        "query": 
        {
            "bool": 
            {
                "must": 
                    [
                        {
                            "multi_match": 
                            {
                                "query": "'$query'",
                                "fields": ["textBody", "title"]
                            }
                        }
                    ]
            }
        }
    }' | ./cgi-bin/prog2.py 
else
    curl -X GET 'http://localhost:9200/_all/_search?pretty=true&size=20' -H 'Content-Type:application/json' -d '
    {
        "query": 
        {
            "bool": 
            {
                "must": 
                    [
                        {
                            "multi_match": 
                            {
                                "query": "'$query'",
                                "fields": ["textBody", "title"]
                            }
                        }
                    ],
                "filter": 
                    [
                        {
                            "match":
                            {
                                "source": "'$src'"
                            }
                        }
                    ]
            }
        }
    }' | ./cgi-bin/prog2.py 
fi
