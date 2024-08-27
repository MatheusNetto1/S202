from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
# db.resetDatabase()

# Busca 1: busca pelo Rattata
#def getPokemonByName(name: str):
#    return db.collection.find({"name": name})

#rattata = getPokemonByName("Rattata")
#writeAJson(rattata, "Rattata")
#--------------------------------------------------

# Busca 2: busca por pokemon do tipo normal sem multiplicador com apenas 1 fraqueza
#tipos = ["Normal"]
#pokemons = db.collection.find({ "type": {"$in": tipos}, "multipliers": None, "weaknesses": {"$size": 1} })
#writeAJson(pokemons, "Normal sem multiplicador com apenas 1 fraqueza")
#--------------------------------------------------

# Busca 3: busca por pokemon fraco contro grama ou gelo com apenas 1 fraqueza com chance de spawn entre 0.05 e 0.15
#fraquezas = ["Grass", "Ice"]
#pokemons = db.collection.find({ "weaknesses": {"$in": fraquezas}, "weaknesses": {"$size": 1}, "spawn_chance": {"$gt":0.05, "$lt": 0.15} })
#writeAJson(pokemons, "Fraco contro grama ou gelo com apenas 1 fraqueza com chance de spawn entre 0.05 e 0.15")
#--------------------------------------------------

# Busca 4: busca por pokemon do tipo dragão ou fogo que não tenha mais evolução
#tipos = ["Dragon", "Fire"]
#pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": False} })
#writeAJson(pokemons, "Dragão ou fogo sem evolução")
#--------------------------------------------------

# Busca 5: busca por pokemon do tipo bug e poison com fraqueza de água ou fogo sem evolução com chance de spawn maior que 0.06
#tipos = ["Bug", "Poison"]
#fraquezas = ["Water", "Fire"]
#pokemons = db.collection.find({"type": {"$all": tipos}, "weaknesses": {"$in": fraquezas}, "next_evolution": {"$exists": False},  "spawn_chance": {"$gte": 0.06} })
#writeAJson(pokemons, "Bug e poison com fraqueza de água ou fogo sem evolução com chance de spawn maior que 0.06")