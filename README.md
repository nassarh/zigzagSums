# zigzagSums
construct origami-like quad-based polyhedral surfaces



## Definitions
* A *zigzag* is a piecewise linear space curve invariant by translation along $A_1A_3$ where $A_1$ is its first vertex and $A_3$ is its third vertex.
* A *zigzag sum* is the the sum of two zigzags: take every point of one zigzag and add it, by translation as a vector, to every point of another zigzag to produce a polyhedral surface.

## Observations
* A zigzag sum is a polyhedral surface composed of parallelograms.
* The period of a zigzag sum, in particular, is composed of $2\times 2$ parallelograms.
* It is possible to deform a zigzag sum in a way that preserves the lengths of all edges and that *almost* preserves the planarity of the facets.
* Well-known examples of zigzag sums are the "Miura-ori" pattern and the "eggbox" pattern.

## Contents
* ``zigzagsum.py`` contains functions that allow to construct surfaces that are "screw symmetric" deformed zigzag sums.
* The remaining files are examples.

## How it works
* The input is the deformed state of one period of a zigzag, i.e., an angle, and the rotation matrix that defines the "screw symmetry".
* Letting the rotation act on the period produces the first row of vertices of the desired surface.
* The next row is found by ensuring that edges maintain their lengths. This involves iterating a function that constructs the intersection of three spheres.
* The construction is pursued as long as said spheres have an intersection. If they don't, the construction stops.

## Dependencies
* ``numpy`` and ``pyvista``

## References
* https://hal.science/hal-01368009v1/file/MainDocument.pdf
* https://arxiv.org/pdf/2207.08752
* https://hal-enpc.archives-ouvertes.fr/hal-01978795v1/file/7OSME-paper-Nassar-Lebee-Monasse-8.pdf
* https://hal-enpc.archives-ouvertes.fr/hal-01691183v1/file/IASS17_revised.pdf

## Acknowledgments
* https://www.nsf.gov/awardsearch/showAward?AWD_ID=2045881
* http://mmcd.univ-paris-est.fr/funded-projects/post-doc-projects/
