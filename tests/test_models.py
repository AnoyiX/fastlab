from fastlab.models import Response, PageData


# Web base repsonse
assert Response(data='hello').dict() == {"code": 0, "message": "", "data": "hello"}
assert Response(code=10000, message='server error', data={}) == {"code": 10000, "message": "server error", "data": {}}


# Web pageable data
assert PageData(skip=0, limit=10, total=100, has_more=True, data=list(range(0, 10))) == {"skip": 0 , "limit": 10, "total": 100, "has_more": True, "data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}
