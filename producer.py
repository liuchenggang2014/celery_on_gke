from app.tasks import *

print(add(1,2))
r=reverse.delay("cliu")
print(r.status)