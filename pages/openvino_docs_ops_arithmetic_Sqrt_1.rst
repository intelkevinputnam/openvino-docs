.. index:: pair: page; Sqrt
.. _doxid-openvino_docs_ops_arithmetic__sqrt_1:


Sqrt
====

:target:`doxid-openvino_docs_ops_arithmetic__sqrt_1_1md_openvino_docs_ops_arithmetic_sqrt_1` **Versioned name** : *Sqrt-1*

**Category** : *Arithmetic unary*

**Short description** : Square root element-wise operation.

**Detailed description** : *Sqrt* performs element-wise square root operation on a given input tensor ``a``, as in the following mathematical formula, where ``o`` is the output tensor:

.. math::

	o_{i} = \sqrt{a_{i}}

* If the input value is negative, then the result is undefined.

* For integer element type the result is rounded (half up) to the nearest integer value.

**Attributes** : *Sqrt* operation has no attributes.

**Inputs**

* **1** : A tensor of type *T* and arbitrary shape. **Required.**

**Outputs**

* **1** : The result of element-wise *Sqrt* operation. A tensor of type *T* and the same shape as input tensor.

**Types**

* *T* : any numeric type.

**Examples**

*Example 1*

.. ref-code-block:: cpp

	<layer ... type="Sqrt">
	    <input>
	        <port id="0">
	            <dim>4</dim> <!-- float input values: [4.0, 7.0, 9.0, 10.0] -->
	        </port>
	    </input>
	    <output>
	        <port id="1">
	            <dim>4</dim> <!-- float output values: [2.0, 2.6457512, 3.0, 3.1622777] -->
	        </port>
	    </output>
	</layer>

*Example 2*

.. ref-code-block:: cpp

	<layer ... type="Sqrt">
	    <input>
	        <port id="0">
	            <dim>4</dim> <!-- int input values: [4, 7, 9, 10] -->
	        </port>
	    </input>
	    <output>
	        <port id="1">
	            <dim>4</dim> <!-- int output values: [2, 3, 3, 3] -->
	        </port>
	    </output>
	</layer>

*Example 3*

.. ref-code-block:: cpp

	<layer ... type="Sqrt">
	    <input>
	        <port id="0">
	            <dim>256</dim>
	            <dim>56</dim>
	        </port>
	    </input>
	    <output>
	        <port id="1">
	            <dim>256</dim>
	            <dim>56</dim>
	        </port>
	    </output>
	</layer>

