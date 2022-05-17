.. index:: pair: page; ShapeOf
.. _doxid-openvino_docs_ops_shape__shape_of_1:


ShapeOf
=======

:target:`doxid-openvino_docs_ops_shape__shape_of_1_1md_openvino_docs_ops_shape_shapeof_1` **Versioned name** : *ShapeOf-1*

**Category** : *Shape manipulation*

**Short description** : *ShapeOf* produces 1D tensor with the input tensor shape.

**Attributes** : has no attributes.

**Inputs** :

* **1** : Arbitrary input tensor. **Required.**

**Outputs** :

* **1** : 1D tensor that is equal to input tensor shape. Number of elements is equal to input tensor rank. Can be empty 1D tensor if input tensor is a scalar, that mean 0-dimensional tensor.

**Example**

.. ref-code-block:: cpp

	<layer ... type="ShapeOf">
	    <input>
	        <port id="0">
	            <dim>2</dim>
	            <dim>3</dim>
	            <dim>224</dim>
	            <dim>224</dim>
	        </port>
	    </input>
	    <output>
	        <port id="1">  <!-- output value is: [2,3,224,224]-->
	            <dim>4</dim>
	        </port>
	    </output>
	</layer>

