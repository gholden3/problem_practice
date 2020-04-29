# For a chemical reaction represented by a string, verify that the chemical
# reaction is a balanced reaction (i.e. that we didn't somehow lose or gain
# an atom during reaction). If the reaction is balanced return true,
# otherwise return false.

# For example, for the hydrogen combustion reaction:

# '2 H2 + O2 -> 2 H2O'
# would output true because the number of atoms in the reactants match up
# with the number of atoms in the product.

# However, for the precipitation of silver-chloride:

# 'NaCl + AgNO3 -> NaNO3 + Ag'
# the output should be false because we're missing the chlorine atom in
# the products.

# The reactancts and products will always be separated by a right
# pointing arrow "->" and the individual molecules within the
# reactants/products are always separated by a "+" sign. Multiple
# molecules are represented by a number and space prefacing the
# molecule (e.g., "2 H20").

# Other test cases:

# 'O2 -> NaCl' = false
# 'C6H12O6 + 6 O2 -> 6 CO2 + 6 H2O' = true
# '10 NH3 + 10 H2O -> 10 NH4 + OH' = false

import unittest
from collections import Counter

def pop_next_element_name_from_molecule(molecule):
    # (max 2 charachters, first upcase second donwcase)
    # if molecule is only one char return (first, "")
    if(len(molecule) < 2):
        return (molecule, "")
    # extract first 2 characters.
    first, second = molecule[0], molecule[1]
    # if the second charachter is a number return (first, everything except first)
    #TODO: account for multiple digit numbers here
    if(second.isdigit()):
        return (first, molecule[1:])
    # if the second charachter is a capital letter return (first, everything except first)
    if(second.isupper()):
        return (first , molecule[1:])
    # if the second charachter is a lowercase letter return (first + second, everything except first and second)
    if(second.islower()):
        return (first + second, molecule[2:])
    # the second char is something we didn't expect
    return -1

def pop_next_count_from_molecule(molecule):
    # account for the end of the string
    if(molecule == ""):
        return (1, "")
    count = molecule[0]
    count_str = ""
    if(count.isdigit()):
        for char in molecule:
            if(char.isdigit()):
                count_str += char
            else: 
                break
        length_of_count_str = len(count_str)
        return(int(count_str), molecule[length_of_count_str:])
    else: # there was no count
        return (1, molecule)

def add_atom_counts_for_molecule(molecule, factor, atoms):
    while(len(molecule) > 0):
        (element_name, molecule) = pop_next_element_name_from_molecule(molecule)
        (count, molecule) = pop_next_count_from_molecule(molecule)
        atoms[element_name] += count * factor
    return atoms

def count_atoms_in_molecules(molecules):
    atoms = Counter()
    for molecule in molecules:
        factor = 1
        # if there is a space in the molecule this implies a count applies to the following molecule
        if(molecule.count(' ')):
            factor, molecule = molecule.split(' ')
            factor = int(factor)
        # count the atoms in each molecule
        atoms = add_atom_counts_for_molecule(molecule, factor, atoms)
    return atoms

def balanced_reaction(reaction):
    left_side, right_side = reaction.split(' -> ')
    left_molecules = left_side.split(' + ')
    right_molecules = right_side.split(' + ')
    left_atom_counts = count_atoms_in_molecules(left_molecules)
    right_atom_counts = count_atoms_in_molecules(right_molecules)
    return right_atom_counts == left_atom_counts

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('2 H2 + O2 -> 2 H2O', True),
        ('NaCl + AgNO3 -> NaNO3 + Ag', False),
        ('O2 -> NaCl', False),
        ('C6H12O6 + 6 O2 -> 6 CO2 + 6 H2O', True),
        ('10 NH3 + 10 H2O -> 10 NH4 + OH' , False)]

    def test_balanced_reactions(self):
        for [test_string, expected] in self.data:
            print("testing " + test_string)
            actual = balanced_reaction(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()