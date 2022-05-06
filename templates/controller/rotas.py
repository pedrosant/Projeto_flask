def verif_rota(rota):
    if rota == '/':
        return 'view/index.html'
    if rota == 'logado':
        return 'view/home.html'
    if rota == 'usuario':
        return 'view/usuario.html'
    if rota == 'passageiro':
        return 'view/passageiro.html'
    if rota == 'motorista':
        return 'view/motorista.html'
    if rota == 'veiculos':
        return 'view/veiculos.html'    
