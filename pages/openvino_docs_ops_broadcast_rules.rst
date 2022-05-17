.. index:: pair: page; Broadcast Rules For Elementwise Operations
.. _doxid-openvino_docs_ops_broadcast_rules:


Broadcast Rules For Elementwise Operations
==========================================

:target:`doxid-openvino_docs_ops_broadcast_rules_1md_openvino_docs_ops_broadcast_rules` The purpose of this document is to provide a set of common rules which are applicable for ops using broadcasting.

Description
~~~~~~~~~~~

Broadcast allows to perform element-wise operation for inputs of arbitrary number of dimensions. There are 2 types of broadcasts supported: Numpy and PDPD.

Rules
~~~~~

**None broadcast** :

#. Input tensors dimensions must match.

#. No implicit broadcast rule is applied.

**Numpy broadcast** :

#. Right aligned dimensions of the two tensors are compared elementwise.

#. Smaller tensor is prepended with dimension(s) of size 1 in order to have the same shape as the larger tensor.

#. After alignment two tensors are compatible when both are equal or one of the dimensions is 1.

#. Tensor with dimension of size 1 will be implicitly broadcasted to match the size of the second tensor.

#. When both inputs are of rank = 0 the result is a scalar.

**PDPD broadcast** :

#. First input tensor A is of any rank, second input B has rank smaller or equal to the first input.

#. Input tensor B is a continuous subsequence of input A.

#. Apply broadcast B to match the shape of A, where provided *axis* is the start dimension index for broadcasting B onto A.

#. If *axis* is set to default (-1) calculate new value: ``axis = rank(A) - rank(B)``.

#. The trailing dimensions of size 1 for input B will be ignored for the consideration of subsequence, such as ``shape(B) = (3, 1) => (3)``.

Numpy examples
~~~~~~~~~~~~~~

* ``A: Shape(,) -> scalar``
  
  ``B: Shape(,) -> scalar``
  
  ``Result: Shape(,) -> scalar``

* ``A: Shape(2, 3)``
  
  ``B: Shape(   1)``
  
  ``Result: Shape(2, 3)``

* ``A: Shape(   3)``
  
  ``B: Shape(2, 3)``
  
  ``Result: Shape(2, 3)``

* ``A: Shape(2, 3, 5)``
  
  ``B: Shape(,) -> scalar``
  
  ``Result: Shape(2, 3, 5)``

* ``A: Shape(2, 1, 5)``
  
  ``B: Shape(1, 4, 5)``
  
  ``Result: Shape(2, 4, 5)``

* ``A: Shape(   6, 5)``
  
  ``B: Shape(2, 1, 5)``
  
  ``Result: Shape(2, 6, 5)``

* ``A: Shape(2, 1, 5)``
  
  ``B: Shape(   4, 1)``
  
  ``Result: Shape(2, 4, 5)``

* ``A: Shape(3, 2, 1, 4)``
  
  ``B: Shape(      5, 4)``
  
  ``Result: Shape(3, 2, 5, 4)``

* ``A: Shape(   1, 5, 3)``
  
  ``B: Shape(5, 2, 1, 3)``
  
  ``Result: Shape(5, 2, 5, 3)``

* ``A: Shape(3)``
  
  ``B: Shape(2)``
  
  ``Result: broadcast won't happen due to dimensions mismatch``

* ``A: Shape(3, 1, 5)``
  
  ``B: Shape(4, 4, 5)``
  
  ``Result: broadcast won't happen due to dimensions mismatch on the leftmost axis``

PDPD examples
~~~~~~~~~~~~~

* ``A: Shape(2, 3, 4, 5)``
  
  ``B: Shape(   3, 4   ) with axis = 1``
  
  ``Result: Shape(2, 3, 4, 5)``

* ``A: Shape(2, 3, 4, 5)``
  
  ``B: Shape(   3, 1   ) with axis = 1``
  
  ``Result: Shape(2, 3, 4, 5)``

* ``A: Shape(2, 3, 4, 5)``
  
  ``B: Shape(      4, 5) with axis=-1(default) or axis=2``
  
  ``Result: Shape(2, 3, 4, 5)``

* ``A: Shape(2, 3, 4, 5)``
  
  ``B: Shape(1, 3      ) with axis = 0``
  
  ``Result: Shape(2, 3, 4, 5)``

* ``A: Shape(2, 3, 4, 5)``
  
  ``B: Shape(,)``
  
  ``Result: Shape(2, 3, 4, 5)``

* ``A: Shape(2, 3, 4, 5)``
  
  ``B: Shape(5,)``
  
  ``Result: Shape(2, 3, 4, 5)``



.. _doxid-openvino_docs_ops_broadcast_rules_1openvino_docs_ops_bidirectional_broadcast_rules:

Bidirectional Broadcast Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
-----------

Bidirectional Broadcast is not intended for element-wise operations. Its purpose is to broadcast an array to a given shape.

Rules
-----

**Bidirectional broadcast** :

#. Dimensions of the input tensors are right alignment.

#. Following broadcast rule is applied: ``numpy.array(input) \* numpy.ones(target_shape)``.

#. Two corresponding dimension must have the same value, or one of them is equal to 1.

#. Output shape may not be equal to ``target_shape`` if:
   
   * ``target_shape`` contains dimensions of size 1,
   
   * ``target_shape`` rank is smaller than the rank of input tensor.

Bidirectional examples
----------------------

* ``A: Shape(5)``
  
  ``B: Shape(1)``
  
  ``Result: Shape(5)``

* ``A: Shape(2, 3)``
  
  ``B: Shape(   3)``
  
  ``Result: Shape(2, 3)``

* ``A: Shape(3, 1)``
  
  ``B: Shape(3, 4)``
  
  ``Result: Shape(3, 4)``

* ``A: Shape(3, 4)``
  
  ``B: Shape(,) -> scalar``
  
  ``Result: Shape(3, 4)``

* ``A: Shape(   3, 1)``
  
  ``B: Shape(2, 1, 6)``
  
  ``Result: Shape(2, 3, 6)``

