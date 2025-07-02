def process_order(order):
    validation_result = validate_order(order)
    if validation_result is not None:
        return validation_result

    total_price = calculate_total_price(order)
    if total_price is None:
        return "Invalid order: Item not found."

    total_price = apply_discount(order, total_price)

    payment_status = process_payment(order['payment_info'], total_price)
    if not payment_status:
        return "Payment failed."

    confirmation = generate_confirmation(order, total_price)
    return confirmation


def validate_order(order: dict) -> str | None:
    """Validate the order for required fields."""
    if not order.get('item_id') or not order.get('quantity'):
        return "Invalid order: Missing item ID or quantity."
    return None


def calculate_total_price(order: dict) -> float | None:
    """Calculate the total price for the order."""
    item_price = get_item_price(order['item_id'])
    if item_price is None:
        return None
    return item_price * order['quantity']


def apply_discount(order: dict, total_price: float) -> float:
    """Apply discount if applicable."""
    if order['quantity'] > 10:
        discount = total_price * 0.1  # 10% discount for large orders
        total_price -= discount
    return total_price
