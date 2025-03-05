# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# if the word has space, replace it with '%20'

'''
<span class="ryNqvb"
jsname="W297wb"
jsaction="click:PDNqTc,GFf3ac,qlVvte;contextmenu:Nqw7Te,QP7LD;
mouseout:Nqw7Te;
mouseover:PDNqTc,c2aHje">

pas maintenant et</span>
'''


# https://translate.google.ca/?sl=en&tl=fr-CA&text=not%20now%20%26amp%3B&op=translate       :eng to francais
# https://translate.google.ca/?sl=fr-CA&tl=en&text=pas%20maintenant%20et&op=translate       :francais to eng
# ---------------->


# https://www.google.com/search?sca_esv=1a2a07081c7891bb&rlz=1C1CHBF_enCA967CA967&sxsrf=AHTn8zqamyzpZJZ8iFkouYZJQMYqyRe4rQ:1741158915743&q=lentilles&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBsxayPSIAqObp_AgjkUGqengxVrJ7hrmYmz7X2OZp_NIYfhIAjPnSJLO3GH6L0gKvsMx863yWAECACzcq28K_xbJJoPcSEvdLSYBoilrVRznyvhgudvug19AweeEbrCGkt1-WOOEb9EGKHZMjwGgxB85lVM932Nv9pb4lgel1ps0RGcIKA&sa=X&ved=2ahUKEwiPnK61svKLAxVyvokEHTjYFOIQtKgLegQIERAB&biw=1920&bih=953&dpr=1
# https://www.google.com/search?sca_esv=1a2a07081c7891bb&rlz=1C1CHBF_enCA967CA967&sxsrf=AHTn8zrOQXwrDpH7yLXhmp7KGMOHHz4cgg:1741158847691&q=broccoli&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBsxayPSIAqObp_AgjkUGqekYoUzDaOcDDjQfK4KpR2OIJg0p8GjEafhVsU6UZNT2tUhHTA_XMhcunRVhbh9fJ-E_NpOwc0V4M-pxQ-VRkNVBLtVA39i8pg8uW6jlEtLtrbdNHgWLD-vHAmoqmNrKak2sYhiqpsjYUvt_8vhjtkMNrZWABg&sa=X&ved=2ahUKEwjkzvSUsvKLAxVDkokEHZqEKRUQtKgLegQIExAB&biw=1920&bih=953&dpr=1


def download_images(search_query='Cat', num_images=5):
    import requests
    from PIL import Image
    from io import BytesIO
    from duckduckgo_search import DDGS
    with DDGS() as ddgs:
        results = ddgs.images(search_query, max_results=num_images, safesearch='off')

    if not results:
        print(f"No images found for: {search_query}")
        return

    for i, result in enumerate(results):
        url = result['image']
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            image = Image.open(BytesIO(response.content))

            filename = f"downloads\\{search_query.replace(' ', '_')}_{i + 1}.jpg"
            image.save(filename)

            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")


def show_images(query='active dog', num_images=1, size="Medium", type_image="Photo", safe="off"):
    import requests
    from PIL import Image
    from io import BytesIO
    from duckduckgo_search import DDGS
    with DDGS() as ddgs:
        results = ddgs.images(
            query,
            max_results=num_images,
            size=size,
            type_image=type_image,
            safesearch=safe
        )

    if not results:
        print(f"No images found for: {query}")
        return

    for i, result in enumerate(results):
        url = result['image']
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            image = Image.open(BytesIO(response.content))

            # Directly display the image (without saving)
            image.show(title=f"{query} - {i + 1}")


        except Exception as e:
            print(f"Failed to fetch {url}: {e}")


# Example Usage
french_nouns = [
    "Bonjour",  # Hello
    "Au revoir",  # Goodbye
    "Oui",  # Yes
    "Non",  # No
    "Merci",  # Thank you
    "Désolé",  # Sorry
    "Excusez-moi",  # Excuse me
    "Maison",  # House
    "Porte",  # Door
    "Fenêtre",  # Window
    "Chaise",  # Chair
    "Table",  # Table
    "Lit",  # Bed
    "Lumière",  # Light
    "Téléphone",  # Phone
    "Voiture",  # Car
    "Clé",  # Key
    "Eau",  # Water
    "Pain",  # Bread
    "Fromage",  # Cheese
    "Café",  # Coffee
    "Thé",  # Tea
    "Vin",  # Wine
    "Pomme",  # Apple
    "Lait",  # Milk
    "Poulet",  # Chicken
    "Poisson",  # Fish
    "Aujourd'hui",  # Today
    "Demain",  # Tomorrow
    "Hier",  # Yesterday
    "Matin",  # Morning
    "Soir",  # Evening
    "Lundi",  # Monday
    "Mardi",  # Tuesday
    "Mercredi",  # Wednesday
    "Jeudi",  # Thursday
    "Vendredi",  # Friday
    "Samedi",  # Saturday
    "Dimanche",  # Sunday
    "Soleil",  # Sun
    "Pluie",  # Rain
    "Vent",  # Wind
    "Neige",  # Snow
    "Ciel",  # Sky
    "Rivière",  # River
    "Montagne",  # Mountain
    "Arbre",  # Tree
    "Fleur",  # Flower
    "Mer",  # Sea
    "Prix",  # Price
    "Argent",  # Money
    "Magasin",  # Store
    "Vêtements",  # Clothes
    "Chaussures",  # Shoes
    "Sac",  # Bag
    "Promotion",  # Sale
    "Danger",  # Danger
    "Police",  # Police
    "Hôpital",  # Hospital
    "Médecin",  # Doctor
    "Feu",  # Fire
]
legumes = [
    "carotte",  # carrot
    "pomme de terre",  # potato
    "tomate",  # tomato
    "courgette",  # zucchini
    "oignon",  # onion
    "ail",  # garlic
    "poivron",  # bell pepper
    "épinard",  # spinach
    "brocoli",  # broccoli
    "chou",  # cabbage
    "haricot vert",  # green bean
    "concombre",  # cucumber
    "petit pois",  # pea
    "aubergine",  # eggplant
    "radis",  # radish
    "laitue",  # lettuce
    "navet",  # turnip
    "champignon",  # mushroom
    "betterave",  # beetroot
    "poireau"  # leek
]


def random_images_from_your_list(your_list):
    import random
    a = 0
    while a < 100:
        a += 1
        word = random.choice(your_list)
        show_images(word)
