import sys, re
import numpy as np

def remove_all_whitespace(x):
    pattern = re.compile(r'\s+')
    return re.sub(pattern, '', x)

def whitespace_to_semicol(x):
    pattern = re.compile(r'\s+')
    return re.sub(pattern, ';', x)

def extract_coord(x):
    coo = whitespace_to_semicol( x ).split( ';' )[1:4]
    return np.array( [float(ci) for ci in coo] )

def atomic_positions(contcar, natoms):
    pox = np.zeros((natoms, 3))
    for i in range(natoms):
        pox[i] = extract_coord( contcar[i+8] )

class Lattice:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            contcar = f.readlines()
        system = remove_all_whitespace( contcar[0] )
        scale_factor = float( remove_all_whitespace( contcar[1] ) )
        ucell = np.array( [extract_coord(x) for x in contcar[2:5]] )
        species = whitespace_to_semicol( contcar[5] ).split( ';' )[1:-1]
        nspecies = [int(n) for n in whitespace_to_semicol( contcar[6] ).split( ';' )[1:-1]]
        natoms = sum(nspecies)
        coosys = remove_all_whitespace( contcar[7] )
        pox = atomic_positions(contcar, natoms)

if ( len(sys.argv) != 2 ): 
    print('polaroncar >> Wrong number of arguments.')
    exit(404)

filename = sys.argv[1]

print(pox)
