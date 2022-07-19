import html
from django.http import HttpResponse

from .models import Pokemon

def get_pokemon(request,pokemon_id):
    pokemon=Pokemon.objects.get(id=pokemon_id)
    show_poke=(f"""<p>{pokemon.name}</p> \n
               <p>{pokemon.type}</p>\n
              <p> {pokemon.hp}</p>\n
               {pokemon.name_ar}""")
        
    return HttpResponse (show_poke)
