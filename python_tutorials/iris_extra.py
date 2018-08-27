# Some matplotlib code to complement iris.py. Visualizes the initial clusters.

features2, label2 = iter(train_dataset).next()
features3, label3 = iter(train_dataset).next()
features4, label4 = iter(train_dataset).next()

np_features = features.numpy()
np_features = np.append(features2.numpy(), np_features)
np_features = np.append(features2.numpy(), np_features)
np_features = np.append(features2.numpy(), np_features)
all_features = np.array(np.split(np_features, 128))

np_labels = label.numpy()
np_labels = np.append(label2.numpy(), np_labels)
np_labels = np.append(label3.numpy(), np_labels)
np_labels = np.append(label4.numpy(), np_labels)

two_features = []
for flower in all_features:
    new_flower = []
    for i in range(len(flower)):
        if i == 2 or i == 3:
            new_flower.append(flower[i])
    two_features.append(new_flower)

# Graph 2 features against each other. Different colors are different iris species.
x, y = zip(*two_features)
col = []
for species in np_labels:
    if species == 0:
        col.append('r')
    elif species == 1:
        col.append('g')
    else:
        col.append('b')
plt.scatter(x, y, c=col)
plt.show()
