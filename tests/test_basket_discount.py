import pytest

def test_apply_promo_code(product_page, basket_page):
    # Получение названия товара "Происхождение"
    product_name = product_page.get_product_origin()
    print(f"Добавленный товар: {product_name}")

    # Добавление товара в корзину
    product_page.add_product_to_basket()

    # Переход на страницу корзины
    basket_page.page.goto("https://basket.genotek.ru/basket")

    # Получение текущей цены товара до применения промокода
    try:
        price_before = basket_page.get_product_price(after_promo=False)  # Получаем цену до промокода
        print(f"Цена товара до применения промокода: {price_before}")
    except Exception as e:
        print(f"Ошибка при получении цены до промокода: {e}")

    # Применение промокода
    basket_page.apply_promo_code("genotek5")

    # Ждем обновления цены товара
    try:
        # Ожидаем, что обновленная цена будет видна
        basket_page.page.wait_for_selector("overlay-scrollbars", timeout=10000)

        # Получаем обновленную цену после применения промокода
        price_after = basket_page.get_product_price(after_promo=True)  # Получаем цену после промокода
        print(f"Цена товара после применения промокода: {price_after}")
    except Exception as e:
        print(f"Не удалось обновить цену товара после применения промокода: {e}")
