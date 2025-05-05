from fastapi import APIRouter, HTTPException
router = APIRouter()


@router.post("/query")
async def query_handler():
    try:


        return {"message":"heelo world"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    

