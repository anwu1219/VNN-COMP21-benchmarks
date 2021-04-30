This repo contains three cifar10 classifers.
The input image is normalized between 0-1.

The architecture of the three networks can be found in `architecture.txt`
The script generate_linf_robustness_query.py can be used to generate l-inf
targeted robustness queries for a given test image and epsilon. for example:
```python generate_linf_robustness_query.py --index 0 --eps 0.03 > example_query.vnnlib```
will pipe a vnnlib query that checks the first test image with epsilon 0.03.

The target label is set to be `(correct label + 1 % 10)`
