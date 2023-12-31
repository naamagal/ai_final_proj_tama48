import evaluate_plan
import building_types as bt
import util
import building_types
import needs
import state


def check_clinic_conflicts(building, prev_state):
    pass


def check_community_center_conflicts(building, prev_state):
    pass


def check_elderly_center_conflicts(building, prev_state):
    pass


def check_high_school_conflicts(building, prev_state):
    pass


def check_hospital_conflicts(building, prev_state):
    pass


def check_kindergarden_conflicts(building, prev_state):
    pass


def check_mikve_conflicts(building, prev_state):
    pass


def check_police_conflicts(building, prev_state):
    pass


def check_primary_school_conflicts(building, prev_state):
    pass


def check_sport_conflicts(building, prev_state):
    pass


def check_synagogue_conflicts(building, prev_state):
    pass


def calculate_conflicts(building, prev_state):
    conflicts = 0

    for pub_building in building.get_used_public_buildings():
        conflicts += pub_building.calc_conflicts()
        
    return conflicts



################################################################

def min_conflict_solution(buildings_data, all_needs, housing_units_to_add):

    # main idea of min-conflict algorithm: in each iteration, check the conflicts, and add a floor to the
    # building with least conflict. (I think that the right way to do it is to check violations of the
    # optimal values (for example - 20 kids in a classroom, where each additional child is a conflict)
    num_added_units = 0

    added_floors_resd = [0]*len(bt.find_buildings_in_type(bt.RESIDENTIAL, buildings_data))
    prev_state = state.State(buildings_data, added_floors_resd, all_needs)

    # the algorithm runs until we have enough housing units
    while num_added_units < housing_units_to_add:

        # a for loop, iterating over all the residential buildings and counts their conflicts
        residential_buildings = building_types.find_buildings_in_type(building_types.RESIDENTIAL, buildings_data)
        conflicts = []
        for building in residential_buildings:
            conflicts.append((calculate_conflicts(building, prev_state), building))

        sorted(conflicts, key=lambda building: building[0]) #TODO check if it works properly
        building_to_increase = conflicts[0][1]
        num_added_units += util.add_floors(1, prev_state, building_to_increase) # returns the number of units added

    return prev_state




    # additional_heights = []
    # building_residential = []
    # building_types = []
    # # TODO implement algorithm, implement
    # for building in buildings_data:
    #     if building[0] == 'residential':
    #         building_residential == building[1]
    #         break
    #     else:
    #         building_types.append(building[0])

    # type algorithm here
    # for ...
    #   new_plan_state = ...
    #   additional_heights = evaluate_plan.EvaluatePlan(init_state, new_plan_state, all_needs)
    # ...



    # iter until max_iter
    # for i=1 to ____ :
        # if current_state is a solution of csp then return current_state
        # we return a solution set of values for the variable
        # var <-- a randomly chosen variable from the set of conflicted variables CONFLICTED[csp]
        # value <-- the value v for var that minimizes CONFLICTS(var,v,current_state,csp)
        # set var = value in current_state
    # return fail

    # current_state, an initial assignment of values for the variables in the csp
    # csp, a constraint satisfaction problem: <variables> , <constraints> ,



