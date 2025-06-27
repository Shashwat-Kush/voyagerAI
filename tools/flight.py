class SearchFlightTool:
    def run(origin:str, destination:str, depart:date, class_type:str)->List[FlightOption]:
        """
        Searches for flights based on the provided parameters.

        Args:
            origin (str): The origin airport code.
            destination (str): The destination airport code.
            depart (date): The departure date.
            class_type (str): The class type for the flight (e.g., economy, business).

        Returns:
            List[FlightOption]: A list of available flight options.
        """
        pass

class BookFlightTool:
    def run(flight_if:str, passenger_info:dict, payment_token:str) -> BookingConfirmation:
        """
        Books a flight with the provided flight ID and passenger information.

        Args:
            flight_id (str): The ID of the flight to book.
            passenger_info (dict): A dictionary containing passenger details.
            payment_token (str): A token for processing the payment.

        Returns:
            BookingConfirmation: Confirmation details of the booked flight.
        """
        pass
