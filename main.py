from fastapi import FastAPI,Query,Path
from models.animals import animals
from models.login import login
from models.race import race
from models.species import species
from models.userdatacomplete import userdatacomplete
from database import conn #importo la base de datos para luego realizar consultas con los endpoints
from routers import animalsrouter,loginrouter,racerouter,speciesrouter,userdatacompleterouter

app=FastAPI()  # create app

app.include_router(animalsrouter.router)
app.include_router(loginrouter.router)
app.include_router(speciesrouter.router)
app.include_router(racerouter.router)
app.include_router(userdatacompleterouter.router) #que la app te incluya las rutas (endpoints)en routers.
animals=[{
    'id':'1',
    'age':20,
    'hair_color':'brown',
    'eyes_color':'blue',
    'weight':15,
    'character':'good',
    'disabilities':'healthy',
    'size':'big',
    'diseases':'no'
    
},
{
      'id':'2',
      'age':3,
      'hair_color':'blondie',
      'eyes_color':'brown',
      'weight':10,
      'character':'calm ',
      'disabilities':'yes,deaf', 
      'size':'small',
      'diseases':'no'     
}     
  ]
login=[{
    'email':'micaelacorolaire@gmail.com',
    'password':'harrypotter',
    'numberphone':1523131387,
    'name':'micaela'
}]
race=[{
    'name':'doberman'
}]
species=[{
    'name':'sarasa'
}]
userdatacomplete=[{
    'name':'sabrina',
    'lastname':'corolaire',
    'email':'cororlaires@gmail.com.ar',
    'numberphone':1523131387,
    'otherphone':5467,
    'age':34,
    'where_live':'arizona'
}]

@app.get('/')
def message():
    return 'WELCOME TO PETS PAGE , YOU WILL FIND YOUR PERFECT ANIMAL  '



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port=8000)
    





