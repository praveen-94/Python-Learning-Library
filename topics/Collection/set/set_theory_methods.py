from helpers.display_utils import *

def main(topic_number: int):
    print_heading("Set Theory Based Operations", topic_number)
    imp_note_points("""IMP POINTS
- Remember that all these operations return a new set and do not modify the original sets.
- If you want to update a set in-place, you can use update(), intersection_update(), difference_update(), etc.
- Set operations are unordered and ignore duplicates by default.""")

    # -------------------------------------------------------------------------------------------------------
    # Union Operation
    # -------------------------------------------------------------------------------------------------------
    print_sub_heading("Union: Combines all unique elements from both sets.")
    display_note("This operation is useful when you want to merge sets without duplicates.")
    code1 = """# Define two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

union_set = setA.union(setB)
print(f"Union of A and B: {union_set}")
#--------------------------------------#"""
    output1 = run_code_snippet(code1)
    show_code_with_output(code1, output1)


    # -------------------------------------------------------------------------------------------------------
    # Intersection Operation
    # -------------------------------------------------------------------------------------------------------
    print_sub_heading("Intersection: Common elements found in both sets.")
    display_note("This is used to filter out elements that are shared between sets.")
    code2 = """ # Define two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
                          
intersection_set = setA.intersection(setB)
print(f"Intersection of A and B: {intersection_set}")
#-----------------------------------------------------#"""
    output2 = run_code_snippet(code2)
    show_code_with_output(code2, output2)

    # -------------------------------------------------------------------------------------------------------
    # Difference Operation
    # -------------------------------------------------------------------------------------------------------
    print_sub_heading("Difference: Elements in set A that are not in set B.")
    display_note("Used to subtract elements of one set from another.")
    display_note("The operation is directional. A - B is different from B - A.", "Warning")
    code3 = """# Define two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
difference_set = setA.difference(setB)
print(f"Difference of A - B: {difference_set}")
#-----------------------------------------------#"""
    output3 = run_code_snippet(code3)
    show_code_with_output(code3, output3)

    # -------------------------------------------------------------------------------------------------------
    # Symmetric Difference Operation
    # -------------------------------------------------------------------------------------------------------
    print_sub_heading("Symmetric Difference: Elements in either A or B but not in both.")
    display_note("""Useful for identifying mismatched or exclusive items between two sets.
This removes the common part and includes only non-overlapping elements.""")
    code4 = """# Define two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
sym_diff_set = setA.symmetric_difference(setB)
print(f"Symmetric Difference of A and B: {sym_diff_set}")
#---------------------------------------------------------#"""
    output4 = run_code_snippet(code4)
    show_code_with_output(code4, output4)

    # -------------------------------------------------------------------------------------------------------
    # Subset and Superset Check
    # -------------------------------------------------------------------------------------------------------
    print_sub_heading("Check whether one set is a subset or superset of another.")
    display_note("""Superset: Checks if set A contains all elements of set B.
Both operations are useful for validating hierarchy between sets.""")
    code5 = """# Define two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

print(f"Is setA subset of setB? {setA.issubset(setB)}")
print(f"Is setA superset of setB? {setA.issuperset(setB)}")
#----------------------------------------------------------#"""
    output5 = run_code_snippet(code5)
    show_code_with_output(code5, output5)

    # -------------------------------------------------------------------------------------------------------
    # Disjoint Check
    # -------------------------------------------------------------------------------------------------------
    print_sub_heading("Disjoint: Check if two sets have no elements in common.")
    display_note("""Returns True if sets are completely distinct, otherwise False.
Helpful in scenarios where overlapping items are not allowed or need to be checked.""")
    code6 = """# Define two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print(f"Are setA and setB disjoint? {setA.isdisjoint(setB)}")
#-------------------------------------------------------------#"""
    output6 = run_code_snippet(code6)
    show_code_with_output(code6, output6)
