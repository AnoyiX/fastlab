from fastlab.models import Response, PageData


# Web base repsonse
print(Response(data='hello'))                                   # >>> {"code": 0, "message": "", "data": "hello"}
print(Response(code=10000, message='server error', data={}))    # >>> {"code": 10000, "message": "server error", "data": {}}


# Web pageable data: skip=0 limit=20 total=100 has_more=True data=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(PageData(skip=0, limit=20, total=100, has_more=True, data=list(range(0, 20))))    
