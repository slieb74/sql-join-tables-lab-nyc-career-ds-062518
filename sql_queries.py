

def select_all_power_types_for_batman():
    return """SELECT powers.type
            FROM powers
            INNER JOIN hero_powers
            ON powers.id = hero_powers.power_id
            INNER JOIN heroes
            ON heroes.id = hero_powers.hero_id
            WHERE heroes.name = 'Batman';"""

# def better_way():
#     return """SELECT powers.type
#             FROM powers
#             INNER JOIN hero_powers, heroes
#             ON heroes.id = hero_powers.hero_id AND powers.id = hero_powers.power_id
#             WHERE heroes.name = 'Batman';"""

def select_total_damage_points_for_wonder_woman():
    return """SELECT SUM(powers.damage_points)
            FROM powers
            INNER JOIN hero_powers, heroes
            ON powers.id = hero_powers.power_id AND heroes.id = hero_powers.hero_id
            WHERE heroes.name = "Wonder Woman";"""

def list_iron_mans_powers_and_respective_damage_points():
    return """SELECT powers.type, powers.damage_points
            FROM powers
            INNER JOIN hero_powers, heroes
            ON powers.id = hero_powers.power_id AND heroes.id = hero_powers.hero_id
            WHERE heroes.name = "Iron Man";"""

def total_power_of_only_humans():
    return """SELECT SUM(powers.damage_points)
            FROM powers
            INNER JOIN hero_powers, heroes
            ON heroes.id = hero_powers.hero_id AND hero_powers.power_id = powers.id
            WHERE heroes.weakness = 'mortal human';"""

def select_all_hero_names_with_superstrength_in_alphabetical_order():
    return """SELECT heroes.name
            FROM heroes
            INNER JOIN hero_powers, powers
            ON heroes.id = hero_powers.hero_id AND powers.id = hero_powers.power_id
            WHERE powers.type = 'superstrength'
            ORDER BY heroes.name;"""

def list_heroes_and_their_num_of_powers_ordered_by_hero_name_alphabetically():
    return """SELECT heroes.name, COUNT(powers.type) AS num_of_powers
            FROM heroes
            INNER JOIN hero_powers, powers
            ON heroes.id = hero_powers.hero_id AND powers.id = hero_powers.power_id
            GROUP BY heroes.name;"""

def select_heroes_name_and_sum_damage_points_ordered_by_most_damage_to_least():
    return """SELECT heroes.name, SUM(powers.damage_points) AS total_damage
            FROM heroes INNER JOIN hero_powers, powers
            ON heroes.id = hero_powers.hero_id AND hero_powers.power_id = powers.id
            GROUP BY heroes.name
            ORDER BY total_damage DESC;"""
