.. index:: pair: page; Log
.. _doxid-openvino_docs_ops_arithmetic__log_1:


Log
===

:target:`doxid-openvino_docs_ops_arithmetic__log_1_1md_openvino_docs_ops_arithmetic_log_1` **Versioned name** : *Log-1*

**Category** : *Arithmetic unary*

**Short description** : *Log* performs element-wise natural logarithm operation with given tensor.

**Detailed description** : *Log* does the following with the input tensor *a* :

.. math::

	a_{i} = log(a_{i})

**Attributes** :

.. code-block:: cpp

	No attributes available.

**Inputs**

* **1** : An tensor of type *T* and arbitrary shape. **Required.**

**Outputs**

* **1** : The result of element-wise log operation. A tensor of type *T* and the same shape as input.

**Types**

* *T* : any numeric type.

**Examples**

*Example 1*

.. ref-code-block:: cpp

	<layer ... type="Log">
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

