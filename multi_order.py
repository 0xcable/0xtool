import requests
import json
import time
from pystyle import *
from pygments import highlight, lexers, formatters
import os
import random
import signal
import os
import requests
import json
from pystyle import *
from pygments import highlight, lexers, formatters
import os
from datetime import datetime, timedelta
import hmac
import hashlib
import redis








def handler(signum, frame):
    print("Relancement du tool")
    os.system("python multi_order.py")  # Remplacez "multi_order.py" par le nom de votre fichier si nécessaire

# Associer le signal SIGINT (Ctrl+C) au gestionnaire de signal
signal.signal(signal.SIGINT, handler)


os.system('cls')



def send_likes(api_key1, link, quantity):
    api_key1 = "9320bd30991779e6723437125e2adbad"
    service_id = 941
    url = f"https://addsmm.com/api/v2?action=add&service={service_id}&link={link}&quantity={quantity}&key={api_key1}"

    response = requests.get(url)

    if response.status_code == 200:
        print(Colorate.Diagonal(Colors.red_to_green, "Les abonnés ont bien été envoyés "))
    else:
        print(Colorate.Diagonal(Colors.red_to_black, "Une erreur s'est produite lors de l'envoi des likes."))

def is_api_key_valid(api_key):
    url = f"https://zefame.com/api/v2?key={api_key}&action=balance"
    headers = {'Authorization': 'Bearer ' + api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return True
    else:
        return False

banner = """
        ╦══╩══════════════0══════════════════╩══╦
     ▄▄ ·  ▄▄▄· ▄▄· ▐▄• ▄  ▄▄·  ▄▄▄· ▄▄▄▄· ▄▄▌  ▄▄▄ .
    ▐█ ▀. ▐█ ▄█▐█ ▌▪ █▌█▌▪▐█ ▌▪▐█ ▀█ ▐█ ▀█▪██•  ▀▄.▀·
    ▄▀▀▀█▄ ██▀·██ ▄▄ ·██· ██ ▄▄▄█▀▀█ ▐█▀▀█▄██▪  ▐▀▀▪▄
     █▄▪▐█▐█▪·•▐███▌▪▐█·█▌▐███▌▐█ ▪▐▌██▄▪▐█▐█▌▐▌▐█▄▄▌
     ▀▀▀▀ .▀   ·▀▀▀ •▀▀ ▀▀·▀▀▀  ▀  ▀ ·▀▀▀▀ .▀▀▀  ▀▀▀ 
        ╩══╦══════════════0══════════════════╦══╩
 ╔═════════╩═════════════════════════════════╩═════════╗
"""

print(Colorate.Diagonal(Colors.red_to_yellow, banner))

menu_choice = input(Colorate.Diagonal(Colors.red_to_yellow, 
"""
        ╦══╩══════════════0══════════════════╩══╦
        ╩═       [1] View Tiktok               ═╩
                 [2] Likes Tiktok [version utilisateur]                             
                 [3] Telegram Post View [version utilisateur]
                 [4] Twitter Tweet Views [version utilisateur]
                 [5] like instagram [version utilisateur]
                 [6] follow instagram [bientot]
                 [7] instagram canal member [bientot]
        ╦═                                     ═╦
        ╩══╦══════════════0══════════════════╦══╩
                        
[?] Choose an option: """))



# ... (votre code existant jusqu'au début du choix de menu)

if menu_choice == '1':
    api_key_file_path = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le chemin du fichier contenant les clés API : "))
    links_file_path = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le chemin du fichier contenant les liens TikTok : "))
    quantity = 1000
    service_id = 367

    with open(api_key_file_path, "r") as api_key_file:
        api_keys = [line.strip() for line in api_key_file]

    with open(links_file_path, "r") as links_file:
        links = [line.strip() for line in links_file]

    success_count = 0
    error_count = 0
    view_add = 0
    delay = random.randint(50, 105)  # Délai aléatoire entre 2 et 5 minutes

    api_index = 0
    link_index = 0

    while True:
        api_key = api_keys[api_index]
        link1 = links[link_index]
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        print(Colorate.Diagonal(Colors.purple_to_red, f"\nUtilisation de la clé API : {api_key}"))
        print(Colorate.Diagonal(Colors.purple_to_red, f"\nLien TikTok en cours : {link1}"))

        print(Colorate.Diagonal(Colors.white_to_blue, f"\nStatistique de votre compte:\n\nValidation de commande : {success_count}\nErreur/Changement : {error_count}\nVues totals : {view_add}"))
        response = requests.get(url1)
        data = response.json()
        if data == {'error': 'error.incorrect_service_id'}:
            error_count += 1
            print(Colorate.Diagonal(Colors.blue_to_black, '\nChangement du service id...'))
            params = {
                "key": api_key,
                "action": "services"
            }
            response_services = requests.get(url1, params=params)
            services = response_services.json()
            for service in services:
                category = service.get("category")
                if category == 'Services gratuits':
                    service_id = service.get("service")
                    break
            url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        elif data == {'error': 'neworder.error.link_duplicate'}:
            print(Colorate.Diagonal(Colors.yellow_to_green, '\nEn attente de validation de la commande...'))
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
            link_index = (link_index + 1) % len(links)
        elif data == {'error': 'Invalid API key'}:
            print(Colorate.Diagonal(Colors.red_to_black, '\n Votres Clés Personnel est plus valide'))
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
            link_index = (link_index + 1) % len(links)
        else:
            success_count += 1; view_add += 1000*2
            print(Colorate.Diagonal(Colors.green_to_cyan, f"\nValidation, Les {quantity} vues ont bien été envoyés\nNouvelle commande en preparation merci de patientez {delay} second..."))
            link_index = (link_index + 1) % len(links)  # Passer au lien TikTok suivant
            api_index = (api_index + 1) % len(api_keys)




if menu_choice == '2':
    api_key_file_path = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le chemin du fichier contenant les clés API : "))
    links_file_path = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le chemin du fichier contenant les liens TikTok : "))
    quantity = 10
    service_id = 429

    with open(api_key_file_path, "r") as api_key_file:
        api_keys = [line.strip() for line in api_key_file]

    with open(links_file_path, "r") as links_file:
        links = [line.strip() for line in links_file]

    success_count = 0
    error_count = 0
    view_add = 0
    delay = random.randint(50, 105)  # Délai aléatoire entre 2 et 5 minutes

    api_index = 0
    link_index = 0

    while True:
        api_key = api_keys[api_index]
        link1 = links[link_index]
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        print(Colorate.Diagonal(Colors.purple_to_red, f"\nUtilisation de la clé API : {api_key}"))
        print(Colorate.Diagonal(Colors.purple_to_red, f"\nLien TikTok en cours : {link1}"))

        print(Colorate.Diagonal(Colors.white_to_blue, f"\nStatistique de votre compte:\n\nValidation de commande : {success_count}\nErreur/Changement : {error_count}\nVues totals : {view_add}"))
        response = requests.get(url1)
        data = response.json()
        if data == {'error': 'error.incorrect_service_id'}:
            error_count += 1
            print(Colorate.Diagonal(Colors.blue_to_black, '\nChangement du service id...'))
            params = {
                "key": api_key,
                "action": "services"
            }
            response_services = requests.get(url1, params=params)
            services = response_services.json()
            for service in services:
                category = service.get("category")
                if category == 'Services gratuits':
                    service_id = service.get("service")
                    break
            url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        elif data == {'error': 'neworder.error.link_duplicate'}:
            print(Colorate.Diagonal(Colors.yellow_to_green, '\nEn attente de validation de la commande...'))
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
        elif data == {'error': 'Invalid API key'}:
            print(Colorate.Diagonal(Colors.red_to_black, '\n Votres Clés Personnel est plus valide'))
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
            link_index = (link_index + 1) % len(links)
        else:
            success_count += 1; view_add += 50
            print(Colorate.Diagonal(Colors.green_to_cyan, f"\nValidation, Les {quantity} likes ont bien été envoyés\nNouvelle commande en preparation merci de patientez {delay} second..."))
            time.sleep(1)
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
            link_index = (link_index + 1) % len(links)  # Passer au lien TikTok suivant





if menu_choice == '3':
    api_key_file_path = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le chemin du fichier contenant les clés API : "))
    links_file_path = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le chemin du fichier contenant les liens TikTok : "))
    quantity = 1000
    service_id = 369

    with open(api_key_file_path, "r") as api_key_file:
        api_keys = [line.strip() for line in api_key_file]

    with open(links_file_path, "r") as links_file:
        links = [line.strip() for line in links_file]

    success_count = 0
    error_count = 0
    view_add = 0
    delay = random.randint(50, 105)  # Délai aléatoire entre 2 et 5 minutes

    api_index = 0
    link_index = 0

    while True:
        api_key = api_keys[api_index]
        link1 = links[link_index]
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        print(Colorate.Diagonal(Colors.purple_to_red, f"\nUtilisation de la clé API : {api_key}"))
        print(Colorate.Diagonal(Colors.purple_to_red, f"\nLien Telegram en cours : {link1}"))

        print(Colorate.Diagonal(Colors.white_to_blue, f"\nStatistique de votre compte:\n\nValidation de commande : {success_count}\nErreur/Changement : {error_count}\nVues totals : {view_add}"))
        response = requests.get(url1)
        data = response.json()
        if data == {'error': 'error.incorrect_service_id'}:
            error_count += 1
            print(Colorate.Diagonal(Colors.blue_to_black, '\nChangement du service id...'))
            params = {
                "key": api_key,
                "action": "services"
            }
            response_services = requests.get(url1, params=params)
            services = response_services.json()
            for service in services:
                category = service.get("category")
                if category == 'Services gratuits':
                    service_id = service.get("service")
                    break
            url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        elif data == {'error': 'neworder.error.link_duplicate'}:
            print(Colorate.Diagonal(Colors.yellow_to_green, '\nEn attente de validation de la commande...'))
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
        elif data == {'error': 'Invalid API key'}:
            print(Colorate.Diagonal(Colors.red_to_black, '\n Votres Clés Personnel est plus valide'))
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
            link_index = (link_index + 1) % len(links)
        else:
            success_count += 1; view_add += 1000*2
            print(Colorate.Diagonal(Colors.green_to_cyan, f"\nValidation, Les {quantity} vues ont bien été envoyés\nNouvelle commande en preparation merci de patientez {delay} second..."))
            time.sleep(1)
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
            link_index = (link_index + 1) % len(links)  # Passer au lien TikTok suivant



if menu_choice == '4':
    api_key_file_path = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le chemin du fichier contenant les clés API : "))
    links_file_path = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le chemin du fichier contenant les liens TikTok : "))
    quantity = 1000
    service_id = 368

    with open(api_key_file_path, "r") as api_key_file:
        api_keys = [line.strip() for line in api_key_file]

    with open(links_file_path, "r") as links_file:
        links = [line.strip() for line in links_file]

    success_count = 0
    error_count = 0
    view_add = 0
    delay = random.randint(50, 105)  # Délai aléatoire entre 2 et 5 minutes

    api_index = 0
    link_index = 0

    while True:
        api_key = api_keys[api_index]
        link1 = links[link_index]
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        print(Colorate.Diagonal(Colors.purple_to_red, f"\nUtilisation de la clé API : {api_key}"))
        print(Colorate.Diagonal(Colors.purple_to_red, f"\nLien twitter en cours : {link1}"))

        print(Colorate.Diagonal(Colors.white_to_blue, f"\nStatistique de votre compte:\n\nValidation de commande : {success_count}\nErreur/Changement : {error_count}\nVues totals : {view_add}"))
        response = requests.get(url1)
        data = response.json()
        if data == {'error': 'error.incorrect_service_id'}:
            error_count += 1
            print(Colorate.Diagonal(Colors.blue_to_black, '\nChangement du service id...'))
            params = {
                "key": api_key,
                "action": "services"
            }
            response_services = requests.get(url1, params=params)
            services = response_services.json()
            for service in services:
                category = service.get("category")
                if category == 'Services gratuits':
                    service_id = service.get("service")
                    break
            url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        elif data == {'error': 'neworder.error.link_duplicate'}:
            print(Colorate.Diagonal(Colors.yellow_to_green, '\nEn attente de validation de la commande...'))
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
        elif data == {'error': 'Invalid API key'}:
            print(Colorate.Diagonal(Colors.red_to_black, '\n Votres Clés Personnel est plus valide'))
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
            link_index = (link_index + 1) % len(links)
        else:
            success_count += 1; view_add += 1000*2
            print(Colorate.Diagonal(Colors.green_to_cyan, f"\nValidation, Les {quantity} vues ont bien été envoyés\nNouvelle commande en preparation merci de patientez {delay} second..."))
            time.sleep(1)
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
            link_index = (link_index + 1) % len(links)  # Passer au lien TikTok suivant


if menu_choice == '5':
    api_key_file_path = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le chemin du fichier contenant les clés API : "))
    links_file_path = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le chemin du fichier contenant les liens TikTok : "))
    quantity = 30
    service_id = 371

    with open(api_key_file_path, "r") as api_key_file:
        api_keys = [line.strip() for line in api_key_file]

    with open(links_file_path, "r") as links_file:
        links = [line.strip() for line in links_file]

    success_count = 0
    error_count = 0
    view_add = 0
    delay = random.randint(50, 105)  # Délai aléatoire entre 2 et 5 minutes

    api_index = 0
    link_index = 0

    while True:
        api_key = api_keys[api_index]
        link1 = links[link_index]
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        print(Colorate.Diagonal(Colors.purple_to_red, f"\nUtilisation de la clé API : {api_key}"))
        print(Colorate.Diagonal(Colors.purple_to_red, f"\nLien en cours : {link1}"))


        print(Colorate.Diagonal(Colors.white_to_blue, f"\nStatistique de votre compte:\n\nValidation de commande : {success_count}\nErreur/Changement : {error_count}\nVues totals : {view_add}"))
        response = requests.get(url1)
        data = response.json()
        if data == {'error': 'error.incorrect_service_id'}:
            error_count += 1
            print(Colorate.Diagonal(Colors.blue_to_black, '\nChangement du service id...'))
            params = {
                "key": api_key,
                "action": "services"
            }
            response_services = requests.get(url1, params=params)
            services = response_services.json()
            for service in services:
                category = service.get("category")
                if category == 'Services gratuits':
                    service_id = service.get("service")
                    break
            url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={api_key}"
        elif data == {'error': 'neworder.error.link_duplicate'}:
            print(Colorate.Diagonal(Colors.yellow_to_green, '\nEn attente de validation de la commande...'))
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
            link_index = (link_index + 1) % len(links)  # Passer au lien TikTok suivant
        elif data == {'error': 'Invalid API key'}:
            print(Colorate.Diagonal(Colors.red_to_black, '\n Votres Clés Personnel est plus valide'))
            api_index = (api_index + 1) % len(api_keys)  # Passer à la clé API suivante
            link_index = (link_index + 1) % len(links)
        else:
            success_count += 1; view_add += 50
            print(Colorate.Diagonal(Colors.green_to_cyan, f"\nValidation, Les {quantity} likes ont bien été envoyés\nNouvelle commande en preparation merci de patientez {delay} second..."))
            time.sleep(0.1)
            link_index = (link_index + 1) % len(links)  # Passer au lien TikTok suivant


if menu_choice == '6':
    last_usage_time = load_last_usage_time(redis_client, ip_saisie)  
    if last_usage_time is None or is_allowed_to_use(datetime.fromisoformat(last_usage_time)):
        
        
    
       last_usage_time = datetime.now().isoformat()
       save_last_usage_time(redis_client, ip_saisie, last_usage_time)
       link = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le lien du profil Instagram : "))
       quantity = 10
       api_key1 = "9320bd30991779e6723437125e2adbad"
       send_likes(api_key1, link, quantity)
    else:
        print("la commande charge encore , vueillez attendre au maximum 24h")
    
    
