from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def hello_my_root():
    return {"Hello": "Strange World"}


@router.get("/items/{item_id}")
async def read_item_id(item_id: int):
    return {"items_id": item_id}


@router.get("/users/{user_name}")
async def greeting_user(user_name: str):
    return {"Hello": user_name}


@router.get("/users/{user_name}/bilio")
async def user_biblio(user_name: str, bib_info: str | None = None):
    if bib_info:
        return {"user": user_name, "biblio": bib_info}
