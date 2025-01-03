# This is project from Harry chemistry class. I couldn't run on Pycharm, but still useful for review and code readability

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_url = "https://github.com/RodrigoAVargasHdz/CHEM-4PB3/raw/w2024/Course_Notes/data/methane.csv"
data = pd.read_csv(data_url)

print("Data Information:")
print(data.info())
# data has 9000 points
# data has position, energy level, 3D postition of H1,H2,H3,H4, C of CH4 with both validation and test data

min_energy_row = data[data['Energy'] == data['Energy'].min()]

lowest_energy_geometry = min_energy_row.iloc[0]['Energy']

print("Geometry with the lowest energy:", lowest_energy_geometry)
print(min_energy_row)


def get_xyz_str(z, xyz):
    n_atoms = len(z)
    xyz_ = []
    xyz_str = '%s\n * (null), Energy   -1000.0000000\n' % (n_atoms)
    for zi, xyzi in zip(z, xyz):
        xyzi_str = '%s     %.4f     %.4f     %.4f\n' % (
            zi, float(xyzi[0]), float(xyzi[1]), float(xyzi[2]))
        xyz_str += xyzi_str
    return xyz_str


def draw_molecule(view, z, xyz):
    """_summary_

    Args:
        view (_type_): py3dmol class
        z (_type_): atomic numbers, list for CH4, z = ['H','H','H','H','C']
        xyz (_type_): xyz coordinates in numpy array
    """
    xyz_str = get_xyz_str(z, xyz)
    view.addModel(xyz_str, 'xyz')
    view.setStyle({'sphere': {'radius': 0.35}, 'stick': {'radius': 0.1}})
    view.zoomTo()
    view.update()
    view.clear()


'''
#Example Ozone
z = ['O','O','O']
xyz = np.array([[0.4496,   0.0000000,   0.0000000],
    [-0.2248,   0.0000000,  1.0927],
    [ -0.2248,  0.0000000,  -1.0927]])
view = py3Dmol.view(width=400, height=400)
view.show()
draw_molecule(view, z, xyz)
'''

# code here!
# Create a py3Dmol view
import py3Dmol

h1 = np.array(min_energy_row[['H1x', 'H1y', 'H1z']])
h2 = np.array(min_energy_row[['H2x', 'H2y', 'H2z']])
h3 = np.array(min_energy_row[['H3x', 'H3y', 'H3z']])
h4 = np.array(min_energy_row[['H4x', 'H4y', 'H4z']])
c = np.array(min_energy_row[['Cx', 'Cy', 'Cz']])
xyz = np.reshape(np.vstack((h1.ravel(), h2.ravel(), h3.ravel(), h4.ravel(), c.ravel())), (5, 3))


def get_xyz_str(z, xyz):
    n_atoms = len(z)
    xyz_ = []
    xyz_str = '%s\n * (null), Energy   -1000.0000000\n' % (n_atoms)
    for zi, xyzi in zip(z, xyz):
        xyzi_str = '%s     %.4f     %.4f     %.4f\n' % (
            zi, float(xyzi[0]), float(xyzi[1]), float(xyzi[2]))
        xyz_str += xyzi_str
    return xyz_str


def draw_molecule(view, z, xyz):
    xyz_str = get_xyz_str(z, xyz)
    view.addModel(xyz_str, 'xyz')
    view.setStyle({'sphere': {'radius': 0.35}, 'stick': {'radius': 0.1}})
    view.zoomTo()
    view.update()
    view.clear()


z = ['H', 'H', 'H', 'H', 'C']

view = py3Dmol.view(width=400, height=400)
view.show()
draw_molecule(view, z, xyz)
# histogram of the energies for  CH4
plt.hist(data['Energy'])
plt.title('Energy Histogram of CH4')
plt.xlabel('Energy(Eh)')
plt.ylabel('Position')
ax = plt.gca()
ax.set_xlim([-40.48, -40.42])
plt.show()
# Common energy level for CH4 ranging approximately around -40.48Eh and least common approximately around -40.42Eh

# code here!
from sklearn.model_selection import train_test_split


def split_data(data, n_tr, n_val):
    # Extract features and target variable
    data = data.to_numpy()
    X = data['Energy']
    y = d1
    X = X.to_numpy()
    y = y.to_numpy()

    # Split the data into training and temporary set (remaining data)
    X_train_temp, X_tst, y_train_temp, y_tst = train_test_split(X, y, test_size=0.2, random_state=42)

    # Determine the size of the temporary set
    num_test_points = len(X_tst)

    # Calculate the ratio of training and validation points
    total = n_tr + n_val
    train_ratio = n_tr / total

    # Split the temporary set into training and validation sets
    X_tr, X_val, y_tr, y_val = train_test_split(X_train_temp, y_train_temp, train_size=train_ratio, random_state=42)

    # split the data into training, validation and test

    return (X_tr, y_tr), (X_val, y_val), (X_tst, y_tst)


# code here!
h1 = np.array(data[['H1x', 'H1y', 'H1z']])
h2 = np.array(data[['H2x', 'H2y', 'H2z']])
h3 = np.array(data[['H3x', 'H3y', 'H3z']])
h4 = np.array(data[['H4x', 'H4y', 'H4z']])
c = np.array(data[['Cx', 'Cy', 'Cz']])
X = np.hstack((h1, h2, h3, h4, c))
X1 = X.reshape(9000, 5, 3)


def distance(xi, xj):
    diff = np.sum((xi - xj) ** 2)
    return diff


d1 = []
for i, xi in enumerate(X1):
    dall = []
    for i, zi in enumerate(xi):
        # print(zi)
        for j, zj in enumerate(xi[i + 1:]):
            d = distance(zi, zj)
            dall.append(d)
    d1.append(dall)
d1 = np.array(d1)

# code here!
bins = np.linspace(0, np.max(d1), 20)
pairs = ['H1-H2', 'H1-H3', 'H1-H4', 'H2-H3', 'H2-H4', 'H3-H4', 'C-H1', 'C-H2', 'C-H3', 'C-H4']
num_rows = int(np.ceil(len(pairs) / 2))
num_cols = min(len(pairs), 2)
colors = plt.cm.tab10(np.linspace(0, 1, len(pairs)))
fig, axs = plt.subplots(num_rows, num_cols, figsize=(20, 20))
for i, pair in enumerate(pairs):
    row_idx = i // num_cols
    col_idx = i % num_cols
    axs[row_idx][col_idx].hist(d1[:, i], bins=20, color=colors[i], edgecolor='black')
    axs[row_idx][col_idx].set_title(pair)
    axs[row_idx][col_idx].set_xlabel('Distance')
    axs[row_idx][col_idx].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

# code here!
split_data(data, n_tr=50, n_val=250, )
num_test_points = 1000
