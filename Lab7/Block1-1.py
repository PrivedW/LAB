# Вариант 7
import pickle

shops = {
    "Магазин 1": {"Пн": 1000, "Вт": 1200, "Ср": 800, "Чт": 950, "Пт": 1100, "Сб": 1500, "Вс": 2000},
    "Магазин 2": {"Пн": 900, "Вт": 850, "Ср": 700, "Чт": 600, "Пт": 750, "Сб": 1000, "Вс": 950},
    "Магазин 3": {"Пн": 2000, "Вт": 2100, "Ср": 1900, "Чт": 2200, "Пт": 2500, "Сб": 2700, "Вс": 3000},
    "Магазин 4": {"Пн": 1500, "Вт": 1600, "Ср": 1700, "Чт": 1800, "Пт": 1900, "Сб": 2000, "Вс": 2100},
    "Магазин 5": {"Пн": 500, "Вт": 400, "Ср": 300, "Чт": 600, "Пт": 700, "Сб": 800, "Вс": 1000},
    "Магазин 6": {"Пн": 1300, "Вт": 1400, "Ср": 1350, "Чт": 1450, "Пт": 1500, "Сб": 1600, "Вс": 1700},
    "Магазин 7": {"Пн": 100, "Вт": 200, "Ср": 150, "Чт": 300, "Пт": 400, "Сб": 500, "Вс": 600},
}


print("Средняя выручка за неделю по каждому магазину:")
shop_avg = {}
for shop, monei in shops.items():
    avg_money = sum(monei.values()) / len(monei)
    shop_avg[shop] = avg_money
    print(f"{shop}: {avg_money:.2f}")

max_store = max(shop_avg, key=shop_avg.get)
min_store = min(shop_avg, key=shop_avg.get)
print(f"Магазин с максимальной средней выручкой: {max_store} ({shop_avg[max_store]:.2f})")
print(f"Магазин с минимальной средней выручкой: {min_store} ({shop_avg[min_store]:.2f})")

print("Неблагоприятные дни для каждого магазина:")
bad_days = {}
for shop, monei in shops.items():
    min_day = min(monei, key=monei.get)
    bad_days[shop] = min_day
    print(f"{shop}: {min_day} ({monei[min_day]} руб.)")

highmStores = {store: monei for store, monei in shops.items() if monei["Вс"] > shop_avg[store] * 1.2}
print("Магазины в которых выручка в воскресенье превышает среднюю более чем на 20%:")
for shop, monei in highmStores.items():
    print(f"{shop}: Воскресенье ({monei['Вс']} руб.) превышает среднюю на 20% ({shop_avg[shop]:.2f})")


with open("data.pickle", "wb") as f:
    pickle.dump(highmStores, f)


with open("data.pickle", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)