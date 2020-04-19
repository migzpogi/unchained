class Ilan:

    @staticmethod
    def get_qty(total_amount, price):
        """
        Divides the total amount by its price to get the quantity
        :param total_amount:
        :param price:
        :return:
        """

        return round(total_amount/price)
