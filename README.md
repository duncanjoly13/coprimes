# Exploring Modular Multiples of Coprime Numbers

This short Python project aims to prove whether for every pair of coprime numbers [x, y] that the function
`(min(x, y) * n) % max(x, y)` produces each natural number less than `max(x, y)` at least once.

##### Usage
`python3 main.py`

CSV output will be saved to "coprimes-**{minP}**-to-**{maxP}**_n-**{minN}**-to-**{maxN}**.csv" and a plot will be saved
to "coprimes-**{minP}**-to-**{maxP}**_n-**{minN}**-to-**{maxN}**.png", where the bold entries are replaced by their
respective values

##### Dependencies
`matplotlib`
`numpy`