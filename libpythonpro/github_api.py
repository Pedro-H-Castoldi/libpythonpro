import requests


def buscar_avatar(usuario):
    """
    Busca avatar do usuário no Github
    :param usuario: str com o nome do usuário no Github
    :return: str com o link do avattar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('Pedro-H-Castoldi'))
