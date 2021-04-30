from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--index', type=int, default=0, help='index of the test image in the test set')
parser.add_argument('--eps', type=float, default=0.01, help='radius of the l-inf ball')

args = parser.parse_args()

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

index = args.index
epsilon = args.eps

image = test_images[index].flatten()/255
label = test_labels[index][0]
targetLabel = (label + 1) % 10

print("; index {}, correct label {}, target label {}, epsilon {}".format(index,label, targetLabel,epsilon))

for i in range(3*32*32):
    print("(declare-const X_{} Real)".format(i))

for i in range(10):
    print("(declare-const Y_{} Real)".format(i))

print( "; Input constraints")
for i in range(3*32*32):
    val = image[i]
    lb = max(0, val - epsilon)
    ub = min(1, val + epsilon)
    print("(assert (<= X_{} {})".format(i, ub))
    print("(assert (>= X_{} {})".format(i, lb))

print( "; Output constraints")
for i in range(10):
    if i != targetLabel:
        print("(assert (>= Y_{} Y_{}))".format(targetLabel, i))
