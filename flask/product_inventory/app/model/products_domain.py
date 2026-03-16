# This will be the domain
    # A group of related items in a model
    # the domain is a data object and has no SQL or any know how of how to store the instance


# We are creating a shop that stores precious metals and stones/jems
# Gold, Silver, Platinum, Copper, Tsavorite
class Product:
    def __init__(self, name, price, weight, color, durability):
        self.name = name
        self.price = price
        self.weight = weight
        self.color = color
        self.durability = durability

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "weight": self.weight,
            "color": self.color,
            "durability": self.durability
        }
