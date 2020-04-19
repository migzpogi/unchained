class Ilan:

    @staticmethod
    def get_qty(total_amount, price):
        """
        Divides the total amount by its price to get the quantity
        :param total_amount: number to be divided
        :param price: number used to divide
        :return: rounded down total_amount/price
        """

        return round(total_amount/price)

    @staticmethod
    def is_string_number_valid(number: str):
        """
        Checks if the given number is valid
        :param str number: input given by the user
        :return:
        """

        try:
            stripped_number = Ilan().__remove_commas(number)
            return float(stripped_number)
        except AttributeError:
            print('Please make sure you provided int')
            return False
        except ValueError:
            print('Please check correct format. No letters, multiple decimal points, special characters')
            return False

    @staticmethod
    def __remove_commas(number):
        """
        Removes commas
        :param str number:
        :return:
        """

        return number.replace(',', '')