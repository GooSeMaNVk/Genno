import re
from playwright.sync_api import Page, Locator, expect

class BasketPage:
    def __init__(self, page: Page):
        self.page = page
        self.promo_code_input = page.locator('[placeholder="Введите промокод"]')  
        self.apply_promo_button = page.locator("app-promo-code i")  
        self.product_price_locator_before = page.locator("body > app-root:nth-child(1) > app-massmarket.ng-star-inserted:nth-child(2) > div.wrapper.wrapper--new > app-ordercheckout.ng-star-inserted:nth-child(3) > div.basket-order > div.basket-order__container.basket-order__container--main.ng-star-inserted:nth-child(1) > div.basket-order__grid > div.basket-order__cell.basket-order__cell--report:nth-child(2) > div.basket-order__report > overlay-scrollbars > div:nth-child(2) > div.basket-order__report-inner > div.basket-order__report-total:nth-child(4) > span:nth-child(2) > priceroller")  
        self.product_price_locator_after = page.locator("overlay-scrollbars").get_by_text(re.compile(r"\d+\.\d{2} ₽")).nth(2) 
        self.promo_code_text = page.locator("text=У меня есть промокод")  

    def apply_promo_code(self, promo_code: str):
        """Метод для применения промокода"""
        # Кликаем по тексту "У меня есть промокод"
        self.promo_code_text.click()

        # Заполняем поле промокода и применяем его
        self.promo_code_input.fill(promo_code)
        self.apply_promo_button.click()

    def get_product_price(self, after_promo=False) -> float:
        """Метод для получения цены товара из корзины"""
        # Ожидаем, пока элемент с ценой товара станет видимым в зависимости от того, после или до применения промокода
        locator = self.product_price_locator_after if after_promo else self.product_price_locator_before
        expect(locator).to_be_visible()

        # Получаем текстовое содержимое из элемента
        price_text = locator.text_content()

        if price_text:
            # Преобразуем цену из текста в число
            # Заменяем '₽' на пустую строку и, если нужно, меняем запятую на точку
            price_text = price_text.replace('₽', '').replace(',', '.').strip()

            try:
                # Преобразуем строку в float
                return float(price_text)
            except ValueError:
                
                print(f"Не удалось преобразовать цену: {price_text}")
                return 0.0
        return 0.0  # Если текста нет или произошла ошибка, возвращаем 0.0
