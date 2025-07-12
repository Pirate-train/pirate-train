from django.shortcuts import render, get_object_or_404
from .models import Game, MemoryOffset, Pointer, Trainer

def index(request):
    games = Game.objects.all().order_by('title')
    latest_trainers = Trainer.objects.filter(is_approved=True).order_by('-upload_date')
    return render(request, 'index.html', {
        'games': games,
        'latest_trainers': latest_trainers
    })

def game_list(request):
    games = Game.objects.all().order_by('title')
    return render(request, 'game_list.html', {'games': games})

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)

    offsets = game.offsets.all()
    pointers = game.pointers.all()
    trainers = game.trainers.filter(is_approved=True)
    
    features = None
    if trainers.exists():
        trainer = trainers.first()
        features = {
            'raw': trainer.features,
            'lines': [line.strip() for line in trainer.features.split('\n') if line.strip()]
        }

    return render(request, 'game_detail.html', {
        'game': game,
        'offsets': offsets,
        'pointers': pointers,
        'trainers': trainers,
        'features': features
    })

def search(request):
    query = request.GET.get('q', '')
    games = Game.objects.filter(title__icontains=query)
    offsets = MemoryOffset.objects.filter(description__icontains=query)
    pointers = Pointer.objects.filter(description__icontains=query)
    
    return render(request, 'search_results.html', {
        'query': query,
        'games': games,
        'offsets': offsets,
        'pointers': pointers
    })