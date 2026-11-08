# DEBUG PRACTICE - BOSS LEVEL: Mini Library Manager
# Topics mixed: variables, conditions, list, tuple, dictionary, set,
# loops, functions, nested data.
# Is program mein 12 bugs hain: syntax-free, lekin runtime, logic aur
# "silent" bugs (jo error nahi dete, bas galat output dete hain).
#
# Expected output (sab fix hone ke baad):
# Total books: 4
# Available: ['Python Basics', 'DSA in Java', 'Machine Learning']
# Issued
# Out of stock
# Book not found
# Issued
# Issued
# Issued: {'Md': ['Python Basics', 'DSA in Java'], 'Ali': ['DSA in Java']}
# Copies left: {'Python Basics': 4, 'Data Science': 0, 'DSA in Java': 0, 'Machine Learning': 3}
# Days 5 -> fee 0
# Days 7 -> fee 0
# Days 12 -> fee 25
# Days 40 -> fee 100
# Never issued: ['Data Science', 'Machine Learning']
# In stock: ['Python Basics', 'Machine Learning']
# Average book age: 6.5
# ['a'] ['b']
#
# Rules: pehle code ko padho aur samjho, phir run karo.
# Har bug fix karne ke baad likho: bug kahan tha aur kyun tha.

books = [
    ("Python Basics", "Guido", 2020, 5),
    ("Data Science", "Wes", 2018, 0),
    ("DSA in Java", "Babbar", 2019, 2),
    ("Machine Learning", "Andrew", 2021, 3),
]


def build_catalog(books):
    catalog = {}
    
    for title, author, year, copies in books:
        entry = {}
        entry["author"] = author
        entry["year"] = year
        entry["copies"] = copies
        catalog[title] = entry  #quetes bug 1
    return catalog


def available_titles(catalog):
    result = []
    for title, data in catalog.items():
        if data["copies"] > 0:
            result.append(title)
    return result


def issue_book(catalog, title, member, issued):
    if title not in catalog:
        return "Book not found"
    elif catalog[title]["copies"] == 0:
        return "Out of stock"
    else:
        catalog[title]["copies"] -= 1

        if member not in issued:
            issued[member] = []

        issued[member].append(title)
        return "Issued"


def late_fee(days_kept):
    allowed = 7
    if days_kept <= allowed:
        return 0
    fee = (days_kept - allowed) * 5
    return min(fee, 100)


def record(title, log=None):
    if log is None:
        log = []

    log.append(title)
    return log


catalog = build_catalog(books)
issued = {}
print("Total books: " , len(books))
print("Available:", available_titles(catalog))
print(issue_book(catalog, "Python Basics", "Md", issued))
print(issue_book(catalog, "Data Science", "Md", issued))
print(issue_book(catalog, "Rust Guide", "Ali", issued))
print(issue_book(catalog, "DSA in Java", "Ali", issued))
print(issue_book(catalog, "DSA in Java", "Md", issued))
print("Issued:", issued)
print("Copies left:", {t: d["copies"] for t, d in catalog.items()})

for days in (5, 7, 12, 40):
    print("Days", days, "-> fee", late_fee(days))

borrowed_titles = set()
for titles in issued.values():
    for title in titles:
        borrowed_titles.add(title)
print("Never issued:", sorted(set(catalog) - borrowed_titles))

in_stock = [
    t for t in catalog
    if catalog[t]["copies"] > 0
]
print("In stock:", in_stock)

total_age = 0
for data in catalog.values():
    total_age += 2026 - data["year"]
print("Average book age:", total_age / len(catalog))

print(record("a"), record("b"))