def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """Return the bean cost before discounts."""
    return bag_price * bags

def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """Return the discount rate based on bags and partner status."""
    if bags < 20:
        discount = 0.0
    elif bags < 80:
        discount = 0.09
    else:
        discount = 0.14

    if partner and bags >= 20:
        discount += 0.04

    return discount

def calculate_shipment_total(
    bag_price: float, bags: int, partner: bool = False
) -> float:
    """Return the shipment total including any shipping fee."""
    bean_cost = calculate_bean_cost(bag_price, bags)
    discount = get_bulk_discount(bags, partner)
    discounted_cost = bean_cost * (1 - discount)

    if discounted_cost < 250:
        discounted_cost += 35

    return discounted_cost

def requires_prepayment(total: float) -> bool:
    """Return True if the shipment requires prepayment."""
    return total >= 1500

def needs_pallet(bags: int, total: float) -> bool:
    """Return True when a shipment needs a freight pallet."""
    return bags > 60 and total > 700

def total_shipped(shipments: list) -> float:
    """Return the combined total of all shipments."""
    total = 0.0

    for shipment in shipments:
        bag_price = shipment["bag_price"]
        bags = shipment["bags"]
        partner = shipment["partner"]

        shipment_total = calculate_shipment_total(
            bag_price, bags, partner
        )

        total += shipment_total

    return total

def largest_shipment(shipments: list) -> str:
    """Return the buyer with the largest shipment total."""
    largest_total = -1.0
    largest_buyer = ""

    for shipment in shipments:
        total = calculate_shipment_total(
            shipment["bag_price"],
            shipment["bags"],
            shipment["partner"],
        )

        if total > largest_total:
            largest_total = total
            largest_buyer = shipment["buyer"]

    return largest_buyer

def format_shipment_line(
    buyer: str, total: float, prepayment: bool, pallet: bool
) -> str:
    """Return one formatted line for the shipment report."""
    prepayment_text = "yes" if prepayment else "no"
    pallet_text = "yes" if pallet else "no"

    return (
        f"{buyer}: ${total:.2f} | "
        f"prepayment: {prepayment_text} | pallet: {pallet_text}"
    )