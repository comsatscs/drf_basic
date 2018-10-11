from rest_framework.response import Response
from rest_framework.views import status


def validate_request_employee(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        title = args[0].request.data.get("name", "")
        artist = args[0].request.data.get("designation", "")
        if not title and not artist:
            return Response(
                data={
                    "message": "Both name and designation are required to add a employee"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated