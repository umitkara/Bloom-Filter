# Bloom Filter

## About Bloom Filter

Data structure theorized by *Burton Howard Bloom* in 1970. Bloom Filter is a space-efficient, probabilistic (Monte Carlo) data structure. It is used to test whether an element is part of a list (set).  It is used in Caching (especially on *CDN* and *DNS* servers), routers, some I/O devices, primitive spell checkers, distributed databases and file systems, and web crawlers. 
New elements can be added to bloom filter, but not deleted.  The more elements are added to the bloom filter, the greater the probability of a false positive.
Since bloom filter is a Monte Carlo type data structure, it is possible to give false positive outputs, but not false negatives. The reason for not giving a false negative is that the element cannot be deleted from the data structure.

Bloom filter has been developed over time because it is a data structure with a history of 50 years.  *Bloomier filter* is a more advanced version that does not give false positives, *combining bloom filter* is a version that prevents false positives by using multiple filters, *layered bloom filter* is a version that aims to prevent conflicts and false positives by using more than one filter in layered form, and *counting bloom filter* is a version that can allow element deletion.

Bloom filter is based on a bit array with *m bit* length.  Each element to be added to the filter is hashed *k* times with *k hash* functions. With the resulting k hash, it is determined which bits will be converted from 0 to 1 on the bit array. If the bit is already 1, it is not changed.
In bloom filter, the query hashes to search, just like while adding elements. The resulting hashes determine the k bits to look at. If all the bits looked at are 1, the query is probably an element of bloom filter, but it can also be a false positive. The number of bits or hash functions in the filter can be increased to reduce false positives.

The error rate of the filter can be found by the following formula: 
$$p = (1 - (1 - (\frac{1}{m})^{(k*n)}))^k$$
where *m* represents the number of bits, *k* represents the number of hash functions, and *n* represents the number of elements in the filter.
If the number of values (n) we will keep in the filter is certain, it can also calculate in advance how many bits of array and how many hash functions the filter should use.

The number of bits is found by using the following formula: 
$$m = -n*\frac{\ln(p)}{\ln(2)^2}$$
where *p* is the error rate of the filter and *n* is the number of elements to be kept.
The number of hash functions can also be found by the following formula:
$$k = -\frac{\ln(p)}{\ln (2)}$$

## Bloom Filter Example

In this repository, I have implemented a bloom filter in Python. My implementation accepts at most 2 hash functions for the sake of simplicity.
As hash functions, I have used *MD5* and *SHA-2* with *base64* encoding.

API:
```python
insert(element:str) -> None
search(element:str) -> bool
size() -> int
```