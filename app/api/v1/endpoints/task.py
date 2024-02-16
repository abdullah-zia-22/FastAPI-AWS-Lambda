from fastapi import APIRouter

router = APIRouter()


@router.get("/list")
async def list():
    """
    Get Tasks 
    """
    return {"status":"success","data":[{"name":"Test"}]}
    
