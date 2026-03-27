import random

def generate_product(i):
    price = random.randint(20, 40)

    landing = price * 0.25
    fba = price * 0.30
    ppc = price * 0.20
    profit = round(price - (landing + fba + ppc), 2)
    margin = round((profit / price) * 100, 2)

    return {
        "id": i,
        "name": f"Smart Product {i}",
        "amazonLink": f"https://www.amazon.com/s?k=product+{i}",
        "price": price,
        "reviews": random.randint(50, 1500),
        "searchVolume": random.randint(1500, 5000),
        "weight": round(random.uniform(0.2, 4.5), 2),
        "trend": random.choice(["Evergreen", "Stable", "Growing"]),
        "profit": profit,
        "margin": margin
    }

def generate_products(n=50):
    return [generate_product(i) for i in range(n)]
