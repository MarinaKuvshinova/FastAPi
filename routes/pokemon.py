from fastapi import APIRouter, Depends, UploadFile, File
from schemas.pokemon import Pokemon, PokemonResponseModel, PokemonState, PokemonStateResponseModel
from database.connection import get_db
from database.models import Pokemon as PokemonTableModel, PokemonStats as StatesTableModel
from sqlalchemy import select
from sqlalchemy.orm import Session, subqueryload, load_only
from helpers.filehandling import uploadCSVFileToPokemonDatabase, uploadCSVFileToPokemonStatsDatabase

router = APIRouter(prefix = "/pokemons", tags=["pokemons"])

@router.get("/")
def getPokemons(db: Session = Depends(get_db)):
    pokemons = db.query(PokemonTableModel).options(subqueryload(PokemonTableModel.stats)).all()
    return pokemons
    
@router.get("/name/{pokemonName}")
def getSpecificDrum(pokemonName: str, db: Session = Depends(get_db)):
    pokemon = db.query(PokemonTableModel).options(subqueryload(PokemonTableModel.stats)).filter(PokemonTableModel.name.ilike(f"%{pokemonName}%")).first()
    print(pokemon)
    if pokemon:
        return {"data": pokemon}
    return {"message": "found nothing"} 


@router.get("/id/{pokemonId}")
def getPokemonById(pokemonId: int, db: Session = Depends(get_db)):
    pokemon = db.query(PokemonTableModel).options(subqueryload(PokemonTableModel.stats)).filter(PokemonTableModel.id == pokemonId).first()
    if pokemon:
        return {"data": pokemon}
    return {"message": "found nothing"} 
















@router.post("/uploadfile/")
def create_upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # uploadCSVFileToPokemonDatabase(file, db)
    uploadCSVFileToPokemonStatsDatabase(file, db)