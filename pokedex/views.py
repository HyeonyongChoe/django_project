from django.shortcuts import render, get_object_or_404
from .models import PokedexappPokedex


def index(request):
    pokename = PokedexappPokedex.objects.order_by('num')
    return render(request, 'pokedex/dex.html', {'pokename': pokename})

def detail(request,pokemon_id):
    pokemon = get_object_or_404(PokedexappPokedex, pk = pokemon_id)
    url = pokemon.img
    context = {'pokemon' : pokemon, 'url':url}
    return render(request, 'pokedex/dex_detail.html', context)