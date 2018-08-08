# es_2x_type_remove

Elasticsearch 2.x 버젼에서 index 이하의 특정 type만 삭제 하는 기능으로 단순하게 bulk를 이용하여 삭제한다.<br />
~~~es 2.x 에서는 type만 삭제하는 기능이 제공 되지 않는다.~~~

## 언어 및 환경
 - Python 2.7.x
 - Linux 환경에서 동작

## 환경 

runner.sh 에서 index와 type를 수정 한다.
~~~
# 13 Line
curl -s -XPOST localhost:9200/index/type/_bulk --data-binary "@id_list.json" > /dev/null
~~~

EsDeleteByType.py 에서 index와 type를 수정한다.
~~~
# 7~8 Line
ES_INDEX = "index"
ES_TYPE = "type"
~~~

### 실행
~~~
./runner.sh
~~~


## License

This project is licensed under the GPL License - see the [WIKI-LICENSE](https://en.wikipedia.org/wiki/GNU_General_Public_License) file for details
