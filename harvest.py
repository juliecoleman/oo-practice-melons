############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, 
                 is_bestseller):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    cas.add_pairing('mint')
    cas.add_pairing('strawberries')
    all_melon_types.append(cas)

    cren = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types


melon_types = make_melon_types()
print(melon_types)

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with - ")
        for pairing in melon.pairings:
            print(f"{pairing}")

print(print_pairing_info(melon_types))

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dictionary = {}

    for melon in melon_types:
        if melon.code not in melon_dictionary:
            melon_dictionary[melon.code] = melon
    return melon_dictionary

print(make_melon_type_lookup(melon_types))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating,  
                 field_number, harvester_name):
        """Initialize a melon."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_number = field_number
        self.harvester_name = harvester_name
        

    def is_sellable(self):

        if self.color_rating > 5 and self.shape_rating > 5 and \
        self.field_number != 3:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_dictionary = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melon_dictionary['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melon_dictionary['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melon_dictionary['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melon_dictionary['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melon_dictionary['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melon_dictionary['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melon_dictionary['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melon_dictionary['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melon_dictionary['yw'], 7, 10, 3, 'Sheila')

    melon_list = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, \
                  melon_7, melon_8, melon_9]

    return melon_list

melon_list = make_melons(melon_types)
print(melon_list)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable() == True:
            status = "(CAN BE SOLD)"
        else:
            status = "(NOT SELLABLE)"
        #Or can be written as: 
        #status = 'CAN BE SOLD' if melon.is_sellable() else 'NOT SELLABLE'
        print(f"Harvested by {melon.harvester_name} from \
                Field {melon.field_number} {status}")

print(get_sellability_report(melon_list))



