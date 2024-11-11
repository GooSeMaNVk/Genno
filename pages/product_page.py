from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_basket_button = page.get_by_role("link", name="Добавить в корзину").nth(0)  # Кнопка добавления в корзину

    def get_product_origin(self):
        # Возвращает текст названия продукта "Происхождение"
        return self.page.locator(".basket-order__choose-card-header-title").nth(0).inner_text()

    def add_product_to_basket(self):

        self.add_to_basket_button.click()



