import random

def generate_product(i):
    price = random.randint(20, 40)

    landing_cost = round(price * 0.25, 2)
    fba_fee = round(price * 0.30, 2)
    ppc = round(price * 0.20, 2)
    profit = round(price - (landing_cost + fba_fee + ppc), 2)
    margin = round((profit / price) * 100, 2)

    return {
        "id": i,
        "name": f"Smart Niche Product {i}",
        "amazonLink": f"https://www.amazon.com/s?k=product+{i}",
        "price": price,

        # RULE DATA
        "monthlyRevenue": random.randint(5000, 30000),
        "searchVolume": random.randint(1500, 5000),
        "reviews": random.randint(50, 1500),
        "weight": round(random.uniform(0.2, 4.5), 2),
        "size": random.choice(["Small", "Medium"]),
        "competition": random.choice(["Low", "Medium"]),
        "trend": random.choice(["Evergreen", "Stable", "Growing"]),

        # COSTS
        "landingCost": landing_cost,
        "fbaFee": fba_fee,
        "ppc": ppc,
        "profit": profit,
        "margin": margin
    }

def generate_products(n=40):
    return [generate_product(i) for i in range(n)]
