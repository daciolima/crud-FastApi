from fastapi import APIRouter, status


routes_home = APIRouter()


@routes_home.get('/', status_code=status.HTTP_200_OK, tags=["Home"])
async def index():
    """ endpoint Home """
    return {"data": {"message": "Blog Index"}}