# 📱 Phone — Classe Python OOP

> Un exercice de **Programmation Orientée Objet** en Python — modélisation d'une classe `Phone` avec attributs et méthodes.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Orienté%20Objet-22c55e?style=flat)

---

## 💡 Ce que fait ce projet

Création d'une classe `Phone` qui représente un téléphone avec ses caractéristiques, et affiche son statut de disponibilité.

```
Galaxy S23 by Samsung has 128GB of storage and is currently in stock
Iphone 15 Pro by Apple has 256GB of storage and is currently out of stock
Redmi Note 12 by Xiaomi has 64GB of storage and is currently in stock
```

---

## 🧱 Structure de la classe

```python
class Phone:
    def __init__(self, brand, model, storage, inStock):
        self.brand = brand      # Marque du téléphone
        self.model = model      # Modèle
        self.storage = storage  # Stockage en GB
        self.inStock = inStock  # Disponibilité (True/False)

    def Afficher(self):
        # Affiche les infos du téléphone + disponibilité
```

---

## 📦 Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `brand` | `str` | Marque du téléphone |
| `model` | `str` | Modèle du téléphone |
| `storage` | `int` | Capacité de stockage en GB |
| `inStock` | `bool` | `True` = disponible, `False` = épuisé |

---

## ⚙️ Méthodes

| Méthode | Description |
|---------|-------------|
| `__init__()` | Constructeur — initialise les attributs |
| `Afficher()` | Affiche les informations du téléphone |

---

## 🧪 Exemples d'utilisation

```python
p1 = Phone("Samsung", "Galaxy S23", 128, True)
p2 = Phone("Apple", "Iphone 15 Pro", 256, False)
p3 = Phone("Xiaomi", "Redmi Note 12", 64, True)

p1.Afficher()
p2.Afficher()
p3.Afficher()
```

---

## 🧑‍💻 Lancer le projet

```bash
git clone https://github.com/Doming-7/phone-oop.git
cd phone-oop
python main.py
```

---

## 📁 Structure du projet

```
phone-oop/
├── main.py       # Classe Phone + instances
└── README.md     # You are here
```

---

## 📌 Roadmap

- [ ] Ajouter un attribut `price`
- [ ] Méthode `appliquerRemise(pct)` pour réduire le prix
- [ ] Liste de téléphones avec filtrage par stock
- [ ] Héritage — classe `Smartphone` qui étend `Phone`

---

## 👤 Auteur

Développé par **Doming-7** — apprentissage de la POO Python pas à pas.

---

## 🔒 Licence

Tous droits réservés © Doming-7
