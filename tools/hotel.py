from datetime import date


class SearchHotelTool:
    def run(
        location: str, check_in: date, check_out: date, max_price: int
    ) -> List[HotelOption]:
        """
        Searches for hotels based on the provided parameters.

        Args:
            location (str): The location where the hotel is situated.
            check_in (date): The check-in date.
            check_out (date): The check-out date.
            max_price (int): The maximum price per night.

        Returns:
            List[HotelOption]: A list of available hotel options.
        """
        pass


class BookHotelTool:
    def run(hotel_id: str, guest_info: dict, payment_token: str) -> BookingConfirmation:
        """
        Books a hotel with the provided hotel ID and guest information.

        Args:
            hotel_id (str): The ID of the hotel to book.
            guest_info (dict): A dictionary containing guest details.
            payment_token (str): A token for processing the payment.

        Returns:
            BookingConfirmation: Confirmation details of the booked hotel.
        """
        pass
