"""
Назва: BookStore Order Calculator
Призначення: Консольна програма для розрахунку вартості замовлення книг з урахуванням
знижок, типу доставки та способів оплати.
"""

from typing import Final

# 2. Константи та анотації типів
FREE_DELIVERY_THRESHOLD: Final[float] = 1500.0
STANDARD_DELIVERY_FEE: Final[float] = 100.0
EXPRESS_DELIVERY_FEE: Final[float] = 250.0

def calculate_order() -> None:
    print("=== ЛАСКАВО ПРОСИМО ДО КНИЖКОВОГО ОНЛАЙН-МАГАЗИНУ ===")
    
    # 3 & 4. Введення та перетворення типів
    customer_name: str = input("Введіть ваше ім'я: ").strip()
    
    print("\nОберіть жанр літератури:")
    print("1 - Художня література")
    print("2 - Наукова / Технічна")
    print("3 - Дитяча література")
    
    genre_choice: int = int(input("Ваш вибір (1-3): "))
    book_price: float = float(input("Введіть ціну обраної книги (грн): "))
    quantity: int = int(input("Введіть кількість примірників: "))
    
    has_club_card_str: str = input("Чи є у вас клубна картка магазину? (так/ні): ").strip().lower()
    has_club_card: bool = True if has_club_card_str == "так" else False
    
    is_holiday_season: bool = True  # Приклад булевої константи святкового періоду

    # 7. Математичні операції
    subtotal: float = book_price * quantity
    
    # 8, 9, 10. Умовні конструкції та логічні оператори (вкладені умови)
    discount: float = 0.0
    
    if subtotal >= 1000.0:
        if has_club_card and not (subtotal > 3000.0):
            print(">> Застосовано стандартну знижку клубної картки (10%).")
            discount = subtotal * 0.10
        elif subtotal > 3000.0:
            print(">> Застосовано максимальну оптову знижку (20%).")
            discount = subtotal * 0.20
        else:
            print(">> Застосовано знижку за суму замовлення (5%).")
            discount = subtotal * 0.05
    else:
        # 11. Умовний вираз (тернарний оператор)
        discount = 50.0 if (is_holiday_season and has_club_card) else 0.0
        if discount > 0:
            print(">> Застосовано святковий бонус-знижку у розмірі 50 грн.")

    total_after_discount: float = subtotal - discount

    # 12. Використання конструкції match-case (вибір способу доставки)
    print("\nОберіть спосіб доставки:")
    print("1 - Самовивіз (Безкоштовно)")
    print("2 - Стандартна пошта")
    print("3 - Експрес-доставка")
    
    delivery_type: int = int(input("Ваш вибір (1-3): "))
    delivery_fee: float = 0.0

    match delivery_type:
        case 1:
            delivery_fee = 0.0
            delivery_name = "Самовивіз"
        case 2:
            # Вкладена перевірка для безкоштовної стандартної доставки
            delivery_fee = 0.0 if total_after_discount >= FREE_DELIVERY_THRESHOLD else STANDARD_DELIVERY_FEE
            delivery_name = "Стандартна пошта"
        case 3:
            delivery_fee = EXPRESS_DELIVERY_FEE
            delivery_name = "Експрес-доставка"
        case _:
            print("Невірний вибір доставки, встановлено стандартну пошту за замовчуванням.")
            delivery_fee = STANDARD_DELIVERY_FEE
            delivery_name = "Стандартна пошта"

    final_total: float = total_after_discount + delivery_fee

    # 5 & 6. Виведення та форматування за допомогою f-рядків
    print("\n" + "="*40)
    print(ЖУРНАЛ ЗАМОВЛЕННЯ ДЛЯ: {customer_name.upper()})
    print(f"Сума до сплати за книги: {subtotal:.2f} грн")
    print(f"Знижка: -{discount:.2f} грн")
    print(f"Доставка ({delivery_name}): {delivery_fee:.2f} грн")
    print(f"ЗАГАЛЬНА ВАРТІСТЬ ДО СПЛАТИ: {final_total:.2f} грн")
    print("="*40)
    print("Дякуємо за покупку!")

if __name__ == "__main__":
    calculate_order()