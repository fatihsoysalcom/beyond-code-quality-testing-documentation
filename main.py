import unittest

def calculate_discount(price: float, discount_percentage: float) -> float:
    """
    Calculates the final price after applying a discount.

    This function demonstrates the importance of clear function design,
    input validation, and documentation beyond just writing code.
    It ensures that the inputs are valid before performing the calculation.

    Args:
        price (float): The original price of the item. Must be non-negative.
        discount_percentage (float): The discount percentage to apply (e.g., 10 for 10%).
                                     Must be between 0 and 100.

    Returns:
        float: The final price after the discount.

    Raises:
        ValueError: If price or discount_percentage are invalid.
    """
    # --- Article Concept: Input Validation & Robustness (beyond just coding the logic) ---
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Price must be a non-negative number.")
    if not isinstance(discount_percentage, (int, float)) or not (0 <= discount_percentage <= 100):
        raise ValueError("Discount percentage must be between 0 and 100.")

    # --- Article Concept: Clear, Readable Logic ---
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    return round(final_price, 2) # Round to 2 decimal places for currency

class TestDiscountCalculator(unittest.TestCase):
    """
    Unit tests for the calculate_discount function.

    --- Article Concept: Comprehensive Testing (critical for successful projects) ---
    Tests ensure the function behaves as expected under various conditions,
    validating its correctness and robustness.
    """
    def test_valid_discount(self):
        # Test a standard discount scenario
        self.assertAlmostEqual(calculate_discount(100, 10), 90.0)
        self.assertAlmostEqual(calculate_discount(50, 20), 40.0)
        self.assertAlmostEqual(calculate_discount(120.50, 5), 114.48)

    def test_no_discount(self):
        # Test when discount is 0%
        self.assertAlmostEqual(calculate_discount(100, 0), 100.0)
        self.assertAlmostEqual(calculate_discount(75.50, 0), 75.50)

    def test_full_discount(self):
        # Test when discount is 100%
        self.assertAlmostEqual(calculate_discount(100, 100), 0.0)
        self.assertAlmostEqual(calculate_discount(25.75, 100), 0.0)

    def test_zero_price(self):
        # Test with a zero price
        self.assertAlmostEqual(calculate_discount(0, 10), 0.0)
        self.assertAlmostEqual(calculate_discount(0, 99), 0.0)

    def test_invalid_price_type(self):
        # Test for invalid price types
        with self.assertRaises(ValueError):
            calculate_discount("abc", 10)
        with self.assertRaises(ValueError):
            calculate_discount(None, 10)

    def test_negative_price(self):
        # Test for negative price
        with self.assertRaises(ValueError):
            calculate_discount(-100, 10)

    def test_invalid_discount_type(self):
        # Test for invalid discount percentage types
        with self.assertRaises(ValueError):
            calculate_discount(100, "ten")
        with self.assertRaises(ValueError):
            calculate_discount(100, None)

    def test_discount_out_of_range(self):
        # Test for discount percentage out of valid range
        with self.assertRaises(ValueError):
            calculate_discount(100, -5)
        with self.assertRaises(ValueError):
            calculate_discount(100, 101)

if __name__ == "__main__":
    print("--- Demonstrating Software Quality Beyond Just Code ---")
    print("Function: calculate_discount")
    print("Purpose: Calculates final price after discount with robust validation.")

    print("\n--- Running Example Scenarios ---")

    try:
        # --- Article Concept: Demonstrating usage with good inputs ---
        price1 = 150.0
        discount1 = 15
        final1 = calculate_discount(price1, discount1)
        print(f"Original Price: ${price1}, Discount: {discount1}% -> Final Price: ${final1}")

        price2 = 200.0
        discount2 = 0
        final2 = calculate_discount(price2, discount2)
        print(f"Original Price: ${price2}, Discount: {discount2}% -> Final Price: ${final2}")

        price3 = 75.50
        discount3 = 25
        final3 = calculate_discount(price3, discount3)
        print(f"Original Price: ${price3}, Discount: {discount3}% -> Final Price: ${final3}")

        print("\n--- Demonstrating Robustness with Invalid Inputs ---")
        # --- Article Concept: Error handling for invalid inputs ---
        # This line will raise an error, caught below
        # calculate_discount(-100, 10)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    try:
        calculate_discount(-100, 10)
    except ValueError as e:
        print(f"Caught expected error (negative price): {e}")

    try:
        calculate_discount(100, 105)
    except ValueError as e:
        print(f"Caught expected error (discount out of range): {e}")

    try:
        calculate_discount("invalid", 10)
    except ValueError as e:
        print(f"Caught expected error (invalid price type): {e}")

    print("\n--- Running Unit Tests ---")
    # --- Article Concept: Automated Testing ---
    # Run the tests programmatically
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDiscountCalculator))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    print("\n--- End of Demonstration ---")
