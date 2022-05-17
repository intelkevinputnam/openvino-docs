.. index:: pair: page; Sigmoid
.. _doxid-openvino_docs_ops_activation__sigmoid_1:


Sigmoid
=======

:target:`doxid-openvino_docs_ops_activation__sigmoid_1_1md_openvino_docs_ops_activation_sigmoid_1` **Versioned name** : *Sigmoid-1*

**Category** : *Activation function*

**Short description** : Sigmoid element-wise activation function.

**Detailed description** : `Reference <https://deepai.org/machine-learning-glossary-and-terms/sigmoid-function>`__

**Attributes** : *Sigmoid* operation has no attributes.

**Mathematical Formulation**

For each element from the input tensor calculates corresponding element in the output tensor with the following formula:

.. math::

	sigmoid( x ) = \frac{1}{1+e^{-x}}

**Inputs** :

* **1** : Input tensor *x* of any floating-point type. **Required.**

**Outputs** :

* **1** : Result of Sigmoid function applied to the input tensor *x*. Floating-point tensor with shape and type matching the input tensor.

**Example**

.. ref-code-block:: cpp

	<layer ... type="Sigmoid">
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

