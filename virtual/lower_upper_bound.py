import calc_wirt
import sym_hm


def get_bounds(gauss_code):
    knot_dict, seed_strand_set, wirt_num = calc_wirt.wirt_main(gauss_code)
    transpositions = sym_hm.sym_group_crafter()
    hmorph, sym_gen_set = sym_hm.homomorphism_finder(seed_strand_set, knot_dict, wirt_num, transpositions)
    lower_bound = 1
    if hmorph:
        lower_bound = len(sym_gen_set)
    return lower_bound, wirt_num


# # # test case
# my_gauss = [1, -2, 3, -4, 5, -6, 7, -1, -9, 10, -3, 11, -12, 13, -14, 15, -7, 9, -16, 2, -11, 12, -13, 14, -15, 6, -5,
#             4, -10, 16]
# my_bounds = get_bounds(my_gauss)
# print("lower, upper bound: ", my_bounds)
