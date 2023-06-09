from fastapi import APIRouter, Depends
from schemas.drum import Drum, DrumResponseModel
from database.dataset import drumDataBase
from database.connection import get_db
from database.models import Drum as DrumTableModel
from sqlalchemy.orm import Session

router = APIRouter(prefix = "/drums", tags=["drums"])

@router.post("/")
def addDrum(drum: Drum, db: Session = Depends(get_db)):
    drumData = DrumTableModel(title=drum.title, description = drum.description)
    db.add(drumData)
    db.commit()
    db.refresh(drumData)
    # drumDataBase.append(drum.dict())
    # return {"data": drumDataBase}
    return {"data": drumData}

# @router.get("/", response_model=list[DrumResponseModel])
# def getDrums(db: Session = Depends(get_db)):
#     drums = db.query(DrumTableModel).all()
#     return drums


    # return {"data": drumDataBase}

@router.get("/{drumName}")
def getSpecificDrum(drumName: str, db: Session = Depends(get_db)):
    drum = db.query(DrumTableModel).filter(DrumTableModel.title.ilike(f"%{drumName}")).first();
    if drum:
        return {"data": drum}
    # for drum in drumDataBase:
    #     if (drum["name"] == drumName.lower()):
    #         return drum
    return {"message": "found nothing"}

@router.delete("/{drumId}")
def deleteDrum(drumId: int):
    # for drum in drumDataBase:
    #     if drum["id"] == drumId:
    #         drumDataBase.remove(drum)
    #         return {"data": drumDataBase}
    newSet = [drum for drum in drumDataBase if drum["id"] != drumId]
    return {"data": newSet}

