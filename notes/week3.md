# Week 3 API curl communication

1- curl -i -X POST http://127.0.0.1:8000/notes -H "Content-Type: application/json" -d '{"title": "Docker", "body": "namespaces + cgroups"}' :

HTTP/1.1 422 Unprocessable Content
date: Mon, 09 Nov 2026 12:45:02 GMT
server: uvicorn
content-length: 206
content-type: application/json
{"detail":[{"type":"model_attributes_type","loc":["body"],"msg":"Input should be a valid dictionary or object to extract fields from","input":"{\"title\": \"Docker\", \"body\": \"namespaces + cgroups\"}"}]}

2- curl -i http://127.0.0.1:8000/notes/1

HTTP/1.1 404 Not Found
date: Mon, 09 Nov 2026 12:47:25 GMT
server: uvicorn
content-length: 22
content-type: application/json

{"detail":"Not Found"}

3- curl -i http://127.0.0.1:8000/notes/999

HTTP/1.1 404 Not Found
date: Mon, 09 Nov 2026 12:50:27 GMT
server: uvicorn
content-length: 22
content-type: application/json

{"detail":"Not Found"}

4- curl -i -X PATCH http://127.0.0.1:8000/notes/1 -H "Content-Type: application/json" -d '{"title": "Containers"}'

HTTP/1.1 404 Not Found
date: Mon, 09 Nov 2026 12:51:04 GMT
server: uvicorn
content-length: 22
content-type: application/json

{"detail":"Not Found"}

5- curl -i -X POST http://127.0.0.1:8000/notes -H "Content-Type: application/json" -d '{"title": "x", "owner": "admin"}'

HTTP/1.1 422 Unprocessable Content
date: Mon, 09 Nov 2026 12:52:43 GMT
server: uvicorn
content-length: 117
content-type: application/json

{"detail":[{"type":"extra_forbidden","loc":["body","owner"],"msg":"Extra inputs are not permitted","input":"admin"}]}

6- curl -i "http://127.0.0.1:8000/notes?limit=1000"

HTTP/1.1 422 Unprocessable Content
date: Mon, 09 Nov 2026 12:53:04 GMT
server: uvicorn
content-length: 145
content-type: application/json

{"detail":[{"type":"less_than_equal","loc":["query","limit"],"msg":"Input should be less than or equal to 100","input":"1000","ctx":{"le":100}}]}

7- curl -i -X DELETE http://127.0.0.1:8000/notes/1

HTTP/1.1 404 Not Found
date: Mon, 09 Nov 2026 12:53:39 GMT
server: uvicorn
content-length: 22
content-type: application/json

{"detail":"Not Found"}


